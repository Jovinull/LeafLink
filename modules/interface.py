from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from .bplustree import BPlusTree

class CommandLineInterface:
    def __init__(self):
        self.console = Console()
        self.tree = BPlusTree(order=4)

    def display_tree(self):
        table = Table(title="B+ Tree Structure", show_lines=True)
        table.add_column("Level", justify="center")
        table.add_column("Keys", justify="center")

        def traverse(node, level):
            if node:
                table.add_row(str(level), ", ".join(map(str, node.keys)))
                if not node.is_leaf:
                    for child in node.children:
                        traverse(child, level + 1)

        traverse(self.tree.root, 0)
        self.console.print(table)

    def run(self):
        self.console.print("[bold green]Bem-vindo ao Gerenciador de Dados com Árvore B+![/bold green]")

        while True:
            self.console.print("\n[bold yellow]Escolha uma opção:[/bold yellow]")
            self.console.print("1. Inserir dados")
            self.console.print("2. Buscar dados")
            self.console.print("3. Exibir estrutura da árvore")
            self.console.print("4. Salvar árvore em JSON")
            self.console.print("5. Carregar árvore de JSON")
            self.console.print("6. Sair")

            choice = Prompt.ask("Digite o número da opção desejada")

            if choice == "1":
                key = int(Prompt.ask("Digite a chave (número inteiro)"))
                value = Prompt.ask("Digite o valor")
                self.tree.insert(key, value)
                self.tree.log_operations("insert", key, value)
                self.console.print(f"[green]Chave {key} com valor '{value}' inseridos com sucesso![/green]")

            elif choice == "2":
                key = int(Prompt.ask("Digite a chave para buscar"))
                result = self.tree.search(key)
                self.tree.log_operations("search", key=key)
                if result:
                    self.console.print(f"[green]Valor encontrado: {result}[/green]")
                else:
                    self.console.print("[red]Chave não encontrada.[/red]")

            elif choice == "3":
                self.display_tree()

            elif choice == "4":
                filename = Prompt.ask("Digite o nome do arquivo JSON")
                self.tree.save_to_file(filename)
                self.console.print(f"[green]Árvore salva em '{filename}' com sucesso![/green]")

            elif choice == "5":
                filename = Prompt.ask("Digite o nome do arquivo JSON")
                try:
                    self.tree = BPlusTree.load_from_file(filename)
                    self.console.print(f"[green]Árvore carregada de '{filename}' com sucesso![/green]")
                except FileNotFoundError:
                    self.console.print(f"[red]Arquivo '{filename}' não encontrado.[/red]")

            elif choice == "6":
                self.console.print("[blue]Encerrando o programa. Até logo![/blue]")
                break

            else:
                self.console.print("[red]Opção inválida. Tente novamente.[/red]")
