
#Cadastro de Clientes:
#Criar uma estrutura para armazenar os dados dos clientes (nome, telefone, endereço, etc.).
class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
#Cadastro de Produtos:
#Criar uma estrutura para armazenar os dados dos produtos (nome, preço, código, etc.).
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

#Implementar funções para adicionar, editar, listar e excluir produtos.

class Comanda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produtos(self, codigo_produto):
        self.produtos.remove(Produto)

    def calcular_total(self):
        total  = sum(produto.preco for produto in self.produtos)
        return total


def gerar_relatorio(comanda):
    pass



cliente1 = Cliente("João", "123456789", "Rua A, 123")
produto1 = Produto("001", "Cerveja", 5.0)
produto2 = Produto("002", "Refrigerante", 3.0)

comanda_joao = Comanda(cliente1)
comanda_joao.adicionar_produto(produto1)
comanda_joao.adicionar_produto(produto2)

total_comanda_joao = comanda_joao.calcular_total()
print("Total da comanda do João:", total_comanda_joao)

gerar_relatorio(comanda_joao)






























































        





























































































































































































































#Implementar funções para adicionar, editar, listar e excluir clientes.