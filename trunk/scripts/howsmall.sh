#!/bin/bash
#verify how small when it is not small files
#but it can't
FILENAME=file3
TEXT='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

HOW_MANY_TIME=1000

for t in $(seq $HOW_MANY_TIME);do
echo $TEXT >> $FILENAME
btrfsctl -c $FILENAME > /dev/null
sleep 0.5
echo -n "$t "
echo -n "$(wc -c <$FILENAME) "
df -B1 | awk '/sda8/ {print $3}'
done
