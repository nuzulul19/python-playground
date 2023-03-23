class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        tmp = self.root
        while True:
            if new_node.value == tmp.value:
                return
            if new_node.value > tmp.value:
                if not tmp.right:
                    tmp.right = new_node
                    return
                tmp = tmp.right
            if new_node.value < tmp.value:
                if not tmp.left:
                    tmp.left = new_node
                    return
                tmp = tmp.left

    def contains(self, value):
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def min_value_node(self, root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp

    def decodeHuff(root, s):
        tmp = root
        i = 0
        result = ""
        while i <= len(s):
            if i < len(s) and s[i] == "0" and tmp.left:
                tmp = tmp.left
                i += 1
            elif i < len(s) and s[i] == "1" and tmp.right:
                tmp = tmp.right
                i += 1
            else:
                result += tmp.data
                tmp = root
                if i == len(s):
                    i += 1

        print(result)

    def preOrder(self, root):
        p = root
        if p is None:
            return
        print(p.info, end=' ')
        self.preOrder(p.left)
        self.preOrder(p.right)
