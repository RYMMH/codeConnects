class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__ (self, head):
        self.head = head

    def printList(self):
        var = self.head
        print(str(var.data))
        while(var.next is not None):
            var = var.next
            print(str(var.data))

variableThree = Node(3)
variableTwo = Node(2)
variableTwo.next = variableThree
variable = Node(1)
variable.next = variableTwo
var = LinkedLists(variable)
var.printList()