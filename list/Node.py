__author__ = 'Elias Haroun'

class Node(object):

    def __init__(self, data, next, previous):
        self.data = data
        self.next = next
        self.previous = previous

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, data):
        self.data = data

    def setNext(self, aNode):
        self.next = aNode

    def setPrevious(self, aNode):
        self.previous = aNode

