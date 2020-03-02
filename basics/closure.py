#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:closure.py
@time:2020/03/02
"""
"""
q = 12


def count():
    l = []
    for i in range(1, 4):
        def fun():
            return i**i
        l.append(fun())
        print(q)
    return l


f1, f2, f3 = count()

print(f1, f2, f3)


# q = list(range(12))
#
# q = (x for x in range(12) if x < 8)
#
# q = aq a: a**2
"""
def fun1(_ = lambda x, y, z: x+y+z):


t2 = lambda x: x**2

q = t(1, 2, 3)
q2 = t2(4)

print(q,q2)

