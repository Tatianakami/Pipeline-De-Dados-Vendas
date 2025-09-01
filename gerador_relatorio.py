# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def criar_banco_e_tabela():
    """
    Cria um banco de dados SQLite e uma tabela de vendas.
    """
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()

    # Cria a tabela de vendas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY,
        produto TEXT NOT NULL,
        valor REAL NOT NULL,
        data_venda TEXT NOT NULL
    );
    """)

    # Insere alguns dados de exemplo
    dados = [
        ('Smartphone', 1500.00, '2025-08-28'),
        ('Tablet', 900.00, '2025-08-28'),
        ('Smartphone', 1500.00, '2025-08-29'),
        ('Smartwatch', 350.50, '2025-08-29'),
        ('Tablet', 900.00, '2025-08-30'),
        ('Smartphone', 1500.00, '2025-08-30'),
        ('Headphone', 250.00, '2025-08-31'),
        ('Tablet', 900.00, '2025-08-31'),
    ]

    cursor.executemany("INSERT INTO vendas (produto, valor, data_venda) VALUES (?, ?, ?)", dados)
    conn.commit()
    conn.close()

def gerar_relatorio_total_vendas():
    """
    Conecta-se ao banco de dados e gera um relatório de vendas diárias.
    """
    conn = sqlite3.connect('vendas.db')

    # Usa um comando SQL para somar os valores de venda por dia
    query = """
    SELECT
        data_venda,
        SUM(valor) as valor_total
    FROM vendas
    GROUP BY
        data_venda
    ORDER BY
        data_venda;
    """
    
    # Carrega os resultados da consulta para um DataFrame do pandas
    relatorio = pd.read_sql_query(query, conn)

    # Salva o relatório em um arquivo CSV
    relatorio.to_csv('relatorio_vendas.csv', index=False)
    
    print("Relatório gerado com sucesso!")
    print(relatorio)

    conn.close()
    return relatorio

def gerar_grafico_vendas_diarias(df_relatorio):
    """
    Gera um gráfico de barras a partir do DataFrame do relatório.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(df_relatorio['data_venda'], df_relatorio['valor_total'], color='skyblue')
    
    plt.title('Vendas Diárias', fontsize=16)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Valor Total', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('grafico_vendas.png')
    
    print("Gráfico de vendas gerado com sucesso!")

if __name__ == '__main__':
    criar_banco_e_tabela()
    df_relatorio = gerar_relatorio_total_vendas()
    gerar_grafico_vendas_diarias(df_relatorio)

