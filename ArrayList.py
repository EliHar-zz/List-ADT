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

    def insert(self, index, aValue):
        if index+1 > self.capacity:
            self.setCapacity((index+1)*2)
            self.array[index] = aValue
        else:
            temp = []
            for i in range(index):
                temp.append(self.array[i])

            temp.append(aValue)

            for i in range(index,self.capacity):
                temp.append(self.array[i])

            self.array = temp
            self.capacity += 1

        self.size += 1


    def delete(self, index):
        if index <= self.capacity:
            temp = []
            for i in range(index):
                temp.append(self.array[i])

            for i in range(index+1,self.capacity):
                temp.append(self.array[i])

            self.array = temp
            self.capacity -= 1

        self.size -= 1

    def get(self, index):
        if index+1 > self.capacity:
            self.setCapacity(index*2)
        return self.array[index]


    def getContent(self):
        result = []
        for i in range (len(self.array)):
            if self.array[i] is not None:
                result.append(self.array[i])
        print (result)