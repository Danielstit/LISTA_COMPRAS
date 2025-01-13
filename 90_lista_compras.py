import os
decisão = ''
lista_decompras = []  
while True:
    
    try:
        decisão = int(input("\nEscolha uma das seguintes opções:\n[1]Adicionar\n[2]Remover\n[3]Ver lista\n"))
    except:
        print("Por favor, insira um valor válido!")
    if decisão == 1:
        produto = input("\nInforme o produto que deseja adicionar: \n")
        lista_decompras.append(produto) 
    elif decisão ==2:
        indice_remover = int(input("Informe o Índice que você deseja remover(o índice [0]) representa o primeiro produto: "))
        try:
            lista_decompras.pop(indice_remover)
        except:
            print("indice informado não existe!")
    elif decisão == 3: 
        print("lista de compras: \n")
        if len(lista_decompras)==0:
            print(f'lista de compras vazia')
        for indice, produto in enumerate(lista_decompras):
            print(indice,produto) 
