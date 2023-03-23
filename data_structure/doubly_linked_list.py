class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next

    def print_list_reverse(self):
        tmp = self.tail
        while tmp:
            print(tmp.value)
            tmp = tmp.prev

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.tail
            self.tail = new_node
            self.tail.prev = tmp
            tmp.next = self.tail
        self.length += 1

    def pop(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            tmp = self.tail.prev
            self.tail = tmp
            self.tail.prev = tmp.prev
            self.tail.next = None
        self.length -= 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.head
            tmp.prev = new_node
            new_node.next = tmp
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            tmp = self.head
            self.head = tmp.next
            self.head.prev = None
            tmp.next = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return
        tmp = self.head
        if index < self.length/2:
            for _ in range(index):
                tmp = tmp.next
        else:
            tmp = self.tail
            for _ in range(self.length - 1, index, -1):
                tmp = tmp.prev
        return tmp

    def set_value(self, index, value):
        tmp = self.get(index)
        if tmp:
            tmp.value = value

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        tmp = self.get(index)
        before = tmp.prev
        after = tmp.next
        before.next = after
        after.prev = before
        tmp.next = None
        tmp.prev = None
        self.length -= 1
