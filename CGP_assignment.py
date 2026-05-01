import tkinter as tk

root = tk.Tk()
root.title("CGP Assignment")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()
canvas.create_rectangle(50, 50, 150, 150, fill="blue")
canvas.create_oval(200, 50, 300, 150, fill="red")
canvas.create_line(50, 220, 300, 220, width=3)
canvas.create_text(250, 300, text="Reyland Gajes", font=("Arial", 20), fill="green")

root.mainloop()