#!/usr/bin/env python
# -*- coding: utf-8 -*-
my_name = u'康 dalei' # raw: Zed A. Shaw
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_height
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." %(
    my_age, my_height, my_weight, my_age + my_height + my_weight)


# %d 整数
# %s 字符串
# %f 浮点数
# %x 十六进制整数
# %r 原始字符串，取消转义
# %% 在字符串中转义%
