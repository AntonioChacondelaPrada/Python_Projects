todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case "show" | 'display': #Bitwise OR operator
            for item in todos:
                item = item.capitalize()
                print(item)
        case "exit":
            break
        case _:
            print("hey, you entered an unknown command")
print("bye")