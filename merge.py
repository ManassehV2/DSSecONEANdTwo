def MergeSort(listToSort):
    if len(listToSort) > 1:
        leftHalf = listToSort[: len(listToSort) // 2]
        MergeSort(leftHalf)
        rightHalf = listToSort[len(listToSort) // 2 : ]
        MergeSort(rightHalf)
        Merge(leftHalf,rightHalf,listToSort)
    return listToSort

def Merge(leftHalf,rightHalf,listToSort):
    index1 = 0
    index2 = 0
    index3 = 0

    while(index1 < len(leftHalf) and index2 < len(rightHalf)):
        if(leftHalf[index1] < rightHalf[index2]):
            listToSort[index3] = leftHalf[index1]
            index1 += 1
            index3 += 1
        else:
            listToSort[index3] = rightHalf[index2]
            index2 += 1
            index3 += 1
    if(index1 < len(leftHalf)):
        while(index1 < len(leftHalf)):
            listToSort[index3] = leftHalf[index1]
            index1 += 1
            index3 += 1
    else:
        while(index2 < len(rightHalf)):
            listToSort[index3] = rightHalf[index2]
            index2 += 1
            index3 += 1

print(MergeSort([4,1,3,2,0]))    
    


    


    
