# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:28:16 2019

@author: DELL
"""

for i in range(int(input())):
    n=int(input())
    l=[]
    c=0
    ma=0
    l=[int(x) for x in input().split()]
    for j in range(1,n):
        c=0
        for k in range(j):
            if(l[k]%l[j]==0):
                c+=1
        if(c>ma):
            ma=c
        c=0
    print(ma)
            