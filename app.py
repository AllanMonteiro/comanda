import tkinter as tk
from tkinter import messagebox

class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Comanda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, codigo_produto):
        # Implemente a lógica para remover um produto da comanda
        pass

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total

def gerar_relatorio(comanda):
    # Implemente a lógica para gerar o relatório em PDF
    pass

def adicionar_produto():
    # Implemente a lógica para adicionar um produto à comanda
    pass

def finalizar_comanda():
    # Implemente a lógica para finalizar a comanda e gerar o relatório
    pass

def criar_interface():
    root = tk.Tk()
    root.title("Controle de Comandas")

    label_cliente = tk.Label(root, text="Nome do Cliente:")
    label_cliente.grid(row=0, column=0)

    entry_cliente = tk.Entry(root)
    entry_cliente.grid(row=0, column=1)

    label_produto = tk.Label(root, text="Produto:")
    label_produto.grid(row=1, column=0)

    entry_produto = tk.Entry(root)
    entry_produto.grid(row=1, column=1)

    label_preco = tk.Label(root, text="Preço:")
    label_preco.grid(row=1, column=2)

    entry_preco = tk.Entry(root)
    entry_preco.grid(row=1, column=3)

    button_adicionar = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
    button_adicionar.grid(row=2, column=0, columnspan=2)

    button_finalizar = tk.Button(root, text="Finalizar Comanda", command=finalizar_comanda)
    button_finalizar.grid(row=2, column=2, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()































































        





























































































































































































































#Implementar funções para adicionar, editar, listar e excluir clientes.