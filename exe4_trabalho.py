#Inicio da função cadastrarPeca
def cadastrarPeca(contador):
    peca = {}
    peca["Codigo"] = contador
    peca["Nome"] = input("Por favor entre com o nome da peça: ")
    peca["Fabricante"] = input("Por favor entre com o fabricante da peça: ")
    peca["Valor"] = float(input("Por favor entre com o  o valor (R$) da peça: "))

    return peca #retornar peca

#Inicio da função consultarPeca
def consultarPeca(pecas):
    while True: #Laço infinito
        print("Consultar Peças:")
        print("1) Consultar Todas as Peças")
        print("2) Consultar Peças por Código")
        print("3) Consultar Peças por Fabricante")
        print("4) Retornar")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("\nTodas as Peças:")
            for codigo, peca in pecas.items():
                print("Código:", codigo)
                print("Nome:", peca["Nome"])
                print("Fabricante:", peca["Fabricante"])
                print("Valor:", peca["Valor"])
                print("------")
        elif opcao == "2":
            codigo = input("Digite o código da peça: ")
            if codigo in pecas:
                peca = pecas[codigo]
                print("\nPeça encontrada:")
                print("Código:", codigo)
                print("Nome:", peca["Nome"])
                print("Fabricante:", peca["Fabricante"])
                print("Valor:", peca["Valor"])
            else:
                print("Código não encontrado.")
        elif opcao == "3":
            fabricante = input("Digite o fabricante da peça: ")
            print("\nPeças do Fabricante", fabricante)
            for codigo, peca in pecas.items():
                if peca["Fabricante"] == fabricante:
                    print("Código:", codigo)
                    print("Nome:", peca["Nome"])
                    print("Valor:", peca["Valor"])
                    print("------")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Digite um valor válido.")

#Inicio da função removerPeca
def removerPeca(pecas):
    codigo = input("Digite o código da peça que deseja remover: ")
    if codigo in pecas:
        del pecas[codigo]
        print("Peça removida com sucesso.")
    else:
        print("Código não encontrado.")


pecas = {}
contador = 1

while True:
    print('Bem Vindo ao Controle de Estoque da Bicicletaria do Anderson Alves Santana')
    print("Escolha a opção desejada:")
    print("1. Cadastrar Peça")
    print("2. Consultar Peça")
    print("3. Remover Peça")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("Você selecionou a opção 1 - Cadastrar Peça")
        print('codigo da peça 0{}'.format(contador))
        peca = cadastrarPeca(contador)
        pecas[str(contador)] = peca
        contador += 1
        print("Peça cadastrada com sucesso.")
    elif opcao == "2":
        print("Você selecionou a opção 2 - Consultar Peça")
        consultarPeca(pecas)
    elif opcao == "3":
        print("Você selecionou a opção 3 - Remover Peça")
        removerPeca(pecas)
    elif opcao == "4":
        print("Você selecionou a opção 4 - Sair")
        break
    else:
        print("Opção inválida. Digite um valor válido.")

print("\nTodas as Peças Cadastradas:")
for codigo, peca in pecas.items():
    print("Código:", codigo)
    print("Nome:", peca["Nome"])
    print("Fabricante:", peca["Fabricante"])
    print("Valor:",peca["Valor"])

