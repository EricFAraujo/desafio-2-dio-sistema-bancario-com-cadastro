def exibir_menu():
    return """
    [1] Criar Cliente
    [2] Criar Conta Corrente e Vincular ao Cliente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente (somente números): ")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado (sigla): ")

    # Verificar se o CPF já existe em algum cliente
    while any(cliente["cpf"] == cpf for cliente in clientes):
        print("CPF já cadastrado. Digite um CPF diferente.")
        cpf = input("Digite o CPF do cliente (somente números): ")

    return {
        "nome": nome,
        "cpf": cpf,
        "endereco": {
            "logradouro": logradouro,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado
        },
        "conta_corrente": None
    }

def criar_conta_corrente(cliente):
    numero_conta = input("Digite o número da conta corrente: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    limite_conta = float(input("Digite o limite da conta: "))
    
    conta_corrente = {
        "numero": numero_conta,
        "saldo": saldo_inicial,
        "limite": limite_conta,
        "extrato": "",
        "numero_saques": 0,
    }
    
    cliente["conta_corrente"] = conta_corrente


clientes = []

while True:
    opcao = input(exibir_menu())

    if opcao == "1":
        novo_cliente = criar_cliente()
        clientes.append(novo_cliente)
        print("Cliente criado com sucesso!")

    elif opcao == "2":
        cpf_cliente = input("Digite o CPF do cliente para vincular a conta corrente: ")
        cliente_encontrado = None

        for cliente in clientes:
            if cliente["nome"] == cpf_cliente:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            criar_conta_corrente(cliente_encontrado)
            print("Conta corrente criada e vinculada com sucesso!")
        else:
            print("Cliente não encontrado.")

    # Restante do seu código para as operações de depósito, saque, extrato e sair
