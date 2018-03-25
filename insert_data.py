#! /usr/bin/env python

import sys
import logging

log = logging.getLogger()
#log.setLevel('DEBUG')
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = "test"

def main(argv):
    log.info("")
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.default_timeout = 60 # seconds

    log.info("creating keyspace...")
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
        """ % KEYSPACE)

    log.info("setting keyspace...")
    session.set_keyspace(KEYSPACE)

    log.info("creating table...")
    session.execute("""
        CREATE TABLE test_table (
            num int, 
            val1 float, 
            val2 float, 
            val3 float, 
            val4 float, 
            val5 float, 
            val6 float, 
            val7 float, 
            val8 float, 
            PRIMARY KEY ((val1, val2, val3, val4, val5, val6, val7, val8))
        )
        """)

    prepared = session.prepare("""
        INSERT INTO test_table (num, val1, val2, val3, val4, val5, val6, val7, val8)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """)

    i = 0
    filename = str(argv[0])
    with open(filename, 'r') as fp:
        for line in fp:
            i = i + 1
            log.info("inserting row %d" % i)
            line_split = line.split()
            session.execute(prepared.bind((int(line_split[0]), float(line_split[1]), float(line_split[2]), float(line_split[3]), float(line_split[4]), float(line_split[5]), float(line_split[6]), float(line_split[7]), float(line_split[8]))))

    #log.info("dropping existing keyspace...")
    #session.execute("DROP KEYSPACE " + KEYSPACE)

    cluster.shutdown()
    log.info("")

if __name__ == "__main__":
    main(sys.argv[1:])
