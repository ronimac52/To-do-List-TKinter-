#from Christian Thompson via youtube
# Create GUI elements
import Tkinter
import tkMessageBox
import random

#Create root window
root = Tkinter.Tk()

# Change root window bg colour
root.configure(bg="white")

# Create title
root.title("Todo Helper")

# set window size
root.geometry("350x400")

#Create empty list
tasks = []

#List for testing
tasks =["music","coding","create invoice", "tax return"]

# Create functions:




def update_listbox():
    # clear the current listbox
    clear_listbox()
    # Populate listbox by appending each task to list
    for task in tasks:
        lb_tasks.insert("end", task)


def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task(event=None): # "event=None" so that enter key can add task without clicking the button
    #get user input(prompt)
    task = txt_input.get()
    # Ensure user has enetered a task
    if task !="":
      tasks.append(task)
      update_listbox()
    else:
        tkMessageBox.showwarning("Note!", "Please enter a task")
    # Clear the textbox to avoid adding the same task twice accidentally
    txt_input.delete(0, "end")

root.bind('<Return>', add_task)# bind return key to add_task so that enter key can add task without clicking the button

#.......For later integration with file io etc
#def select_task():
#    task = lb_tasks.get("active")
#    if task in tasks:
#        lbl_display["text"]=task
#    else:
#        tkMessageBox.showwarning("Note!", "Task {} is not in list, Please choose another task".format(task))
#    update_listbox()



def num_tasks():
    num_tasks = len(tasks)
    msg = "There are {} tasks in the list".format(num_tasks)
    lbl_display["text"]=msg

def delete_task():

    # Get the text of the currently selected item
    task = lb_tasks.get("active")
    # Confirm task is in list
    if task in tasks:
        confirm_del = tkMessageBox.askyesno("Confirm Deletion", "Are you sure you want to delete task:   ** {} ** ?".format(task))
        if confirm_del:# tkmessageBox.askyesno returns boolean
          tasks.remove(task)
    update_listbox()


def sort_list_up():
    tasks.sort()
    update_listbox()

def sort_list_down():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def rand_task():
    task = random.choice(tasks)
    # Update display label
    lbl_display["text"]=task

def delete_all():
    # As list is being changed, it needs to be global.
    global tasks
    confirm_del = tkMessageBox.askyesno("Delete All Confirmation", "Are you sure you want to delete all tasks?")
    if confirm_del:
      # Clear the tasks list.
      tasks = []
      # Update listbox
      update_listbox()

def exit():
    quit()

root.bind('<Return>', add_task)

# Create title in root widget of GUI with white background
lbl_title = Tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row= 0, column=0 )

lbl_display = Tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0 , column=1 )

txt_input = Tkinter.Entry(root, width = 15)
txt_input.grid(row=1 , column=1 )

btn_add_task = Tkinter.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row= 1, column=0 )

#btn_select_task = Tkinter.Button(root, text="Select Task", fg="green", bg="white", command=select_task)
#btn_select_task.grid(row= 2, column=0 )

btn_num_tasks = Tkinter.Button(root, text="Number of Tasks", fg="green", bg="white", command=num_tasks)
btn_num_tasks.grid(row=3 , column= 0)

btn_delete_task = Tkinter.Button(root, text="Delete Task", fg="green", bg="white", command=delete_task)
btn_delete_task.grid(row=4 , column=0 )

btn_delete_all = Tkinter.Button(root, text="Delete All", fg="green", bg="white", command=delete_all)
btn_delete_all.grid(row=5 , column= 0)

btn_sort_list_up = Tkinter.Button(root, text="Sort List Ascending", fg="green", bg="white", command=sort_list_up)
btn_sort_list_up.grid(row=6 , column=0 )

btn_sort_list_down = Tkinter.Button(root, text="Sort List Descending", fg="green", bg="white", command=sort_list_down)
btn_sort_list_down.grid(row=7 , column=0 )

btn_rand_task = Tkinter.Button(root, text="Random Task", fg="green", bg="white", command=rand_task)
btn_rand_task.grid(row=8 , column=0 )


btn_quit_program = Tkinter.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_quit_program.grid(row=9 , column=0 )

lb_tasks = Tkinter.Listbox(root)
lb_tasks.grid(row=2 , column=1, rowspan=7 )

#Populate listbox at program start for future file io functionality
def show_listbox():
    global tasks
    for task in tasks:
        lb_tasks.insert("end", task)
#Populate listbox at program start for future file io functionality
show_listbox()

# Start the main events loop
root.mainloop()
