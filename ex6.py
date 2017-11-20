#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给x赋值一个字符串
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don'n t"
# 给y赋值，格式化替换          
y = "Those who know %s and those who %s ." % (binary, do_not)

print x
print y
# 有点字符串拼接的意思, 注意%r x字符串自动带引号,%r显示原始格式
print "I said: %r." % x
# %s 字符串无引号
print "I also said: %s" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e

