#!/bin/bash
#verify space efficient packing of small files

FILE_SIZE=0
FILE_NUMS=10000
TEST_NUMS=40
STEP=128
DATA_NAME=../btrfs-data

for i in $(seq $TEST_NUMS); do
    FILE_SIZE=`expr $FILE_SIZE + $STEP`
    for t in $(seq $FILE_NUMS); do
        dd if=/dev/urandom of=${t} bs=$FILE_SIZE count=1 2> /dev/null
    done
    sync
    TOTAL_SIZE=`btrfs f df . | python ../outproc.py`
    AVE_SIZE=`expr $TOTAL_SIZE / $FILE_NUMS`
    echo  "$FILE_SIZE $AVE_SIZE" 
    rm * 2> /dev/null
    sync
done
