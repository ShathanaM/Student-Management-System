import tkinter as tk
from database import add_student, view_students, delete_student

def add():
    add_student(
        name_entry.get(),
        age_entry.get(),
        course_entry.get(),
        email_entry.get(),
        phone_entry.get()
    )
    show_students()

def show_students():
    listbox.delete(0, tk.END)

    for student in view_students():
        listbox.insert(tk.END, student)

def delete():
    selected = listbox.get(listbox.curselection())
    delete_student(selected[0])
    show_students()

root = tk.Tk()
root.title("Student Management System")

tk.Label(root, text="Name").grid(row=0)
tk.Label(root, text="Age").grid(row=1)
tk.Label(root, text="Course").grid(row=2)
tk.Label(root, text="Email").grid(row=3)
tk.Label(root, text="Phone").grid(row=4)

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
course_entry = tk.Entry(root)
email_entry = tk.Entry(root)
phone_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)
course_entry.grid(row=2, column=1)
email_entry.grid(row=3, column=1)
phone_entry.grid(row=4, column=1)

tk.Button(root, text="Add Student", command=add).grid(row=5)
tk.Button(root, text="View Students", command=show_students).grid(row=6)
tk.Button(root, text="Delete Student", command=delete).grid(row=7)

listbox = tk.Listbox(root, width=60)
listbox.grid(row=8, columnspan=2)

root.mainloop()