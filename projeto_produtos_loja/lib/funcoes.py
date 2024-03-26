from database import produtos, categorias

def menu():
    return print( """
    Menu
    1 - Cadastrar produtos
    2 - Consultar/listar produtos
    3 - Apagar produtos
    4 - Atualizar produtos
    5 - Cadastrar categorias
    6 - Atualizar categorias
    7 - Consultar/listar categorias
    8 - Sair
""")

def cadastrar_produtos(produtos):
    id = len(produtos) +1
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite o nome da categoria: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produtos.append(f"id: {id}, nome: {nome}, categoria: {categoria}, preço: {preco}, quantidade: {quantidade}")
    print(produtos)

def consultar_produtos(produtos):
    print(produtos)

def delete_produtos(produtos):
    id = int(input("Digite o ID que deseja deletar: "))
    for produto in produtos:
        if produto["id"] == id:
            indice =  id -14
            del produtos[indice]
        print(produtos)

def atualizar_produtos(produtos):
    id = int(input("Digite o ID que deseja atualizar: "))
    preco = int(input("Digite o novo preço: "))
    categoria = input("Digite a nov categoria: ")
    for obj in produtos:
        if obj["id"] == id:
            obj["preco"] = preco
            obj["categoria"] = categoria

        print(obj)

def cadastrar_categorias(categorias):
    id = len(categorias) +1
    descricao = input("Digite a descrição da nova categoria: ")
    categorias.append(f"id: {id}, descricao: {descricao}")
    print(categorias)
 
def atualizar_categorias(categorias):
    id = int(input("Digite o ID que deseja atualizar: "))
    descricao = input("Digite a nova descrição da categoria: ")
    for cat in categorias:
        if cat["id"] == id:
            cat["descricao"] = descricao

        print(cat)

def lista_categorias(categorias):
    print(categorias)
