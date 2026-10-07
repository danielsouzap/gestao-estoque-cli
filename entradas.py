from datetime import datetime

# Funções para ler valores do teclado sem derrubar o programa.
# int(input()) direto lança ValueError se o usuário digitar "abc",
# e o sistema inteiro fecha. Aqui o erro é tratado e a pergunta se repete.


def ler_inteiro(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")
            continue

        # minimo=None significa "qualquer valor serve"
        if minimo is not None and valor < minimo:
            print(f"O valor precisa ser no mínimo {minimo}.")
            continue

        return valor


def ler_decimal(mensagem, minimo=None):
    while True:
        try:
            # aceita vírgula, que é o jeito brasileiro de escrever 2,50
            valor = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um número (ex.: 12.50).")
            continue

        if minimo is not None and valor < minimo:
            print(f"O valor precisa ser no mínimo {minimo}.")
            continue

        return valor


def ler_data(mensagem):
    while True:
        texto = input(mensagem)
        try:
            return datetime.strptime(texto, "%d/%m/%Y")
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")
