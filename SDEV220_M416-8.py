#Aubrie McIntyre
#16.8
import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
    (title TEXT,
    author TEXT,
    year INT)''')
curs.execute('INSERT INTO books VALUES(books2.csv)')
curs.execute('SELECT title from book ORDER BY count DESC')
curs.fetchall()