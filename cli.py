#from function import get_todos,write_todos
import function
import time    

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It Is" , now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    ### add
    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = function.get_todos()
        
        todos.append(todo + '\n')
        
        function.write_todos(todos)
        
    ### show
    elif user_action.startswith('show'):
        
        todos = function.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    ### edit        
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
                
            number = number -1
                
            todos = function.get_todos()

                    
                    
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + "\n"
            
                
            function.write_todos("todos.txt",todos)
        except ValueError:
            print("Your command is not valid.")
            continue       
            
    ### complete
    elif user_action.startswith("complate"):
        number = int(user_action[9:])
        
        todos = function.get_todos()
        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index) 
        
        function.write_todos(todos)
            
        message = f'Todo {todo_to_remove} was removed from the list.' 
        print(message)
        
     ### exit    
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
        
print("Bye")        

