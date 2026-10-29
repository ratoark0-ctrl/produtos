produtos = []

print ("1 para adicionar produto")
print ("2 para listar produtos")
print ("3 para remover produtos")
print ("4 para sair:")
print ("---------------------")

opcao = int(input('Escolha uma opção: '))

if opcao == 1:

    nome = (input("Digite o nome do novo produto: "))
    preco = int(input("Digite o preço do novo produto: "))

    produto_novo = {
        "nome": nome,
        "preço": preco 
    }

    produtos.append (produto_novo)

    print ("Produto adicionado com carinho, amor e sucesso !")
    print (produtos)