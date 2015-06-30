__author__ = 'Elias Haroun'

class Node(object):

    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setValue(self, aValue):
        self.value = aValue

    def setNext(self, aNode):
        self.next = aNode

    def setPrevious(self, aNode):
        self.previous = aNode

