__author__ = 'Elias Haroun'

from List_ADT.list.Node import *

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def setHead(self, aNode):
        self.head = aNode

    def setTail(self, aNode):
        self.tail = aNode

    def insertLast(self, data):

        newNode = Node(data, None, None)

        if self.isEmpty():
            self.setHead(newNode)
            self.setTail(newNode)
        else:
            newNode.setPrevious(self.tail)
            self.getTail().setNext(newNode)
            self.setTail(newNode)

        self.size += 1

    def insertFirst(self, data):

        newNode = Node(data, None, None)

        if self.isEmpty():
            self.setHead(newNode)
            self.setTail(newNode)
        else:
            newNode.setNext(self.head)
            self.getHead().setPrevious(newNode)
            self.setHead(newNode)
        self.size += 1

    def deleteLast(self):

        if self.isEmpty() is not True:
            self.getTail().getPrevious().setNext(None)
            self.getTail().setPrevious(None)
            self.setTail(self.getTail().getPrevious())
            self.size -= 1

    def deleteFirst(self):

        if self.isEmpty() is not True:
            self.setHead(self.getHead().getNext())
            self.getHead().setPrevious(None)
            self.size -= 1

    def getContent(self):
        result = []
        temp = self.getHead()

        while temp:
            result.append(temp.getValue())
            temp = temp.getNext()

        print(result)

    # Finds the first occurance of the data and returns its index
    def find(self, data):
        index = 0
        temp = self.getHead()

        while temp:
            if temp.getValue() == data:
                return index

            index += 1
            temp = temp.getNext()

        return -1
