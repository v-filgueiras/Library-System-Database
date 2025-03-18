import psycopg2
from tkinter import *
from tkinter import ttk

connect = psycopg2.connect(
    dbname="bibliotecavirtual",
    user="postgres",
    host="localhost",
    port="5432",
    password="945d7a2d195b46afbb322b2e94e10846"
)

def bookregister():
    book_name = bookname.get()
    author_name = author.get()
    publisher_name = publisher.get()
    book_id = id.get()

    cn = connect.cursor()
    
    try:
        cn.execute('''
        INSERT INTO livros (bookname, author, publisher, id)
        VALUES (%s, %s, %s, %s)
        ''', (book_name, author_name, publisher_name, book_id))
        connect.commit() 
        print('Livro Registrado')
    except Exception as e:
        print(f"Erro ao registrar livro: {e}")
    finally:
        cn.close() 

def userregister():
    username_value = username.get()
    user_id = userid.get()

    cn = connect.cursor()

    try:
        cn.execute('''
        INSERT INTO usuarios (username, id)
        VALUES (%s, %s)
        ''', (username_value, user_id))
        connect.commit()
        print('Usuário Cadastrado')
    except Exception as e:
        print(f"Erro ao registrar usuário: {e}")
    finally:
        cn.close() 

mainwindow = Tk()
mainwindow.geometry('400x400') 
mainwindow.title('Biblioteca Virtual')

notebook = ttk.Notebook(mainwindow)
notebook.pack(expand=1, fill='both')

aba1 = Frame(notebook)
aba2 = Frame(notebook)

notebook.add(aba1, text='Livros')
notebook.add(aba2, text='Usuários')

mainheader = Label(aba1, text='Cadastro de Livros', font=('Arial', 14))
mainheader.grid(row=0, column=0, columnspan=2, pady=10)

bookname_label = Label(aba1, text='Nome do Livro:')
bookname_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
bookname = Entry(aba1)
bookname.grid(row=1, column=1, padx=10, pady=5)

author_label = Label(aba1, text='Autor:')
author_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
author = Entry(aba1)
author.grid(row=2, column=1, padx=10, pady=5)

publisher_label = Label(aba1, text='Editora:')
publisher_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
publisher = Entry(aba1)
publisher.grid(row=3, column=1, padx=10, pady=5)

id_label = Label(aba1, text='ID do Livro:')
id_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
id = Entry(aba1)
id.grid(row=4, column=1, padx=10, pady=5)

registerbookbutton = Button(aba1, text='Registrar Livro', command=bookregister)
registerbookbutton.grid(row=5, column=0, columnspan=2, pady=10)

secondaryheader = Label(aba2, text='Cadastro de Usuários', font=('Arial', 14))
secondaryheader.grid(row=0, column=0, columnspan=2, pady=10)

username_label = Label(aba2, text='Nome do Usuário:')
username_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
username = Entry(aba2)
username.grid(row=1, column=1, padx=10, pady=5)

userid_label = Label(aba2, text='ID do Usuário:')
userid_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
userid = Entry(aba2)
userid.grid(row=2, column=1, padx=10, pady=5)

userregisterbutton = Button(aba2, text='Registrar Usuário', command=userregister)
userregisterbutton.grid(row=3, column=0, columnspan=2, pady=10)

mainwindow.mainloop()
