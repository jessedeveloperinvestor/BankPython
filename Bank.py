def menu():
    menu = """

    [1] Depósito
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [7] Finalizar Operação
    -> """
    return input(menu)

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('Operação falhou! Tente novamente.')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Operação falhou! Saldo insuficiente.')
    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite.')
    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print('Operação falhou! Tente novamente.')  

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n================ Extrato ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}') 
    print('=========================================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario: 
        print('CPF já cadastrado')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (longadouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário cadastrado com sucesso!')

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuário não encontrado. Criação de conta encerrada!')

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Angência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
         """
        
        print('=' * 100)
        print(linha)

def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == '1':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar (
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUE,
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios) 

            if conta:
                contas.append(conta)
            
        elif opcao == '5':
            listar_contas(contas)
        
        elif opcao == '6':
            criar_usuario(usuarios)

        elif opcao == '7':
            break
        else: 
            print('Operação inválida, por favor selecione novamente a operação desejada.')

main()
