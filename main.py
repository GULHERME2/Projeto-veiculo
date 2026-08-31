

from fastapi import FastAPI,HTTPException

from models import Veiculo

from database import 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def pagina_inicial():
    return FileResponse("templates/index.html")



@app.post("/veiculos")
def cadastrar_veiculo(veiculo: Veiculo):

    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO veiculos
        (id, modelo, placa, quilometragem, marca_id)
        VALUES (?, ?, ?, ?, ?)
    """, (
        veiculo.id,
        veiculo.modelo,
        veiculo.placa,
        veiculo.quilometragem,
        veiculo.marca_id
    ))

    conexao.commit()

    return veiculo




 @app.get("/veiculos/{id}")
def listar_veiculo(id: int):

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM veiculos WHERE id = ?",
        (id,)
    )

    veiculo = cursor.fetchone()

    conexao.close()

    if veiculo is None:
        raise HTTPException(
            status_code=404,
            detail="Veículo não encontrado"
        )

    return veiculo



@app.put("/veiculos/{id}")
def atualizar_veiculo(id: int, veiculo_atualizado: Veiculo):

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE veiculos
        SET modelo = ?,
            placa = ?,
            quilometragem = ?,
            marca_id = ?
        WHERE id = ?
    """, (
        veiculo_atualizado.modelo,
        veiculo_atualizado.placa,
        veiculo_atualizado.quilometragem,
        veiculo_atualizado.marca_id,
        id
    ))

    conexao.commit()

    if cursor.rowcount == 0:
        conexao.close()
        raise HTTPException(
            status_code=404,
            detail="Veículo não encontrado"
        )

    conexao.close()

    return {
        "mensagem": "Veículo atualizado com sucesso!"
    }

@app.delete("/veiculos/{id}")
def deletar_veiculo(id: int):

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM veiculos WHERE id = ?",
        (id,)
    )

    conexao.commit()

    if cursor.rowcount == 0:
        conexao.close()

        raise HTTPException(
            status_code=404,
            detail="Veículo não encontrado"
        )

    conexao.close()

    return {
        "mensagem": "Veículo removido com sucesso!"
    }