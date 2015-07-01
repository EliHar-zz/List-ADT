__author__ = 'Elias Haroun'

from List_ADT.list.Node import *

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def getHead(self):
        return self.head

    def setHead(self, aNode):
        self.head = aNode

    def insertLast(self, data):

        newNode = Node(data, None, None)

        if self.isEmpty():
            self.setHead(newNode)
        else:
            temp = self.head
            while temp.getNext() is not None:
                temp = temp.getNext()
            temp.setNext(newNode)

        self.size += 1

    def insertFirst(self, data):
        newNode = Node(data, None, None)
        newNode.setNext(self.getHead())
        self.setHead(newNode)
        self.size += 1

    def deleteLast(self):

        if self.isEmpty() is not True:
            temp = self.getHead()
            while temp.getNext().getNext() is not None:
                temp = temp.getNext()

            temp.setNext(None)
            self.size -= 1

    def deleteFirst(self):

        if self.isEmpty() is not True:
            self.setHead(self.head.getNext())
            self.size -= 1

    def getContent(self):
        result = []
        temp = self.getHead()

        while temp:
            result.append(temp.getData())
            temp = temp.getNext()

        print(result)

    # Finds the first occurance of the data and returns its index
    def find(self, data):
        index = 0
        temp = self.getHead()

        while temp:
            if temp.getData() == data:
                return index

            index += 1
            temp = temp.getNext()

        return -1