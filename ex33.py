#!/usr/bin/env python
# -*- coding: utf-8 -*-


def while_loop(top_num, step):
    i = 0
    numbers = []
    while i < top_num:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers


numbers = while_loop(8, 2)

for num in numbers:
    print num
