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
