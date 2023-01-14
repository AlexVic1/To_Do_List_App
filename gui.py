import function
import PySimpleGUI
import time
import os 

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass
    
PySimpleGUI.theme("DarkPurple4")

clock = PySimpleGUI.Text('', key="clock")
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=function.get_todos(), key='todos',
                               enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[clock],
                                    [label],
                                    [input_box, add_button],
                                    [list_box, edit_button, complete_button],
                                    [exit_button]],
                            font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].Update(values=todos)
            
        case "Edit":
            try:
               todo_to_edit = values['todos'][0]
               new_todo = values['todo']
            
               todos = function.get_todos()
               index = todos.index(todo_to_edit)
               todos[index] = new_todo
               function.write_todos(todos)
               window['todos'].Update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Please select an item first.", font=("Helvetica", 10))   
        
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos) 
                window['todos'].Update(values=todos)
                window['todo'].Update(value='')
            except IndexError:
                PySimpleGUI.popup("Please select an item first.", font=("Helvetica", 10))        
                
        
        case "Exit":
            break
            
        case 'todos':
            window['todo'].Update(value=values['todos'][0])    
               
        case PySimpleGUI.WIN_CLOSED:
            break  
    
window.close()


