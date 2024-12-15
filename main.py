class Node:
    def __init__(self, is_leaf=False):
        self.keys = []  # Chaves do nó
        self.children = []  # Filhos (ou valores, no caso de folhas)
        self.is_leaf = is_leaf

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

    # Teste de busca
    print(bpt.search(7))  # Deve retornar "Produto C"
    print(bpt.search(4))  # Deve retornar None
