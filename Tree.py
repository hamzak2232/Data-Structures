class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insert(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert(current.right, new_node)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        elif data < current.data:
            return self._search(current.left, data)
        else:
            return self._search(current.right, data)

    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.data)
            self._inorder(current.right, result)
        return result

    def preorder(self):
        return self._preorder(self.root, [])

    def _preorder(self, current, result):
        if current:
            result.append(current.data)
            self._preorder(current.left, result)
            self._preorder(current.right, result)
        return result

    def postorder(self):
        return self._postorder(self.root, [])

    def _postorder(self, current, result):
        if current:
            self._postorder(current.left, result)
            self._postorder(current.right, result)
            result.append(current.data)
        return result

binary_tree = BinaryTree()
binary_tree.insert(10)
binary_tree.insert(5)
binary_tree.insert(15)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(12)
binary_tree.insert(18)

print("Inorder traversal:", binary_tree.inorder())
print("Preorder traversal:", binary_tree.preorder())
print("Postorder traversal:", binary_tree.postorder())

print("Search for 7:", binary_tree.search(7))
print("Search for 20:", binary_tree.search(20))
