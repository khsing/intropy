#!/usr/bin/env python
#coding:utf-8

import os
import sys
import fnmatch

def pyfind(top,s=2):
    for p,dl,fl in os.walk(top):
        for f in fl:
            ffp = os.path.join(p,f)
            if os.path.getsize(ffp) > int(s)*1024*1024:
                yield ffp

def main():
    if len(sys.argv) != 3:
        print "Err: bad option"
        sys.exit(1)
    else:
        for f in pyfind(sys.argv[1],sys.argv[2]):
            print f

if __name__=="__main__":
    main()
