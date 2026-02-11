import pandas as pd
import sqlite3
import os

# Caminhos baseados na sua estrutura
BASE_DIR = "05-analise-pandas-sql/data"
DB_PATH = os.path.join(BASE_DIR, "olist.db")

# Conecta ao banco (cria se não existir)
conn = sqlite3.connect(DB_PATH)

print("🚀 Iniciando a criação do banco de dados SQL...")

# Lista arquivos na pasta data
files = [f for f in os.listdir(BASE_DIR) if f.endswith('.csv')]

for file in files:
    # Nome da tabela limpo (ex: olist_customers_dataset.csv -> customers)
    table_name = file.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
    
    # Lendo o CSV e jogando para o SQL
    path_to_csv = os.path.join(BASE_DIR, file)
    df = pd.read_csv(path_to_csv)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    print(f"✅ Tabela '{table_name}' criada com sucesso!")

conn.close()
print(f"\n✨ Pronto! Seu banco de dados está em: {DB_PATH}")