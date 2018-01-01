#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print( "%s\r" % i, end = " ") # 以空格结尾，而不是newline
        # 默认 end='\n'  在python2 中写法
        # print "string", 
