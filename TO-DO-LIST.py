import json
import tkinter as tk
from tkinter import messagebox

def add_task():
    task_description = task_entry.get()
    if task_description:
        task = {"id": len(task_list) + 1, "description": task_description, "completed": False}
        task_list.append(task)
        task_entry.delete(0, tk.END)
        update_task_listbox()
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in task_list:
        status = "Completed" if task["completed"] else "Not Completed"
        task_listbox.insert(tk.END, f"{task['id']}. {task['description']} - {status}")

def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_id = int(task_listbox.get(selected_task).split(".")[0])
        for task in task_list:
            if task["id"] == task_id:
                task["completed"] = True
                update_task_listbox()
                break

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_id = int(task_listbox.get(selected_task).split(".")[0])
        task_list[:] = [task for task in task_list if task["id"] != task_id]
        update_task_listbox()

def save_tasks():
    with open('tasks.json', 'w') as f:
        json.dump(task_list, f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

task_list = load_tasks()

app = tk.Tk()
app.title("To-Do List")
app.configure(bg="lightblue")

# Configure colorful backgrounds and widget styles
task_entry = tk.Entry(app, width=50, bg="lightyellow", fg="black", font=("Helvetica", 12))
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task, bg="lightgreen", fg="black", font=("Helvetica", 12))
add_button.pack(pady=5)

task_listbox = tk.Listbox(app, width=50, height=10, bg="lightgray", fg="black", font=("Helvetica", 12))
task_listbox.pack(pady=10)

complete_button = tk.Button(app, text="Mark Completed", command=mark_completed, bg="lightpink", fg="black", font=("Helvetica", 12))
complete_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task, bg="lightcoral", fg="black", font=("Helvetica", 12))
delete_button.pack(pady=5)

save_button = tk.Button(app, text="Save Tasks", command=save_tasks, bg="lightskyblue", fg="black", font=("Helvetica", 12))
save_button.pack(pady=5)

update_task_listbox()
app.mainloop()
