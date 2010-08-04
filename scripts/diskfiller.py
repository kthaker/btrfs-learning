#!/usr/bin/env python
# create directory and file for testing fsck

import sys
import os
import os.path
import string

FROM_DIR="."

#LEAF_ALPHA_LEVEL=3
#BRANCH_ALPHA_LEVEL=3
DIR_LEVEL=3
FILE_IN_EACH_LEAF=100

INITIAL_CONTENT_SIZE=1024
APPEND_CONTENT_SIZE=1024

alphas = string.ascii_lowercase[::-1]

def perms(alphabet, size):
    if size==0:
        yield ""
    else:
        for first in alphabet:
            for rest in perms(alphabet, size-1):
                yield first+rest

file_names_rev = ["f%05d"%x for x in reversed(range(FILE_IN_EACH_LEAF))]
dir_names_rev = list(alphas)

initial_content = "\0"*INITIAL_CONTENT_SIZE
append_content = "\0"*APPEND_CONTENT_SIZE

def enum_all_dirs(dir_names, depth, cur_path = "."):
    if depth>0:
        for name in dir_names:
            new_path = os.path.join(cur_path,name)
            yield new_path
            for subdirs in enum_all_dirs(dir_names, depth-1, new_path):
                yield subdirs

def enum_leaf_dirs(dir_names, depth, cur_path = '.'):
    if depth==0:
        yield cur_path
    else:
        for name in dir_names:
            new_path = os.path.join(cur_path,name)
            for subdirs in enum_leaf_dirs(dir_names, depth-1, new_path):
                yield subdirs

def enum_files(dir_names, file_names, depth, cur_path = '.'):
    for dir_path in enum_leaf_dirs(dir_names, depth, cur_path):
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            yield file_path

def enum_files_zigzag(dir_names, file_names, depth, cur_path = '.'):
    for file_name in file_names:
        for dir_path in enum_leaf_dirs(dir_names, depth, cur_path):
            file_path = os.path.join(dir_path, file_name)
            yield file_path

def work(dir_names, file_names, depth, prefix = '.'):
    for dir in enum_all_dirs(dir_names, depth, prefix):
        os.mkdir(dir)

    for file_path in enum_files_zigzag(dir_names, file_names, depth, prefix):
        f = open(file_path, "w")
        f.write(initial_content)
        f.close()

    for file_path in enum_files(dir_names, file_names, depth, prefix):
        f = open(file_path, "a")
        f.write(append_content)
        f.close()

if __name__=="__main__":
    work(dir_names_rev, file_names_rev, DIR_LEVEL, FROM_DIR)
