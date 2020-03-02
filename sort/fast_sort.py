#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:fast_sort.py
@time:2020/03/02
"""
import random


def fast_sort(a: list)->list:
    if len(a) < 2:
        return a
    head = list(x for x in a if x < a[0])
    middle = list(x for x in a if x == a[0])
    tail = list(x for x in a if x > a[0])
    return fast_sort(head) + middle + fast_sort(tail)


if __name__ == '__main__':
    q = int(input('enter list size:'))
    l1 = list(range(q))
    random.shuffle(l1)

    l2 = fast_sort(l1)
    l3 = sorted(l1)

    print(l2)
    print(l2 == l3)
