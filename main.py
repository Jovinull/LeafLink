import json
from rich.console import Console
from rich.table import Table

class Node:
    def __init__(self, is_leaf=False):
        self.keys = []  # Chaves do nó
        self.children = []  # Filhos (ou valores, no caso de folhas)
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
        self.order = order  # Ordem da árvore

    def insert(self, key, value):
        # Insere uma chave-valor na árvore
        root = self.root
        if len(root.keys) == self.order - 1:
            # Divisão da raiz se estiver cheia
            new_root = Node()
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def _split_child(self, parent, index):
        # Divide um nó filho cheio
        full_child = parent.children[index]
        mid_index = len(full_child.keys) // 2
        mid_key = full_child.keys[mid_index]

        # Cria um novo nó
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
            # Insere diretamente em uma folha
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            node.keys.insert(i, key)
            node.children.insert(i, value)
        else:
            # Encontra o filho correto para inserção
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if len(node.children[i].keys) == self.order - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key, value)

    def search(self, key):
        # Procura uma chave na árvore
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

    def display(self):
        console = Console()
        table = Table(title="B+ Tree Structure", show_lines=True)
        table.add_column("Level", justify="center")
        table.add_column("Keys", justify="center")

        def traverse(node, level):
            if node:
                table.add_row(str(level), ", ".join(map(str, node.keys)))
                if not node.is_leaf:
                    for child in node.children:
                        traverse(child, level + 1)

        traverse(self.root, 0)
        console.print(table)

# Demonstração
if __name__ == "__main__":
    # Criação da árvore com ordem 4
    bpt = BPlusTree(order=4)

    # Inserção de dados fictícios
    data = [
        (1, "Produto A"),
        (3, "Produto B"),
        (7, "Produto C"),
        (10, "Produto D"),
        (15, "Produto E"),
    ]

    for key, value in data:
        bpt.insert(key, value)

    # Salva a árvore em um arquivo JSON
    bpt.save_to_file("bplustree.json")

    # Carrega a árvore do arquivo JSON
    loaded_tree = BPlusTree.load_from_file("bplustree.json")

    # Teste de busca
    print(loaded_tree.search(7))  # Deve retornar "Produto C"
    print(loaded_tree.search(4))  # Deve retornar None

    # Exibição da estrutura da árvore
    loaded_tree.display()
