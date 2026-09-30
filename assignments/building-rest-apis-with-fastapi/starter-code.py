from fastapi import FastAPI

app = FastAPI()

# Example in-memory storage
items = [
    {"id": 1, "title": "Learn FastAPI", "description": "Build a simple API"}
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add CRUD routes for /items
