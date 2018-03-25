#!/bin/sh

C_PID=$(ps aux | grep [c]assandra | awk '{print $2}')

echo ''

if [ -z $C_PID ]
then
    echo "No such process"
else
    echo "Killing Cassimdra process: $C_PID"
    kill $C_PID
fi
