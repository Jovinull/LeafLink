# Gerenciador de Dados com Árvore B+

Um projeto em Python que implementa e interage com uma estrutura de dados **Árvore B+**. Este projeto oferece uma **Interface de Linha de Comando (CLI)** amigável para inserir, buscar e visualizar dados na Árvore B+. Também inclui suporte para salvar e carregar a estrutura em arquivos JSON, tornando-o ideal para fins educacionais e práticos.

---

## O que é uma Árvore B+?

A Árvore B+ é uma estrutura de dados balanceada amplamente utilizada em sistemas de banco de dados e sistemas de arquivos. Ela é uma extensão da Árvore B e possui as seguintes características:

1. **Balanceamento Automático**: A Árvore B+ mantém todas as folhas no mesmo nível, garantindo eficiência em buscas e operações de inserção e remoção.
2. **Eficiência**: É uma estrutura otimizada para leitura e escrita em disco, devido ao número mínimo de operações de I/O.
3. **Uso em Banco de Dados**: É frequentemente usada para implementar índices, permitindo buscas rápidas de dados.
4. **Separação de Dados**: Os nós internos armazenam apenas as chaves para navegação, enquanto os nós folha armazenam os dados reais.

---

## Benefícios da Implementação

- **Rápido Acesso**: Permite buscas e operações em tempo logarítmico.
- **Flexibilidade**: Suporte para grandes volumes de dados devido ao balanceamento dinâmico.
- **Persistência**: Permite salvar e carregar estruturas complexas em arquivos JSON.

---

## Funcionalidades

- **Implementação Completa da Árvore B+**:
  - Inserção e busca de pares chave-valor.
  - Divisão automática de nós para balanceamento.
- **Interface de Linha de Comando**:
  - Visualização da estrutura da árvore em diferentes níveis.
  - Menu interativo para realizar operações na árvore.
- **Serialização em JSON**:
  - Salve e recarregue a árvore em arquivos JSON.
- **Registro de Operações**:
  - Log de todas as inserções e buscas em arquivo de texto.
- **Visualização Dinâmica**:
  - Estrutura da árvore apresentada de forma legível com a biblioteca `rich`.

---

## Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Biblioteca `rich` para exibição da árvore e interação via CLI

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/arvore-bmais.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd arvore-bmais
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## Como Usar

Execute o arquivo `main.py` para iniciar a CLI:
```bash
python main.py
```

### Menu Interativo

1. **Inserir Dados**: Adicione pares chave-valor à árvore.
2. **Buscar Dados**: Busque por uma chave na árvore.
3. **Exibir Estrutura da Árvore**: Veja a estrutura hierárquica da árvore.
4. **Salvar Árvore em JSON**: Salve o estado atual da árvore em um arquivo JSON.
5. **Carregar Árvore de JSON**: Carregue uma árvore previamente salva.
6. **Sair**: Encerre o programa.

---

## Estrutura do Projeto

```
arvore-bmais/
├── main.py                  # Ponto de entrada do programa
├── modules/
│   ├── bplustree.py         # Implementação da Árvore B+
│   ├── interface.py         # Interface de Linha de Comando
├── requirements.txt         # Dependências do Python
└── README.md                # Documentação do projeto
```

### Principais Módulos

1. **`bplustree.py`**:
   - Contém a implementação das classes `BPlusTree` e `Node`.
   - Suporte para operações como inserção, busca, serialização e desserialização.

2. **`interface.py`**:
   - Implementa a interface CLI usando a biblioteca `rich`.
   - Facilita a interação do usuário com a Árvore B+.

3. **`main.py`**:
   - Inicializa a CLI.

---

## Operações na Árvore

### Inserir Dados
- Adiciona um par chave-valor à Árvore B+.
- Balanceia a árvore automaticamente ao dividir nós cheios.

### Buscar Dados
- Localiza o valor associado a uma chave.
- Retorna `None` caso a chave não esteja presente.

### Salvar/Carregar
- Salve a estrutura completa da árvore em um arquivo JSON.
- Restaure o estado da árvore a partir de um arquivo JSON.

---

## Log de Operações

Todas as operações de inserção e busca são registradas em um arquivo chamado `bplustree_log.txt`. Os registros incluem:

- Inserções:
  ```plaintext
  Inserido chave=10, valor='Exemplo'
  ```
- Buscas:
  ```plaintext
  Buscado chave=15
  ```

---

## Visualização da Estrutura

A estrutura da árvore é exibida dinamicamente usando a biblioteca `rich`. Cada nível da árvore é mostrado com suas respectivas chaves.

Exemplo:
```
+-----------------------------+
|       Estrutura da Árvore B+|
+-------+---------------------+
| Nível | Chaves              |
+-------+---------------------+
|   0   | 10, 20              |
|   1   | 1, 5                |
|   1   | 15, 18              |
+-----------------------------+
```

---

## Licença

Este projeto está licenciado sob a Licença MIT LICENSE. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
