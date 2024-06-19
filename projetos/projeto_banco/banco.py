valor_conta = 0
saques_disponiveis = 3
conta_extrato = []
limite = 500

def extrato():
    global valor_conta
    global conta_extrato
    conta_operacoes = len(conta_extrato)
    print(f"Movimentações na conta: {conta_operacoes}")
    print("--EXTRATO--")
    if conta_operacoes > 0:
        for i in range(conta_operacoes):
            if(conta_extrato[i][0]=='deposito'):
                print(f"+R${conta_extrato[i][1]}")
            else:
                print(f"-R${conta_extrato[i][1]}")
        print("-----------")
        print(f"=R${valor_conta}")
    else:
        print("Sem operações realizadas")
        return 0
    return 0

def deposito(valor: float):
    global valor_conta
    global conta_extrato
    if (valor > 0.0):
        valor_conta += valor
        conta_extrato.append(['deposito', valor])
    else:
        print(f"Valor {valor:.2f} deve ser maior que 0")
        return 1
    
    return 0

def saque(valor: float):
    global valor_conta
    global conta_extrato
    global saques_disponiveis
    global limite
    if((saques_disponiveis > 0) and (valor > 0)):    
        if ((valor <= valor_conta) and (valor <= limite)):
            saques_disponiveis -= 1
            valor_conta -= valor
            conta_extrato.append(['saque', valor])
        else:
            print("Saldo na conta insuficiente ou valor limite excedido")
            return 1
    else:
        print("Sem saques diarios disponiveis ou valor invalido de saque")
        return 1
    
    return 0

text = """
d   deposito    permite realizar depositos
s   saque       permite sacar até 3 vezes 
                com no maximo 500R$ por saque
e   extrato     permite visualizar saldo e movimentações
q   sair        sai da operação
h   help        exibe opções disponiveis
"""    


while True:
    print("Que operação deseja realizar?")
    opção = input(text)

    if opção == 'd':
        print("Insira valor do deposito")
        valor = input()
        deposito(float(valor))
    elif opção == 's':
        print("Insira valor do saque")
        valor = input()
        saque(float(valor))
    elif opção == 'e':
        extrato()
    elif opção == 'h':
        print(text)
    elif opção == 'q':
        break
    else:
        print("operação invalida")
