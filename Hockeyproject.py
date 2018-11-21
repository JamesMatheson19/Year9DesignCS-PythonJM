import tkinter as tk 


root = tk.Tk()

titlelabel = tk.Label(root, text = "HOCKEY PROJECT", font=("Helvetica",16), background = "silver", foreground = "gold")
titlelabel.grid(row = 0, column = 0, columnspan = 2)


output = tk.Text(root, height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)

word1Label = tk.Label(root, text = "FLEX", foreground = "blue")
word1Label.grid(row = 2, column = 0, sticky = "NESW")

word2Label = tk.Label(root, text = "SPEED OF RELEASE", foreground = "blue")
word2Label.grid(row = 3, column = 0)

word3Label = tk.Label(root, text = "SPEED OF SHOT", foreground = "blue")
word3Label.grid(row = 4, column = 0)


ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 4, column = 1)

btnGo = tk.Button(root, text = "GENERATE")
btnGo.grid(row = 5, column = 1,)


root.mainloop()

