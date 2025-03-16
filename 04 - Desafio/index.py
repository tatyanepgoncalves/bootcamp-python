from datetime import datetime


menu = """
[a] Cadastrar conta bancária
[c] Cadastrar usuário
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair
=> """

users = []
counts = []
value_deposit = []
account_statement = ""

account_limit = 5000
WITHDRAWAL_LIMIT = 3
TRANSACTIONS_LIMIT = 10
account_balance = 0
withdrawal_number = 0
transaction_count = 0
value_count = 0
extrat = value_deposit

mask_ptbr = "%d/%m/%Y às %H:%M"

def create_user():
  cpf = input("Informe o CPF (somente número): ")
  for user in users:
    if user["cpf"] == cpf:
      print("Usuário já cadastrado!")
      return
    
  name = input("Nome completo: ")
  date_of_birth = input("Data de nascimento (DD/MM/AAAA): ")

  users.append({"cpf": cpf, "Nome": name, "Data de Nascimento": date_of_birth})
  print("Usuário cadastrado com sucesso!")

def create_count():
  cpf = input("Informe o CPF do titular da conta: ")
  user = next((u for u in users if u["cpf"] == cpf), None)
  if not users:
    print("Usuário não encontrado! Realize o cadastro do usuário primeiro.")
  
  number_count = len(counts) + 1
  counts.append({"agencia": "0001", "número da conta": number_count, "usuário": user})
  print(f"Conta {number_count} cadastrada com sucesso para {user["name"]}!")


while True:
  option = input(menu)
  
  if transaction_count >= TRANSACTIONS_LIMIT:
      print("\nVocê atingiu o limite de 10 transações diárias. Tente novamente amanhã.\n")
      continue

  if option == "a":
    create_count()

  elif option == "c":
    create_user()

  elif option == "d":
    cpf = input("Informe o CPF do titular da conta: ")
    user = next((u for u in users if u["cpf"] == cpf), None)
    if not users:
      print("Usuário não encontrado! Realize o cadastro do usuário primeiro.")
    value = float(input("Digite o valor para o deposito: "))
    
    if value > 0:
      account_balance += value
      account_statement += f"Depósito de R$ {value:.2f} em {datetime.now().strftime(mask_ptbr)} na conta de {user} \n"


    else: 
      print("Erro na operação! Informe um valor válido.")
  
  elif option == "s":
    cpf = input("Informe o CPF do titular da conta: ")
    user = next((u for u in users if u["cpf"] == cpf), None)
    if not users:
      print("Usuário não encontrado! Realize o cadastro do usuário primeiro.")
    value = float(input("Digite o valor para saque: "))

    exceeded_balance = value > account_balance
    exceeded_limit = value > account_limit
    exceeded_withdrawal = withdrawal_number >= WITHDRAWAL_LIMIT

    if exceeded_balance:
      print("Erro na operação! Você não tem saldo suficiente.")

    elif exceeded_limit:
      print("Erro na operação! O valor do saque excede o limite.")
    
    elif exceeded_withdrawal:
      print("Erro na operação! Você já atingiu o limite de saques.")
    
    elif value > 0:
      account_balance -= value
      withdrawal_number += 1
      account_statement += f"Saque de R$ {value:.2f} em {datetime.now().strftime(mask_ptbr)} na conta de {user}.\n"
    
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