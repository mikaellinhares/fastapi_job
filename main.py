from fastapi import FastAPI
from job import scheduler

app = FastAPI()
# uvicorn main:app
# uvicorn main:app --reload


scheduler.start()


@app.post('/')
def post():
    from task import contador
    return f'Contador está em {contador}'
