def insertSort(alist):
    for index in range(1,len(alist)):
        temp = alist[index]
        position = index
        while position > 0 and alist[position-1] > temp:
            alist[position] = alist[position-1]
            position = position -1
        alist[position] = temp

alist = [54,26,93,17,77,31,44,55,20]
insertSort(alist)
print(alist)
