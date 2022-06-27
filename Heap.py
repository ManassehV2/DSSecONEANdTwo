class Heap:
    def __init__(self):
        self.__list = []

    def add(self, node):
        self.__list.append(node)
        currentIndex = len(self.__list) - 1
        while currentIndex > 0:
            parentIndex = (currentIndex -1) // 2
            if self.__list[currentIndex] > self.__list[parentIndex]:
                self.__list[currentIndex], self.__list[parentIndex] = \
                    self.__list[parentIndex], self.__list[currentIndex]
                currentIndex = parentIndex
            else:
                break
    def remove(self):
        removedNode = self.__list[0]
        self.__list[0] = self.__list[-1]
        self.__list.pop()
        currentIndex = 0
        while currentIndex < len(self.__list):
            leftChieldIndex = 2 * currentIndex + 1
            rightChieldIndex = 2 * currentIndex + 2

            if leftChieldIndex >= len(self.__list):
                break 
            maxChiledIndex = leftChieldIndex
            if rightChieldIndex < len(self.__list):
                if self.__list[rightChieldIndex] > self.__list[maxChiledIndex]:
                    maxChiledIndex = rightChieldIndex
            
            self.__list[currentIndex], self.__list[maxChiledIndex] \
            = self.__list[maxChiledIndex], self.__list[currentIndex]

            currentIndex = maxChiledIndex


        return removedNode



    def getList(self):
        return self.__list
    def peek(self):
        return self.__list[0]
    def getSize(self):
        return len(self.__list)
    def isEmpty(self):
        return len(self.__list) == 0
