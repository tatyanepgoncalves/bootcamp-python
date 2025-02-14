# Depósito, saque e extrato

menu = """
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair
"""

account_balance = 0 # saldo
account_limit = 500 # limite
account_statement = "" # extrato
withdrawal_number = 0 # numero de saques
WITHDRAWAL_LIMIT = 3 # limite de saques

value_count = 0 # valor da conta
value_deposit = [] # valor do deposito
extrat = value_deposit

while True:
  option = input(menu)
  if option == 'd':
    value = float(input("Digite o valor para deposito: "))

    if value > 0:
      account_balance += value
      account_statement += f"Depósito de R$ {value:.2f}\n"

    else: 
      print("Operação falhou! O valor informado é invalido.")

  elif option == "s":
    value = float(input("Digite o valor para saque: "))

    exceeded_balance = value > account_balance
    exceeded_limit = value > account_limit
    exceeded_withdrawal = withdrawal_number >= WITHDRAWAL_LIMIT

    if exceeded_balance:
      print("Operação falhou! Você não tem saldo suficiente.")

    elif exceeded_limit:
      print("Operação falhou! O valor do saque excede o limite.")
    
    elif exceeded_limit:
      print("Operação falhou! Você já atingiu o limite de saques.")
    
    elif value > 0:
      account_balance -= value
      account_statement += f"Saque de R$ {value:.2f}\n"
      withdrawal_number += 1
    
    else:
      print("Operação falhou! O valor informado é invalido.")
  
  elif option == "e":
    print("\n================ EXTRATO =================")
    print("Não foram realizadas movimentações." if not account_statement else account_statement)
    print(f"\nSaldo: R$ {account_balance:.2f}")
    print("================================")
  
  elif option == "q":
    break

  else: 
    print("Opção inválida, por favor selecione novamente a operação desejada.")