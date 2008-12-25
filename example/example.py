#!/usr/bin/env python
# coding=utf-8

import os
import sys
import datetime
import time

def ago(days):
    timestamp = time.time() - days * 86400
    return datetime.date.fromtimestamp(timestamp)

def get_files(path):
    import glob
    return glob.glob('%s/?[0-9][0-9].txt' % path)

def read_file(fobj):
    fobj.seek(0)
    lines = fobj.readlines()
    return dict(map(lambda x:x.split(),lines))

def init_data(d):
    '''
    >>> init_data({"a":"1","b":"2"})
    {'a': 1, 'b': 2}
    '''
    for i in d.keys():
        d[i] = int(d[i])
    return d

def plus_dict(d1,d2):
    for i in d1:
        if d2.has_key(i):
            d1[i] += d2[i]
            d2.pop(i)
    for j in d2:
        d1[j] = d2[j]
    return d1

def md5sum(fobj):
    fobj.seek(0)
    from hashlib import md5
    return md5(fobj.read()).hexdigest()

def write_data(fobj,d):
    for i in d:
        fobj.write("%s %s\n" % (i,str(d[i])))

def main():
    import doctest
    doctest.testmod()

    day = ago(1)
    path = day.strftime('%y%m%d')
    files = get_files(path)
    result = "%s.txt" % path
    data = {}
    sum = {}
    for f in files:
        fd_r = open(f,'r')
        plus_dict(data,init_data(read_file(fd_r)))
        sum[f] = md5sum(fd_r)
    fd_w = open(result,'w')
    fd_w.write("====Result====\n")
    write_data(fd_w,data)
    fd_w.write("====Files====\n")
    write_data(fd_w,sum)

if __name__=="__main__":
    main()
