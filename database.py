import sqlite3

def connect():
    return sqlite3.connect("students.db")

def add_student(name, age, course, email, phone):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, course, email, phone) VALUES (?, ?, ?, ?, ?)",
        (name, age, course, email, phone)
    )

    conn.commit()
    conn.close()

def view_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()
    return rows

def delete_student(id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

def update_student(id, name, age, course, email, phone):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?, email=?, phone=?
    WHERE id=?
    """, (name, age, course, email, phone, id))

    conn.commit()
    conn.close()