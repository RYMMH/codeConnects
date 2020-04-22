class GregStack():

    def __init__(self):
        self.list = []

    def push(self,data):
        self.list.append(data)
    
    def peek(self):
        return self.list[len(self.list)-1]

    def pop(self):
        item = self.list.pop(len(self.list)-1)
        return item

stk = GregStack()
stk.push("HI")
stk.push("Oh")
print(stk.peek())
print(stk.pop())
print(stk.pop())

class GregQueue():
    def __init__(self):
        self.list = []

    def enque(self, data):
        self.list.insert(0, data)

    def dequeue(self):
        item = self.list.pop(len(self.list)-1)
        return item
    
q = GregQueue()
q.enque("1")
q.enque("2")
print(q.dequeue())
print(q.dequeue())

def string_times(str, n):
  x = 0
  end = ""
  
  while x < n:
    end = end+str
    x = x + 1
    print(end)
    
  return str

string_times("hi", 4)