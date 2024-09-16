# Define o dicionário para armazenar os itens do estoque
estoque = {}


def adicionar_item():
    """Adiciona um novo item ao estoque."""
    nome = input('Informe o nome do item: ')
    quantidade = int(input('Informe a quantidade: '))
    preco = float(input('Informe o preço unitário: '))

    if nome in estoque:
        estoque[nome]['quantidade'] += quantidade
        print(f"{quantidade} unidades adicionadas ao item existente '{nome}'.")
    else:
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f"Item '{nome}' adicionado ao estoque.")


def remover_item():
    """Remove um item do estoque."""
    nome = input('Informe o nome do item a ser removido: ')

    if nome in estoque:
        del estoque[nome]
        print(f"Item '{nome}' removido do estoque.")
    else:
        print(f"Item '{nome}' não encontrado no estoque.")


def atualizar_item():
    """Atualiza a quantidade e o preço de um item."""
    nome = input('Informe o nome do item a ser atualizado: ')

    if nome in estoque:
        quantidade = int(input('Informe a nova quantidade: '))
        preco = float(input('Informe o novo preço unitário: '))
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f"Item '{nome}' atualizado.")
    else:
        print(f"Item '{nome}' não encontrado no estoque.")


def listar_estoque():
    """Lista todos os itens no estoque."""
    if estoque:
        print('\nEstoque Atual:')
        for nome, info in estoque.items():
            print(f"Item: {nome} | Quantidade: {info['quantidade']} | Preço: R${info['preco']:.2f}")
    else:
        print('Estoque vazio.')


def menu():
    """Exibe o menu de opções."""
    print("\n--- Aplicativo de Estoque ---")
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Atualizar Item")
    print("4. Listar Estoque")
    print("5. Sair")


while True:
    menu()
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        adicionar_item()
    elif escolha == '2':
        remover_item()
    elif escolha == '3':
        atualizar_item()
    elif escolha == '4':
        listar_estoque()
    elif escolha == '5':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.')
1