saldo = 0
extrato = ""
limite = 500
lista_depositos = []
lista_saques = []
LIMITE_SAQUES = 3

while True:
    print("\nBem vindo ao Banco")
    print("[d]. Depósito")
    print("[s]. Saque")
    print("[e]. Extrato")
    print("[q]. Sair")

    opcao = input("Opção: ")

    if opcao == "d":
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            lista_depositos.append(deposito)
            print(f"Depósito de R${deposito} realizado com sucesso.")
        else:
            print("Digite um depósito válido.")
    elif opcao == "s":
        saque = float(input("Digite o valor do saque: "))
        if saque <= saldo and saque <= 500 and LIMITE_SAQUES <= 3:
            saldo -= saque
            lista_saques.append(saque)
            LIMITE_SAQUES +=1
            print(f"Saque de R${saque} realizado com sucesso.")
        elif saque > 500:
            print("Limite máximo de saque é R$500.")
        elif LIMITE_SAQUES == 3:
            print("O seu LIMITE de saques do dia foi atingindo.")
        else:
            print("Saldo insuficiente para realizar o saque.")
    elif opcao == "e":
        extrato = "\nExtrato da conta\n"
        for el in lista_depositos:
            extrato+= f"\nDeposito - R${el:.2f}"
        for ele in lista_saques:
            extrato+= f"\nSaque - R${ele:.2f}"
        print(extrato)
    elif opcao == "q":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")