from database import produtos, categorias
from lib.funcoes import menu, cadastrar_produtos, consultar_produtos, delete_produtos, atualizar_produtos, cadastrar_categorias, atualizar_categorias, lista_categorias 


while True:
        menu()
        op = int(input("Digite a opção: "))
        if op == 1:
            cadastrar_produtos(produtos)
        elif op == 2:
            consultar_produtos(produtos)
        elif op == 3:
            delete_produtos(produtos)
        elif op == 4:
            atualizar_produtos(produtos)
        elif op == 5:
            cadastrar_categorias(categorias)
        elif op == 6:
            atualizar_categorias(categorias)
        elif op == 7:
            lista_categorias(categorias)
        elif op == 8:
             break
        else:
             print("Digite algo válido")