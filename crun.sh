#!/bin/sh

CMD=$1
LOCAL_PATH=$(pwd)
CASSIMDRA_PATH=/home/mourao/Workspace/cassandra-sim
CASSIMDRA_BIN=$CASSIMDRA_PATH/bin

build() {
    echo 'Removing build/ directory'
    rm -rf $CASSIMDRA_PATH/build

    echo 'Building Cassimdra'
    ant
}

start() {
    $LOCAL_PATH/ckill.sh

    echo ''
    echo 'Starting Cassimdra'

    cd $CASSIMDRA_BIN
    $CASSIMDRA_BIN/cassandra
}

echo ''
echo $LOCAL_PATH
echo 'Starting'

cd $CASSIMDRA_PATH
echo 'Removing data/ directory'
rm -rf $CASSIMDRA_PATH/data

case "$1" in
    ('build') build ;;
    ('start') start ;;
    (*) build && start ;;
esac

cd $LOCAL_PATH

echo ''
echo 'Finish'

