produtos = []

print ("1 para adicionar produto")
print("2 para listar produtos")
print ("3 para remover produtos")
print ("4 para sair:")
print ("---------------------")

opcao = int(input())

if opcao == 1:
    produto_novo = input ("Escreva o que quer adicionar: ")
    produtos.append (produto_novo)