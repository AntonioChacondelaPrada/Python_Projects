user_prompt = "Enter a to-do:"
todos = []

while True:
    todo = input(user_prompt)
    todo = todo.title()
    todos.append(todo)
    print(todos)
