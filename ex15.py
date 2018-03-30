#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入 sys 模块里的 argv 类
from sys import argv
# 解包
script, filename = argv
# 打开 filename 文件，以只读模式，建立 txt 对象
txt = open(filename)

print "Here's your file %r: " % filename 
print txt.read()                # 调用 .read()方法
txt.close()                     # 关闭 txt 对象


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
