#!/usr/bin/env python
#coding:utf-8

import sys
import os
import re

def fmap(dictseq,col,func):
    for d in dictseq:
        d[col] = func(d[col])
        yield d

def analog(logfile):
    cols = ('ip','host','user','datetime','method','request','proto','status','bytes','ref','agent')
    pats = re.compile(r'(\S+) (\S+) (\S+) \[(.*?)\] "(\S+) (\S+) (\S+)" (\S+) (\S+) "(\S+)" "(.*?)"')
    lines = (dict(zip(cols,pats.match(i).groups())) for i in open(logfile))
    log = log = fmap(lines,'status',int)
    log = fmap(log,'bytes',lambda s:int(s) if s != '-' else 0)
    return log

def analog2(logfile):
    lines = (line.rsplit(None,5)[1] for line in open(logfile))
    bytes = (int(x) for x in lines if x != '-')
    return bytes

def main():
    if len(sys.argv) != 3:
        print "Err: bad option"
        sys.exit(1)
    else:
        if sys.argv[2] == 're':
            log = analog(sys.argv[1])
            print "Total byte: %d" % sum(r['bytes'] for r in log)
        elif sys.argv[2] == 'split':
            log = analog2(sys.argv[1])
            print "Total byte: %d" % sum(log)
        

if __name__=="__main__":
    main()
