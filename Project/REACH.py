# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:42:39 2019

@author: samer
"""
##REACH 1
with open('housing.data') as fp:
    housingList = [line.split(maxsplit=14) for line in fp]
    for i in housingList:
        print(i)
        
##REACH 2        