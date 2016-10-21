#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-10-20 15:38:21
# @Last Modified by:   anchen
# @Last Modified time: 2016-10-20 15:49:29

def quickSort(alist,low,high):
	if low < high:
		pos = findpos(alist,low,high)
		quickSort(alist,low,pos-1)
		quickSort(alist,pos+1,high)
def findpos(alist,left,right):
	temp = alist[left]
	while left < right:
		while left < right and alist[right] >= temp:
			right -=1
		alist[left] = alist[right]
		while left < right and alist[left] <= temp:
			left +=1
		alist[right] = alist[left]
	alist[left] = temp
	return left

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist,0,8)
print(alist)