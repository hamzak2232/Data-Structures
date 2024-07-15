class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        if self.head:
            if self.head.data == key:
                if self.head.next == self.head:
                    self.head = None
                else:
                    current = self.head
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next
                return
            prev = None
            current = self.head
            while current.next != self.head:
                if current.data == key:
                    prev.next = current.next
                    return
                prev = current
                current = current.next
            if current.data == key:
                prev.next = self.head

    def find(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def print_list(self):
        if self.head:
            current = self.head
            while True:
                print(current.data, end=' -> ')
                current = current.next
                if current == self.head:
                    break
        print('None')

circular_linked_list = CircularLinkedList()
circular_linked_list.append('apple')
circular_linked_list.append('banana')
circular_linked_list.append('cherry')
circular_linked_list.prepend('date')
circular_linked_list.insert_after_node(circular_linked_list.head.next, 'elderberry')
circular_linked_list.print_list()

circular_linked_list.delete_node('banana')
circular_linked_list.print_list()

print(circular_linked_list.find('apple'))
print(circular_linked_list.find('banana'))
