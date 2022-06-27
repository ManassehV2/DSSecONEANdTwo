def BubbleSort(listToSort):
    for j in range(len(listToSort) - 1):
        for i in range(len(listToSort) - 1):
            if listToSort[i] > listToSort[i + 1]:
                listToSort[i] = listToSort[i] + listToSort[i + 1]
                listToSort[i + 1] = listToSort[i] - listToSort[i + 1]
                listToSort[i] = listToSort[i] - listToSort[i + 1]
def main():
    listToSort = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    print("List before sorting")
    print(listToSort)
    BubbleSort(listToSort)
    print("List after sorting")
    print(listToSort)

if __name__ == "__main__":
    main()
