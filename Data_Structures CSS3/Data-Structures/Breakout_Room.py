class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def add(self, value):
        self.next = Node(value)


#Traverse to get the length and /2 
class LinkedList:
    
    def __init__(self):
        self.head = None

    def push(self, new_data)
        new