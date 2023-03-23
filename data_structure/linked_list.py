class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return

    def pop(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.make_empty()
            return

        pop_value = self.tail
        tmp = self.head
        while tmp.next.next:
            tmp = tmp.next
        self.tail = tmp
        self.tail.next = None
        self.length -= 1
        return pop_value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return

    def pop_first(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.make_empty()
            return

        tmp = self.head
        self.head = tmp.next
        tmp.next = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp

    def set_value(self, index, value):
        tmp = self.get(index)
        if tmp:
            tmp.value = value

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.prepend(value)
            return
        if index == self.length - 1:
            self.append(value)
            return

        new_node = Node(value)
        prev = self.get(index - 1)
        tmp = self.get(index)
        prev.next = new_node
        new_node.next = tmp
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
            return
        if index == self.length - 1:
            self.pop()
            return

        prev = self.get(index - 1)
        tmp = self.get(index)
        prev.next = tmp.next
        tmp.next = None
        self.length -= 1

    def reverse(self):
        tmp = self.head
        self.head, self.tail = self.tail, self.head

        after = tmp.next
        prev = None
        while tmp:
            after = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = after
