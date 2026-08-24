from fastapi import FastAPI

app = FastAPI()

items=[]

@app.get("/")
def inicio():
    return {"mensagem": "API de veículos funcionando!"}


@app.post("/items")
def create_item(item: str):
    items.append(item)

    return items
@app.post("/items/{item_id}")
def create_item(item_id: int)->str:
    items.items {item_id}

    return items