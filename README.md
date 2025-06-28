# 📚 Biblioteca Virtual

Uma aplicação gráfica feita em **Python** com **Tkinter** que permite o cadastro de **livros** e **usuários** em um banco de dados **PostgreSQL**. Ideal para uso didático ou como base para projetos maiores.

---

## 🖼️ Interface Gráfica

A interface é dividida em duas abas:

- **Livros**: formulário para cadastrar livros.
- **Usuários**: formulário para cadastrar usuários.

Tudo organizado em uma janela simples com campos de entrada e botões de ação.

---

## 🧰 Funcionalidades

### ✅ Cadastro de Livros

- Nome do livro  
- Autor  
- Editora  
- ID do livro (único)

### ✅ Cadastro de Usuários

- Nome do usuário  
- ID do usuário (único)

---

## 🗃️ Estrutura do Banco de Dados

Crie o banco de dados PostgreSQL com o nome `bibliotecavirtual` e execute os comandos abaixo para criar as tabelas:

```sql
CREATE TABLE livros (
    id INT PRIMARY KEY,
    bookname VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    publisher VARCHAR(50) NOT NULL
);

CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    bookcounter INT NOT NULL DEFAULT 0
);

Altere os dados de conexão no código para corresponder às configurações do seu PostgreSQL:

connect = psycopg2.connect(
    dbname="bibliotecavirtual",
    user="postgres",
    host="localhost",
    port="5432",
    password="sua_senha_aqui"
)
