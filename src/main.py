from fastapi import FastAPI, HTTPException

app = FastAPI()

# base de dartos falsa en memoria

productos = {
    1: {"id": 1, "nombre": "Laptop", "precio": 999.99},
    2: {"id": 2, "nombre": "Mouse", "precio": 29.99},
    3: {"id": 3, "nombre": "Teclado", "precio": 49.99},
}


@app.get("/")
def root():
    return {"mensaje":"API Funcionando"}


@app.get("/productos")
def obtener_productos():
    return list(productos.values())


@app.get("/productos/{id}")
def obtener_producto(id: int):
    if id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos[id]


@app.post("/productos")
def crear_producto(producto: dict):
    nuevo_id = max(productos.keys()) + 1
    productos[nuevo_id] = {"id": nuevo_id, **producto}
    return productos[nuevo_id]
