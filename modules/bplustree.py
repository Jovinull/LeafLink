import json

class Node:
    def __init__(self, is_leaf=False):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

    def to_dict(self):
        return {
            "keys": self.keys,
            "children": [
                child if self.is_leaf else child.to_dict() for child in self.children
            ],
            "is_leaf": self.is_leaf,
        }

    @staticmethod
    def from_dict(data):
        node = Node(is_leaf=data["is_leaf"])
        node.keys = data["keys"]
        node.children = (
            data["children"]
            if node.is_leaf
            else [Node.from_dict(child) for child in data["children"]]
        )
        return node

class BPlusTree:
    def __init__(self, order=3):
        self.root = Node(is_leaf=True)
        self.order = order

    def insert(self, key, value):
        root = self.root
        if len(root.keys) == self.order - 1:
            new_root = Node()
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def _split_child(self, parent, index):
        full_child = parent.children[index]
        mid_index = len(full_child.keys) // 2
        mid_key = full_child.keys[mid_index]

        new_child = Node(is_leaf=full_child.is_leaf)
        new_child.keys = full_child.keys[mid_index + 1:]
        full_child.keys = full_child.keys[:mid_index]

        if not full_child.is_leaf:
            new_child.children = full_child.children[mid_index + 1:]
            full_child.children = full_child.children[:mid_index + 1]

        parent.keys.insert(index, mid_key)
        parent.children.insert(index + 1, new_child)

    def _insert_non_full(self, node, key, value):
        if node.is_leaf:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            node.keys.insert(i, key)
            node.children.insert(i, value)
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if len(node.children[i].keys) == self.order - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, value)

    def search(self, key):
        node = self.root
        while True:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and key == node.keys[i]:
                return node.children[i] if node.is_leaf else None
            if node.is_leaf:
                return None
            node = node.children[i]

    def to_dict(self):
        return {
            "order": self.order,
            "root": self.root.to_dict(),
        }

    @staticmethod
    def from_dict(data):
        tree = BPlusTree(order=data["order"])
        tree.root = Node.from_dict(data["root"])
        return tree

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return BPlusTree.from_dict(data)

    def log_operations(self, operation, key=None, value=None):
        with open("bplustree_log.txt", "a") as log_file:
            if operation == "insert":
                log_file.write(f"Inserted key={key}, value={value}\n")
            elif operation == "search":
                log_file.write(f"Searched for key={key}\n")
