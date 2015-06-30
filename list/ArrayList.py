__author__ = 'elias'

class ArrayList(object):

    def __init__(self):
        self.size = 0
        self.capacity = 0
        self.array = []

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, newCapacity):
        temp = []
        for i in range(newCapacity):
            temp.append(None)

        for i in range(len(self.array)):
            temp[i] = self.array[i]

        self.array = temp
        self.capacity = newCapacity

    def replace(self, index, aValue):
        if index+1 <= self.capacity:
            temp = self.array[index]
            self.array[index] = aValue
            return temp

    def insert(self, index, aValue):
        if index+1 <= self.capacity:
            self.array.insert(index, aValue)
            self.capacity += 1
            self.size += 1

    def delete(self, index):
        if index+1 <= self.getCapacity():
            self.array.pop(index)
        self.capacity -=1
        self.size -= 1

    def get(self, index):
        if index+1 > self.getCapacity():
            self.setCapacity(index+1)
        return self.array[index]

    def getContent(self):
        result = []
        for i in range (len(self.array)):
            result.append(self.array[i])
        print (result)