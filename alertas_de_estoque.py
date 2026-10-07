import banco_de_dados
import sqlite3

db = sqlite3.connect("controle_de_estoque.db")

def verificar_alertas():

    cursor = db.cursor()

    cursor.execute(""" SELECT produto, quantidade, estoque_minimo
    FROM controle_de_estoque
    """)

    produtos = cursor.fetchall()
    alertas = 0

    for produto in produtos:

        nome = produto[0]
        quantidade = produto[1]
        minimo = produto[2]

        if quantidade <= minimo:
            print(f"ATENÇÃO: {nome} está com estoque baixo!")
            alertas += 1

    # sem essa mensagem, a tela ficava vazia e parecia que nada aconteceu
    if alertas == 0:
        print("Nenhum produto com estoque baixo.")

