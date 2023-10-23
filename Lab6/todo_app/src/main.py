from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def first_func():
    return {"message": "Hello, World"}

@app.get("/items/{item}")
def read_item(item: int):
    return {"item_id": item}

@app.get("/items/")
def read_item_with_query_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items/{item_id}/details")
def read_item_details(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: dict):
    return item 

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)