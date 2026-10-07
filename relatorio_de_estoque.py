import banco_de_dados
import sqlite3
from entradas import ler_inteiro, ler_decimal, ler_data

db = sqlite3.connect("controle_de_estoque.db")

def ver_movimentacoes():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM movimentacoes")
    dados = cursor.fetchall()

    print("\nMOVIMENTAÇÕES")
    print("-" * 50)

    if not dados:
        print("Nenhuma movimentação registrada.")
        return

    for id_mov, produto_id, tipo, motivo, quantidade in dados:
        print(f"#{id_mov} | produto {produto_id} | {tipo} de {quantidade} | {motivo}")

def giro_estoque():
    
    print("\nGIRO DE ESTOQUE")

    cmv = ler_decimal("Digite o CMV: ", minimo=0)
    estoque_inicial = ler_decimal("Digite o estoque inicial: ", minimo=0)
    estoque_final = ler_decimal("Digite o estoque final: ", minimo=0)

    estoque_medio = (estoque_inicial + estoque_final) / 2

    if estoque_medio == 0:
        print("Não é possível dividir por zero")
        return

    giro = cmv / estoque_medio

    print(f"Giro de Estoque: {giro:.2f}")

def nivel_servico():

    print("\nNÍVEL DE SERVIÇO")

    pedidos_prazo = ler_inteiro("Pedidos entregues no prazo: ", minimo=0)
    total_pedidos = ler_inteiro("Total de pedidos: ", minimo=0)

    if total_pedidos == 0:
        print("Total de pedidos não pode ser zero")
        return

    # sem essa checagem, 12 no prazo de 10 pedidos daria 120%
    if pedidos_prazo > total_pedidos:
        print("Pedidos no prazo não podem passar do total")
        return

    nivel = (pedidos_prazo / total_pedidos) * 100

    print(f"Nível de serviço: {nivel:.2f}%")


def tempo_reposicao():

    print("\nTEMPO DE REPOSIÇÃO")

    # o formato era "%d/%m/%7" (erro de digitação), o que quebrava sempre.
    # O correto para ano com 4 dígitos é %Y; agora isso fica em ler_data.
    pedido = ler_data("Data do pedido (dd/mm/aaaa): ")
    recebimento = ler_data("Data do recebimento (dd/mm/aaaa): ")

    tempo = recebimento - pedido

    if tempo.days < 0:
        print("O recebimento não pode ser antes do pedido")
        return

    print(f"Tempo de reposição: {tempo.days} dias")

def custo_manutencao():

    print("\nCUSTO DE MANUTENÇÃO")

    capital = ler_decimal("Custo de capital: ", minimo=0)
    armazenamento = ler_decimal("Custo de armazenamento: ", minimo=0)
    obsolescencia = ler_decimal("Custo de obsolescência: ", minimo=0)
    seguro = ler_decimal("Custo de seguro: ", minimo=0)

    total = capital + armazenamento + obsolescencia + seguro

    print(f"Custo total de manutenção: R$ {total:.2f}")
