#!/usr/bin/env python
# get disk usage of btrfs from btrfs filesystem df .

import re
import sys

used_pattern = re.compile(r'used=(?P<num>[0-9.]+)(?P<unit>[KMGT])B')

s = 0.0

input_str = sys.stdin.read()

results = used_pattern.findall(input_str)
for num_str, unit_str in results:
    num = float(num_str)
    unit = {'K':2**10, 'M':2**20, 'G':2**30, 'T':2**40}[unit_str]
    s += num*unit

s_int = int(s)
print s_int

