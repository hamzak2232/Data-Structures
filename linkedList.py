class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The given previous node must in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def delete_node_at_position(self, position):
        if self.head is None:
            return
        current = self.head
        if position == 0:
            self.head = current.next
            current = None
            return
        for _ in range(position - 1):
            current = current.next
            if current is None:
                return
        if current.next is None:
            return
        next = current.next.next
        current.next = None
        current.next = next

    def find(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

linked_list = LinkedList()
linked_list.append('apple')
linked_list.append('banana')
linked_list.append('cherry')
linked_list.prepend('date')
linked_list.insert_after_node(linked_list.head.next, 'strawberry')
linked_list.print_list()

linked_list.delete_node('banana')
linked_list.print_list()

linked_list.delete_node_at_position(2)
linked_list.print_list()

print(linked_list.find('apple'))
print(linked_list.find('banana'))

linked_list.reverse()
linked_list.print_list()
