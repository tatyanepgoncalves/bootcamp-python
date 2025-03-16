# '''
# Para ler e escrever dados em Python, utilizamos as seguintes funções:
# - input: lê UMA linha com dado(s) de Entrada do usuário;
# - print: imprime um texto de Saída (Output), pulando linha.
# '''

# def calcular_saldo(transacoes):
#     saldo = 0

#     for transacao in transacoes:
#         saldo += transacao

#     return f"R$ {saldo:.2f}".replace(".", ",")


# entrada_usuario = input("Digite os valores separados por vírgula: ")

# entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

# transacoes = [float(valor) for valor in entrada_usuario.split(",")]


# resultado = calcular_saldo(transacoes)

# print("Saldo: ", resultado)


