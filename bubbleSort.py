#coding=utf-8

def bubbleSort(alist):
	for sorttime in range(len(alist)-1,0,-1):
		for i in range(sorttime):
			if alist[i] > alist[i+1]:
				tmp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = tmp

alist = [54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print alist