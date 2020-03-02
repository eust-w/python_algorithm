#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:insert_sort.py
@time:2020/03/02
"""
import random


def insert_sort(a: list)->list:
    for i in range(len(a)-1):
        if a[i+1] < a[0]:
            a.insert(0, a[i+1])
            a.pop(i+2)
        else:
            for j in range(i):
                if a[j] <= a[i+1] <= a[j+1]:
                    a.insert(j+1, a[i+1])
                    a.pop(i+2)
    return a


if __name__ == '__main__':
    q = int(input('enter list size:'))
    l1 = list(range(q))
    random.shuffle(l1)

    l2 = insert_sort(l1)
    l3 = sorted(l1)

    print(l2 == l3)
