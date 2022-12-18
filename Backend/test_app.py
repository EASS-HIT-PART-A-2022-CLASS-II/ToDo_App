from main import Todo, create_todo, delete_todo, read_todos, todos, update_todo


def test_create_todo():
    todo = Todo(task="Finish homework", completed=False, id="1")
    create_todo(todo)
    assert todos == [todo]

def test_read_todos():
    todo1 = Todo(task="Finish homework", completed=False, id="1")
    todo2 = Todo(task="Do grocery shopping", completed=False, id="2")
    todos.extend([todo1, todo2])
    assert read_todos() == todos

def test_update_todo():
    todo = Todo(task="Finish homework", completed=True, id="1")
    create_todo(todo)
    todo.task = "Finish task"
    update_todo("1", todo)
    assert todos == [todo]

def test_delete_todo():
    todo = Todo(task="Finish homework", completed=True, id="1")
    create_todo(todo)
    delete_todo("1")
    assert todos == []
