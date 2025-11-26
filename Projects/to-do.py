import tkinter as tk
from tkinter import messagebox

# --- Setup ---
window = tk.Tk()
window.title("To-Do List with Checkboxes")
window.geometry("400x500")
window.config(bg="#E6F7FF")

# --- Task Container ---
tasks = []

# --- Functions ---
def add_task():
    task_text = entry.get()
    if task_text:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(task_frame, text=task_text, variable=var,
                            font=("Arial", 12), anchor='w', bg="#E6F7FF")
        cb.pack(fill='x', padx=10, pady=2)
        tasks.append((cb, var))
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_selected():
    for cb, var in tasks[:]:
        if var.get():
            cb.destroy()
            tasks.remove((cb, var))

def clear_all():
    for cb, _ in tasks:
        cb.destroy()
    tasks.clear()

# --- Widgets ---
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(window, text="Add Task", command=add_task, bg="#A3E4D7", font=("Arial", 12))
add_btn.pack(pady=5)

delete_btn = tk.Button(window, text="Delete Selected", command=delete_selected, bg="#F5B7B1", font=("Arial", 12))
delete_btn.pack(pady=5)

clear_btn = tk.Button(window, text="Clear All", command=clear_all, bg="#AED6F1", font=("Arial", 12))
clear_btn.pack(pady=5)

task_frame = tk.Frame(window, bg="#E6F7FF")
task_frame.pack(fill='both', expand=True, padx=10, pady=10)

window.mainloop()

