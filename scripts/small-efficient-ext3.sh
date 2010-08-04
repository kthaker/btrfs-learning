#!/bin/bash
#verify space efficient packing of small files

FILE_SIZE=4480
FILE_NUMS=10000
TEST_NUMS=10
STEP=1024
DATA_NAME=../ext3-data
MEDEDATA_SIZE=`df -B1 | awk '/sda9/ {print $3}'`

for i in $(seq $TEST_NUMS); do
    FILE_SIZE=`expr $FILE_SIZE + $STEP`
    for t in $(seq $FILE_NUMS); do
        dd if=/dev/urandom of=${t} bs=$FILE_SIZE count=1 2> /dev/null
    done
    sync
    TOTAL_SIZE=`df -B1 | awk '/sda9/ {print $3}'`
    ACTUAL_SIZE=`expr $TOTAL_SIZE - $MEDEDATA_SIZE`
    AVE_SIZE=`expr $ACTUAL_SIZE / $FILE_NUMS`
    echo  "$FILE_SIZE $AVE_SIZE" 
    rm * 2> /dev/null
    sync
done
