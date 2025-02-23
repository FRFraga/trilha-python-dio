def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace(",", "temp").replace(".", ",").replace("temp", ".")

saldo = 0.0
depositos = []
saques = []
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0

menu = """
======== MENU ========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
======================
"""

while True:
    print(menu)
    opcao = input("Escolha uma opção: ").strip().lower()
    
    if opcao == 'd':
        try:
            valor = float(input("Valor do depósito: "))
            if valor > 0:
                saldo += valor
                depositos.append(valor)
                print("Depósito realizado com sucesso!")
            else:
                print("Erro: O valor do depósito deve ser positivo.")
        except ValueError:
            print("Erro: Valor inválido. Digite um número.")
    
    elif opcao == 's':
        try:
            if numero_saques >= LIMITE_SAQUES:
                print("Erro: Limite diário de 3 saques atingido.")
                continue
            
            valor = float(input("Valor do saque: "))
            
            if valor > LIMITE_VALOR_SAQUE:
                print(f"Erro: Valor máximo por saque é {formatar_valor(LIMITE_VALOR_SAQUE)}.")
            elif valor > saldo:
                print("Erro: Saldo insuficiente para realizar o saque.")
            elif valor <= 0:
                print("Erro: Valor do saque deve ser positivo.")
            else:
                saldo -= valor
                saques.append(valor)
                numero_saques += 1
                print("Saque realizado com sucesso!")
        
        except ValueError:
            print("Erro: Valor inválido. Digite um número.")
    
    elif opcao == 'e':
        print("\n======== EXTRATO ========")
        if not depositos and not saques:
            print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES.")
        else:
            for deposito in depositos:
                print(f"Depósito: {formatar_valor(deposito)}")
            for saque in saques:
                print(f"Saque: {formatar_valor(saque)}")
        print(f"\nSaldo atual: {formatar_valor(saldo)}")
        print("========================")
    
    elif opcao == 'q':
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
