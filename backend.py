import sqlite3

 #create database connection
def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view_all():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall() #view function
    conn.close()
    return rows

def search_entry(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows=cur.fetchall() #view function
    conn.close()
    return rows

def delete_entry(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_entry(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


#needs to be added to execute every time I run frontend otherwise nothing will show
connect()

#insert("Utopia", "Wislawa Szymborksa", 1956, 9818643431)
#delete_entry(1)
#update_entry(2, "Ludzie bezdomni", "Stefan Zeromski", 1940, 12342352)
#print(view_all())
#print(search_entry(author="Dan Brown"))
