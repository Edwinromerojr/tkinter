import tkinter as tk

root = tk.Tk()

# size and title
root.geometry("500x500")
root.title("My First GUI")

#textword
label = tk.Label(root, text="Hello World", font=('Arial', 18))
label.pack(padx=20, pady=20)

#textfield
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=20, pady=20)

#input text
myentry = tk.Entry(root)
myentry.pack(padx=10, pady=10)

#button
button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

anotherbtn = tk.Button(root, text="TEST")
anotherbtn.place(x=200, y=400, height=100, width=100)

root.mainloop()
