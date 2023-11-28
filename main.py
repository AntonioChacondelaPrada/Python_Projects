todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case "show" | 'display': #Bitwise OR operator
            for item in todos:
                item = item.capitalize()
                print(item)

        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("write the mew tasks: ")
            todos[number] = new_todo
            print(todos)

        case "exit":
            break
        case _:
            print("hey, you entered an unknown command")
print("bye")