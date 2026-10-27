from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Tracker API", version="1.0.0")

# Simple in-memory storage (data resets when the app restarts)
tasks = {}
next_id = 1


class TaskIn(BaseModel):
    title: str
    done: bool = False


@app.get("/")
def home():
    return {"message": "Welcome to Task Tracker API", "version": "1.0.0"}


@app.get("/health")
def health():
    # Kubernetes will call this to check if the app is alive
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    return list(tasks.values())


@app.post("/tasks", status_code=201)
def create_task(task: TaskIn):
    global next_id
    new_task = {"id": next_id, "title": task.title, "done": task.done}
    tasks[next_id] = new_task
    next_id += 1
    return new_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]