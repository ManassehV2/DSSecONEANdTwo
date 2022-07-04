class Node:
    def __init__(self,Value):
        self.Value = Value
        self.Next = None

class LinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.Size = 0

    def AddFirst(self, val):
        newNode = Node(val)
        if(self.Head == None):
            self.Head = newNode
            self.Tail = newNode
            self.Size += 1
        else:
            newNode.Next = self.Head
            self.Head = newNode
            self.Size += 1

    def AddLast(self, val):
        newNode = Node(val)
        if(self.Head == None):
            self.Head = newNode
            self.Tail = newNode
            self.Size += 1
        else:
            self.Tail.Next = newNode
            newNode.Next = None
            self.Size += 1
    def GetLinkedListVals(self):
        Vals = []
        current = self.Head
        while( current != None):
            Vals.append(current.Value)
            current = current.Next
        return Vals

    def Add(self,val,index):
        newNode = Node(val)
        current = self.Head
        pos = 0
        while(pos < index - 1):
            current = current.Next
            pos += 1
        newNode.Next = current.Next
        current.Next = newNode





def main():
    myLinkedList = LinkedList()
    myLinkedList.AddFirst("d")
    myLinkedList.AddFirst("c")
    myLinkedList.AddFirst("b")
    myLinkedList.AddFirst("a")
    print(myLinkedList.GetLinkedListVals())
    myLinkedList.AddLast("e")
    print(myLinkedList.GetLinkedListVals())
    myLinkedList.Add("z", 3)
    print(myLinkedList.GetLinkedListVals())

main()






