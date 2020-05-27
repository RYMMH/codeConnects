class Node:
    def __init__ (self, data, nextNode):
        self.data = data
        if(nextNode is not None):
            self.next = nextNode
        else:
            self.next = None 