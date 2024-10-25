class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append (self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
            
        last = self.head is None
        while last.next:
            last = last.next

        last.next = new_node

    def search(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        return current
    
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

llist = LinkedList()

llist.append(10)
llist.append(20)
llist.append(30)

llist.printlist