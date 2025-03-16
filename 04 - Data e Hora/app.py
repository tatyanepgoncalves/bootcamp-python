from datetime import datetime


menu = """
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair
=> """
# Capão, 00 - zona rural - Berilo/MG
# Dom Carloa - 55 - Bela Vista - Virgem da Lapa/MG
account_balance = 0
account_limit = 5000
account_statement = ""
withdrawal_number = 0
WITHDRAWAL_LIMIT = 3
transaction_count = 0
TRANSACTIONS_LIMIT = 10
value_count = 0
value_deposit = []
extrat = value_deposit

mask_ptbr = "%d/%m/%Y às %H:%M"

while True:
  option = input(menu)

  if transaction_count >= TRANSACTIONS_LIMIT:
    print("\nVocê atingiu o limite de 10 transações diárias. Tente novamente amanhã.\n")
    continue

  if option == "d":
    value = float(input("Digite o valor para o deposito: "))
    
    if value > 0:
      account_balance += value
      account_statement += f"Depósito de R$ {value:.2f} em {datetime.now().strftime(mask_ptbr)}\n"


    else: 
      print("Erro na operação! Informe um valor válido.")
  
  elif option == "s":
    value = float(input("Digite o valor para saque: "))

    exceeded_balance = value > account_balance
    exceeded_limit = value > account_limit
    exceeded_withdrawal = withdrawal_number >= WITHDRAWAL_LIMIT

    if exceeded_balance:
      print("Erro na operação! Você não tem saldo suficiente.")

    elif exceeded_limit:
      print("Erro na operação! O valor do saque excede o limite.")
    
    elif exceeded_limit:
      print("Erro na operação! Você já atingiu o limite de saques.")
    
    elif value > 0:
      account_balance -= value
      withdrawal_number += 1
      account_statement += f"Saque de R$ {value:.2f} em {datetime.now().strftime(mask_ptbr)}\n"
    
    else:
      print("Erro na operação! O valor informado é invalido.")

  elif option == "e":
    print("\n================ EXTRATO =================")
    print("Não foram realizadas movimentações." if not account_statement else account_statement)
    print(f"\nSaldo: R$ {account_balance:.2f}")
    print("================================")
  
  elif option == "q":
    break

  else: 
    print("Opção inválida, por favor selecione novamente a operação desejada.")