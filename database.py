import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("veiculos.db")
    return conexao

conexao = conectar_banco()
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS marcas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    ativa BOOLEAN NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS veiculos (
    id INTEGER PRIMARY KEY,
    modelo TEXT NOT NULL,
    placa TEXT NOT NULL,
    quilometragem REAL NOT NULL,
    marca_id INTEGER NOT NULL,
    FOREIGN KEY (marca_id) REFERENCES marcas(id)
)
""")

conexao.commit()

print("Banco e tabelas criados!")