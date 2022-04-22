
def menu():
    print('''[1]Abrir Conta
[2]Realizar Depósito
[3]Realizar Saque
[4]Aplicar Juros
[5]Simular Empréstimo
[6]Extrato
[7]Sair''')
    item = input('Escolha uma opção:')
    return item

def opcao_1():
    nome = input('Digite seu nome: ')
    return nome
def opcao_1_1():
    saldoInicial = float(input('Digite o valor inicial da conta:'))
    return saldoInicial
def opcao_2(saldoAtual):
    valorDeposito = float(input('Digite o valor a ser depositado:'))
    valorDeposito = valorDeposito + saldoAtual
    return valorDeposito

def opcao_3(saldoAtual):
    valorSaque = float(input('Digite o valor de saque:'))
    valorSaque = saldoAtual - valorSaque
    return valorSaque
def opcao_4(saldoAtual):
    taxaJuros = float(input('Informe a taxa de juros:'))
    saldoAtual = saldoAtual + saldoAtual * (taxaJuros / 100)
    print('Valor atualizado com juros:', saldoAtual)
    return saldoAtual
def opcao_5():
    valorEmprestimo = 0
    while valorEmprestimo <= 0:
            valorEmprestimo = float(input('Digite o valor do empréstimo:'))             
    return valorEmprestimo
def opcao_5_1():
    taxaJuros = 0
    while taxaJuros <= 0:
            taxaJuros = float(input('Digite o valor do juros de cada parcela do empréstimo:'))        
    return taxaJuros
def opcao_5_2():   
    quantidadeParcelas = 0
    while quantidadeParcelas <= 0:
            quantidadeParcelas = float(input('Digite o número de parcelas:'))
    return quantidadeParcelas
def opcao_5_3():
    valorParcela = valorEmprestimo / quantidadeParcelas
    valorParcelaComJuros = valorParcela + valorParcela * (taxaJuros / 100)
    return valorParcelaComJuros
def opcao_5_3_1():
    valorTotalParcelasComJuros = valorParcelaComJuros * quantidadeParcelas
    return valorTotalParcelasComJuros  
def opcao_5_4():
    quantidadeTotalJuros = valorTotalParcelasComJuros - valorEmprestimo
    return quantidadeTotalJuros
def opcao_6():
    return extrato
def opcao_7():
    sair = input('Sair')
    return sair
escolha = ''
while(escolha != '7'):
    escolha = menu()
    if escolha == '1':
        print(opcao_1())
        saldoAtual = opcao_1_1()
        print(saldoAtual)
    elif escolha == '2':
        saldoAtual = opcao_2(saldoAtual)
        print(saldoAtual)
    elif escolha == '3':
        saldoAtual = opcao_3(saldoAtual)
        print(saldoAtual)
    elif escolha == '4':
        saldoAtual = opcao_4(saldoAtual)
        print(saldoAtual)
    elif escolha == '5':
        valorEmprestimo = opcao_5()
        taxaJuros = opcao_5_1()
        quantidadeParcelas = opcao_5_2()
        valorParcela = opcao_5_3()
        valorParcelaComJuros = opcao_5_3() 
        valorTotalParcelasComJuros = opcao_5_3_1()
        quantidadeTotalJuros = opcao_5_4()
        print('Valor final de cada parcela do empréstimo com juros aplicado:', opcao_5_3())
        print('Valor total das parcelas com juros:', opcao_5_3_1())
        print('Valor total de juros a ser pago:', opcao_5_4())
    elif escolha == '6':
        extrato = opcao_6()
        print(extrato)   
    elif escolha == '7':
        opcao_7()
        print('Saindo...')
    else:
        print('Opção desconhecida!')