class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                current = None
                return
            current = current.next

    def delete_node_at_position(self, position):
        if self.head is None:
            return
        current = self.head
        for _ in range(position):
            current = current.next
            if current is None:
                return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        current = None

    def find(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next
        if prev:
            self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print('None')

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append('lamborghini')
doubly_linked_list.append('ferrari')
doubly_linked_list.append('bmw')
doubly_linked_list.prepend('mercedes')
doubly_linked_list.insert_after_node(doubly_linked_list.head.next, 'volkswagen')
doubly_linked_list.print_list()

doubly_linked_list.delete_node('ferrari')
doubly_linked_list.print_list()

doubly_linked_list.delete_node_at_position(2)
doubly_linked_list.print_list()

print(doubly_linked_list.find('lamborghini'))
print(doubly_linked_list.find('ferrari'))

doubly_linked_list.reverse()
doubly_linked_list.print_list()
