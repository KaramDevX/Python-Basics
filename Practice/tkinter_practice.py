import tkinter as tk

window = tk.Tk() 
window.geometry('540x540')
window.title("DOPE button clicker")
window.config(background="#86FCFA")
counter = 0

def click():
    global counter
    counter += 1
    label.config(text=counter)

button = tk.Button(window, 
                   text='Click Me',
                   font=('Ink Free', 50, 'bold'),
                   highlightbackground='orange',
                   fg='black')

button.config(command=click)
button.pack()

label = tk.Label(window,
                 text = str(counter),
                 font=('ariel', 50, 'bold'))
label.pack()

window.mainloop() 