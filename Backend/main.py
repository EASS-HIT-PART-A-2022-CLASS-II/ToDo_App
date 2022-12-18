from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    task: str
    id: str
    completed: bool = False

todos = []

@app.get("/")
async def root():
  return {"message": "This will be the main window of the Notes APP!!"}


@app.get("/todos")
def read_todos() -> List[Todo]:
  return todos

@app.post("/todos")
def create_todo(todo: Todo):
  todos.append(todo)
  return todos

@app.put("/todos/{task_id}")
def update_todo(task_id: str, task: Todo):
  for t in todos:
      if t.id == task_id:
        t.task = task.task
        return t
  return {"error": "Task not found"}

@app.put("/todos/complete/{task_id}")
def complete_todo(task_id: str):
  for t in todos:
      if t.id == task_id:
        t.completed = True
        return t
  return {"error": "Task not found"}

@app.delete("/todos/{task_id}")
def delete_todo(task_id: str):
  for t in todos:
    if t.id == task_id:
      todos.remove(t)
      return {"success": "Task deleted"}
  return {"error": "Task not found"}