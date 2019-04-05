print('-----------------------------------')
print('|    SUPERMERCADOS BELLA DONNA    |')
print('-----------------------------------')
total = 0
while True:
        valor = float(input('Informe o valor do produto: R$'))
        if (valor > 0):
            total = total + valor
            continue
        else:
            break
print('-----------------------------------')
print('Tecle 1 para 5%')
print('Tecle 2 para 10%')
print('Tecle 3 para 15%')
print('Tecle 4 para 25%')
print('Tecle 5 para 30%')
print('Tecle 0 para Sair')
opcao = int(input('Escolha o desconto a ser aplicado: '))
print('-----------------------------------')
if (opcao == 1):
    totF = total - (total * (5/100))
    print('Total da compra: R${:.2f}\nValor com o desconto de 5%: R${:.2f}'.format(total,totF))
elif (opcao == 2):
    totF = total - (total * (10/100))
    print('Total da compra: R${:.2f}\nValor com o desconto de 10%: R${:.2f}'.format(total,totF))
elif (opcao == 3):
    totF = total - (total * (15/100))
    print('Total da compra: R${:.2f}\nValor com o desconto de 15%: R${:.2f}'.format(total,totF))
elif (opcao == 4):
    totF = total - (total * (25/100))
    print('Total da compra: R${:.2f}\nValor com o desconto de 25%: R${:.2f}'.format(total,totF))
elif (opcao == 5):
    totF = total - (total * (30/100))
    print('Total da compra: R${:.2f}\nValor com o desconto de 30%: R${:.2f}'.format(total,totF))
elif (opcao == 0):
    print('Cancelando operação...')
else:
    print('Opção inválida!!!\n')
print('-----------------')
print('-----------------------------------')
print('Tecle 1 para Dinheiro')
print('Tecle 2 para Cartão de Crédito')
print('Tecle 3 para Vale Alimentação')
print('Tecle 0 para Sair')
opcaoPag = int(input('Selecione o método de pagamento: '))
print('-----------------------------------')
print('-----------------')
if (opcaoPag == 1):
    valorRec = float(input('Informe o valor recebido: R$'))
    troco = valorRec - totF
    print ('Total da compra: R${:.2f}'.format(totF))
    print ('Troco: R${:.2f}\n'.format(troco))
elif (opcaoPag == 2):
    if (totF < 50):
        print ('Parcelamento sem juros\n')
        print ('Tecle 1 - 1x R${:.2f}'.format(totF))
        print ('Tecle 2 - 2x R${:.2f}'.format(totF/2))
        print ('Tecle 3 - 3x R${:.2f}'.format(totF/3))
        print ('Tecle 0 - Sair')
        opcaoParc = int(input('Selecione a parcelamento desejado: '))
        print('-----------------')
        if (opcaoParc == 1):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('1x R${:.2f} sem juros\n'.format(totF))
        elif (opcaoParc == 2):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('2x R${:.2f} sem juros\n'.format(totF/2))
        elif (opcaoParc == 3):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('3x R${:.2f} sem juros\n'.format(totF/3))
        elif (opcaoParc == 0):
            print ('Retornando a tela de método de pagamento...\n')
        else:
            print ('Opção de parcelamento inválido!\n')
    else:
        print ('Parcelamento sem juros')
        print ('Tecle 1 - 1x R${:.2f}'.format(totF))
        print ('Tecle 2 - 2x R${:.2f}'.format(totF/2))
        print ('Tecle 3 - 3x R${:.2f}'.format(totF/3))
        print ('Tecle 4 - 4x R${:.2f}'.format(totF/4))
        print ('Tecle 5 - 5x R${:.2f}'.format(totF/5))
        print ('Tecle 6 - 6x R${:.2f}'.format(totF/6))
        print ('Tecle 0 - Sair')
        opcaoParc = int(input('Selecione o parcelamento desejado: '))
        print('-----------------')
        if (opcaoParc == 1):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('1x R${:.2f} sem juros\n'.format(totF))
        elif (opcaoParc == 2):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('2x R${:.2f} sem juros\n'.format(totF/2))
        elif (opcaoParc == 3):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('3x R${:.2f} sem juros\n'.format(totF/3))
        elif (opcaoParc == 4):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('4x R${:.2f} sem juros\n'.format(totF/4))
        elif (opcaoParc == 5):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('5x R${:.2f} sem juros\n'.format(totF/5))
        elif (opcaoParc == 6):
            print ('Total da compra: R${:.2f}'.format(totF))
            print ('6x R${:.2f} sem juros\n'.format(totF/6))
        elif (opcaoParc == 0):
            print ('Retornando a tela de método de pagamento...\n')
        else:
            print ('Opção de parcelamento inválido!\n')
elif (opcaoPag == 3):
    saldoAtual = float(input('Informe o saldo atual do VA: R$'))
    if (saldoAtual < totF):
        print ('Saldo insuficiente!')
    saldoDisp = saldoAtual - totF
    print ('Total da compra: R${:.2f}'.format(totF))
    print ('Saldo disponivel no VA: R${:.2f}\n'.format(saldoDisp))
elif (opcaoPag == 0):
    print ('Retornando a tela de descontos...\n')
