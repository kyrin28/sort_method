#coding=utf-8

def selectSort(alist):
	for index in range(len(alist)-1,0,-1):
		positiomMax = 0
		for location in range(1,index+1):
			if alist[location] > alist[positiomMax]:
				positiomMax = location

		tmp = alist[index]
		alist[index] = alist[positiomMax]
		alist[positiomMax] = tmp

alist = [54,26,93,17,77,31,44,55,20,54,26,93,17,77,31,44,55,20]
selectSort(alist)
print alist