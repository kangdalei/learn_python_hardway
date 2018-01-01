#!/usr/bin/env python
# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* fishies
\t* catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i, # \r 回车 回到行首，覆盖掉之前输出的字符
        # 结尾的 , 表示输出不换行，以空格结尾，而不是换行符newline
