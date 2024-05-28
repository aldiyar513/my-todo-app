def get_todos(file_path='todos.txt'):
    with open(file_path, 'r') as file:
        todos = file.readlines()
        return todos


def write_todos(arg_todos, file_path='todos.txt'):
    with open(file_path, 'w') as file:
        file.writelines(arg_todos)
