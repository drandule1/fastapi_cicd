from fastapi import FastAPI

app = FastAPI()

#https://github.com/settings/tokens
@app.get("/")
def root():
    return {"message": "Hello from katya"}

@app.get("/alive")
def alive():
    return {"message": "Hello from alive"}


@app.get("/health")
def health():
    return {"message": "Hello from health "}

@app.get("/status")
def status():
    return {"message": "Hello from hell"}

