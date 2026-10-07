import banco_de_dados
import sqlite3
from entradas import ler_inteiro

db = sqlite3.connect('controle_de_estoque.db')

def entrada_produto():
    
    cursor = db.cursor()

    produto_id = ler_inteiro("ID do produto: ")
    # minimo=1: uma entrada negativa funcionaria como uma saída escondida
    quantidade = ler_inteiro("Quantidade entrada: ", minimo=1)
    motivo = input("Motivo: ")

    cursor.execute(""" UPDATE controle_de_estoque
        SET quantidade = quantidade + ?
        WHERE id = ?
        """, (quantidade, produto_id))

    # rowcount diz quantas linhas o UPDATE alterou.
    # 0 = o ID não existe, então não registramos a movimentação.
    if cursor.rowcount == 0:
        print("Produto não encontrado")
        return

    cursor.execute(""" INSERT INTO movimentacoes
        (produto_id, tipo, motivo, quantidade)
        VALUES (?, ?, ?, ?)
        """, (produto_id, "entrada", motivo, quantidade))

    db.commit()
    print("Entrada realizada!")


def saida_produto():

    cursor = db.cursor()

    produto_id = ler_inteiro("ID do produto: ")
    # minimo=1: uma saída de -50 somaria 50 ao estoque
    quantidade = ler_inteiro("Quantidade saída: ", minimo=1)
    motivo = input("Motivo: ")

    cursor.execute(""" SELECT quantidade
        FROM controle_de_estoque
        WHERE id = ?
        """, (produto_id,))

    resultado = cursor.fetchone()

    if resultado is None:
        print("Produto não encontrado")
        return

    estoque_atual = resultado[0]

    if quantidade > estoque_atual:
        print("Estoque insuficiente")
        return

    cursor.execute("""UPDATE controle_de_estoque
        SET quantidade = quantidade - ?
        WHERE id = ?
    """, (quantidade, produto_id))

    cursor.execute("""INSERT INTO movimentacoes
    (produto_id, tipo, motivo, quantidade)
    VALUES (?, ?, ?, ?)
    """, (produto_id, "saida", motivo, quantidade))

    db.commit()

    print("Saída realizada!")