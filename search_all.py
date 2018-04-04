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

    log.info("setting keyspace...")
    session.set_keyspace(KEYSPACE)

    prepared = session.prepare("""
        SELECT * FROM test_table WHERE val1=? AND val2=? AND val3=? AND val4=? AND val5=? AND val6=? AND val7=? AND val8=?
        """)

    i = 0
    filename = str(argv[0])
    with open(filename, 'r') as fp:
        for line in fp:
            i = i + 1
            log.info("reading row %d" % i)
            line_split = line.split()
            rows = session.execute(prepared.bind((float(line_split[1]), float(line_split[2]), float(line_split[3]), float(line_split[4]), float(line_split[5]), float(line_split[6]), float(line_split[7]), float(line_split[8]))))
            for row in rows:
                log.info(row)

    cluster.shutdown()
    log.info("")

if __name__ == "__main__":
    main(sys.argv[1:])
