### Read a text file and return the list of to-do list.
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

text = "\
Principles of productivity: \
Managin your inflow.\
Systemizing evrything that repeats.\
"
print(text)

### Write the to-do items list in the file
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

        
if __name__ == "__main__":
    print(get_todos())        