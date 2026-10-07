import banco_de_dados
import sqlite3
from entradas import ler_inteiro, ler_decimal

db = sqlite3.connect("controle_de_estoque.db")

cursor = db.cursor()

def cadastrar_produto():

    cursor = db.cursor()

    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    # minimo=0: preço e quantidades negativas não fazem sentido
    valor = ler_decimal("Valor: ", minimo=0)
    quantidade = ler_inteiro("Quantidade: ", minimo=0)
    estoque_minimo = ler_inteiro("Estoque mínimo: ", minimo=0)

    cursor.execute(""" INSERT INTO controle_de_estoque(
        produto, categoria, valor, quantidade, estoque_minimo)
        VALUES (?, ?, ?, ?, ?)
        """, (nome, categoria, valor, quantidade, estoque_minimo))

    db.commit()
    print("Produto cadastrado!")


def ver_estoque():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM controle_de_estoque")

    dados = cursor.fetchall()

    print("\nESTOQUE")
    print("-" * 50)

    if not dados:
        print("Nenhum produto cadastrado.")
        return

    for id_produto, produto, categoria, valor, quantidade, minimo in dados:
        print(f"[{id_produto}] {produto} ({categoria}) | R$ {valor:.2f} | "
              f"qtd: {quantidade} | mínimo: {minimo}")

