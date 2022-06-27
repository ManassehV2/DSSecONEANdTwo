from Heap import Heap

def HeapSort(lst):
    myHeap = Heap()
    for item in lst:
        myHeap.add(item)
    
    for i in range(len(lst)):
        lst[len(lst) - 1 - i] = myHeap.remove()

    return lst


print(HeapSort([24,63,71,89,-10,0,-6]))
    