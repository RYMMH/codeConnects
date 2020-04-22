class RyanList:
    def __init__ (self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def peek(self):
        num = len(self.data)
        num -= 1
        return(self.data[num])

    def pop(self):
        result = self.data.pop()
        return(result)
class  RyanQueue:
    def __init__ (self):
        self.data = []

    def push(self, data):
        self.data.insert(0, data)

    def pop(self):
        result = self.data.pop()
        return(result)

    def __str__ (self):
        return(str(self.data)) 

dataOne = RyanList()
dataOne.push(1)
dataOne.push(2)
dataOne.push(3)
print(dataOne.peek())
print(dataOne.pop())
print(dataOne.pop())
dataTwo = RyanQueue()
dataTwo.push(1)
dataTwo.push(2)
dataTwo.push(3)
print(dataTwo)
print(dataTwo.pop())