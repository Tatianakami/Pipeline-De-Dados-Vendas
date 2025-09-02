# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, send_file
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__, template_folder='templates')

def criar_banco_e_tabela():
    conn = sqlite3.connect('vendas.db')  # CORRIGIDO
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY,
        produto TEXT NOT NULL,
        valor REAL NOT NULL,
        data_venda TEXT NOT NULL
    );
    """)

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

def gerar_grafico_vendas_diarias():
    conn = sqlite3.connect('vendas.db')  # CORRIGIDO
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
    df_relatorio = pd.read_sql_query(query, conn)
    conn.close()

    plt.figure(figsize=(10, 6))
    plt.bar(df_relatorio['data_venda'], df_relatorio['valor_total'], color='skyblue')
    
    plt.title('Vendas Diárias', fontsize=16)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Valor Total', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    grafico_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()
    
    return grafico_base64

@app.route('/')
def index():
    criar_banco_e_tabela()
    return render_template('index.html')

@app.route('/gerar')
def gerar_relatorio():
    try:
        grafico = gerar_grafico_vendas_diarias()
        return jsonify(status='success', grafico_url=f'data:image/png;base64,{grafico}')
    except Exception as e:
        return jsonify(status='error', message=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
