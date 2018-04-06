#from Christian Thompson via youtube
# Create GUI elements
import Tkinter
import random


#Create root window
root = Tkinter.Tk()

# Create functions

def add_task():
    pass

def print_num_tasks():
    pass

def search_tasks():
    pass

def delete_name_task():
    pass

def delete_num_task():
    pass

def sort_list_up():
    pass

def sort_list_down():
    pass

def print_rand_task():
    pass

def delete_all():
    pass

def show_menu():
    pass

def print_list():
    pass

def exit():
    pass



# Create title in root widget of GUI with white background
lbl_title = Tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.pack()

lbl_display = Tkinter.Label(root, text="", bg="white")
lbl_display.pack()

txt_input = Tkinter.Entry(root, width = 15)
txt_input.pack()

btn_add_task = Tkinter.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.pack()

btn_print_num_tasks = Tkinter.Button(root, text="Print Number of Tasks", fg="green", bg="white", command=print_num_tasks)
btn_print_num_tasks.pack()

btn_search_tasks = Tkinter.Button(root, text="Search Tasks", fg="green", bg="white", command=search_tasks)
btn_search_tasks.pack()

btn_delete_task_by_name = Tkinter.Button(root, text="Delete Task by Name", fg="green", bg="white", command=delete_name_task)
btn_delete_task_by_name.pack()

btn_delete_task_by_number = Tkinter.Button(root, text="Delete Task by Number", fg="green", bg="white", command=delete_num_task)
btn_delete_task_by_number.pack()

btn_sort_list_up = Tkinter.Button(root, text="Sort List Ascending", fg="green", bg="white", command=sort_list_up)
btn_sort_list_up.pack()

btn_sort_list_down = Tkinter.Button(root, text="Sort List Descending", fg="green", bg="white", command=sort_list_down)
btn_sort_list_down.pack()

btn_print_rand_task = Tkinter.Button(root, text="Print Random Task", fg="green", bg="white", command=print_rand_task)
btn_print_rand_task.pack()

btn_reset_list = Tkinter.Button(root, text="Reset Task List", fg="green", bg="white", command=delete_all)
btn_reset_list.pack()

btn_show_menu = Tkinter.Button(root, text="Show Menu", fg="green", bg="white", command=show_menu)
btn_show_menu.pack()


btn_print_list = Tkinter.Button(root, text="Print Task List", fg="green", bg="white", command=print_list)
btn_print_list.pack()

btn_quit_program = Tkinter.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_quit_program.pack()

lb_tasks = Tkinter.Listbox(root)
lb_tasks.pack()

#btn_ = Tkinter.Button(root, text="", fg="green", bg="white", command=)
#btn_.pack()

# Start the main events loop
root.mainloop()
