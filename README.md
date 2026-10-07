# Gestão de Estoque CLI

Sistema de controle de estoque para pequenos negócios, em Python com SQLite: cadastra produtos, registra entradas e saídas, avisa quando um item chega ao estoque mínimo e calcula os principais indicadores de estoque.

## Demonstração

```
ESTOQUE
--------------------------------------------------
[1] Caneta azul (Papelaria) | R$ 2.50 | qtd: 5 | mínimo: 10
[2] Caderno 96 fls (Papelaria) | R$ 18.90 | qtd: 32 | mínimo: 5

ATENÇÃO: Caneta azul está com estoque baixo!

MOVIMENTAÇÕES
--------------------------------------------------
#1 | produto 1 | saida de 35 | Venda balcão
#2 | produto 2 | entrada de 20 | Compra fornecedor
```

## Tecnologias

- **Python 3** (só biblioteca padrão, sem dependências externas)
- **SQLite** (`sqlite3`) para guardar produtos e movimentações
- SQL: `CREATE TABLE`, `INSERT`, `UPDATE`, `SELECT` com parâmetros `?`

## Como instalar e rodar

Precisa de Python 3.8 ou superior.

```bash
git clone https://github.com/danielsouzap/gestao-estoque-cli.git
cd gestao-estoque-cli
python main.py
```

Na primeira execução o programa cria o arquivo `controle_de_estoque.db` com as tabelas. Esse arquivo fica fora do Git (`.gitignore`).

## Como usar

```
(1) - Cadastrar Produto       (6) - Ver Alertas
(2) - Ver Estoque             (7) - Ver Giro De Estoque
(3) - Entrada De Produto      (8) - Nível de Serviço
(4) - Saída De Produto        (9) - Tempo de Reposição
(5) - Ver Movimentações       (10) - Custo de Manutenção
(0) - Sair
```

Fluxo típico: cadastre um produto com estoque mínimo (1), registre vendas como saída (4) e compras como entrada (3). A opção 6 lista os produtos que chegaram ao mínimo.

**Indicadores (opções 7 a 10)**

| Indicador | Cálculo |
|---|---|
| Giro de estoque | `CMV ÷ ((estoque inicial + estoque final) ÷ 2)` |
| Nível de serviço | `pedidos no prazo ÷ total de pedidos × 100` |
| Tempo de reposição | dias entre a data do pedido e a do recebimento |
| Custo de manutenção | capital + armazenamento + obsolescência + seguro |

## Estrutura

```
main.py                   menu e roteamento das opções
banco_de_dados.py         cria as tabelas no SQLite
produtos.py               cadastro e listagem de produtos
movimentacao.py           entradas e saídas (atualiza o saldo e grava o histórico)
alertas_de_estoque.py     produtos no estoque mínimo ou abaixo
relatorio_de_estoque.py   movimentações e indicadores
entradas.py               leitura validada de números e datas
```

## Regras que o sistema garante

- Saída maior que o saldo é recusada ("Estoque insuficiente").
- Entrada e saída só aceitam quantidade positiva. Antes, uma saída de `-50` **somava** 50 ao estoque.
- Entrada para um ID que não existe é recusada, sem gravar movimentação.
- Texto digitado num campo numérico não derruba o programa: a pergunta se repete.
- As consultas usam parâmetros (`?`) em vez de montar o SQL com o texto digitado, o que evita SQL injection.

## O que aprendi / próximos passos

**Aprendi:** modelar duas tabelas relacionadas (`controle_de_estoque` e `movimentacoes`), usar `cursor.rowcount` para saber se um `UPDATE` encontrou o registro, e que validar a entrada do usuário faz parte da regra de negócio. Uma quantidade negativa passava despercebida e corrompia o saldo.

**Próximos passos:**
- `FOREIGN KEY` de `movimentacoes.produto_id` para `controle_de_estoque.id`
- Data em cada movimentação, para calcular o giro direto do histórico
- Testes automatizados com `unittest`

## Créditos

Projeto em grupo do 1º semestre de Ciência da Computação (UDF, 2026.1). O código Python foi desenvolvido por mim. [@j-alexsander](https://github.com/j-alexsander) e [@EmillyVicxtss](https://github.com/EmillyVicxtss) contribuíram com a documentação original.
---

Daniel Souza Passos · [GitHub](https://github.com/danielsouzap) · [LinkedIn](https://www.linkedin.com/in/daniel-souza-8b9279349)
