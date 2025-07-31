import sqlite3

def create_tables():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("DROP TABLE IF EXISTS genres")

    cursor.execute('''
        CREATE TABLE genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    genres = [("Фантастика",), ("Детектив",), ("Роман",), ("Фэнтези",)]
    cursor.executemany("INSERT INTO genres (name) VALUES (?)", genres)

    cursor.execute("SELECT id, name FROM genres")
    genre_map = {name: genre_id for genre_id, name in cursor.fetchall()}

    books = [
        ("1984", "George Orwell", 1949, 328, 5, genre_map["Фантастика"]),
        ("Убийство в Восточном экспрессе", "Agatha Christie", 1934, 256, 3, genre_map["Детектив"]),
        ("Анна Каренина", "Лев Толстой", 1877, 864, 2, genre_map["Роман"]),
        ("Гарри Поттер", "J.K. Rowling", 1997, 309, 10, genre_map["Фэнтези"]),
        ("Солярис", "Станислав Лем", 1961, 300, 4, genre_map["Фантастика"]),
        ("Шерлок Холмс", "Артур Конан Дойл", 1892, 221, 6, genre_map["Детектив"]),
    ]

    cursor.executemany('''
        INSERT INTO books (name, author, publication_year, number_of_pages, number_of_copies, genre_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', books)

    conn.commit()
    conn.close()

def select_books_with_genres():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT books.name, books.author, genres.name as genre_name
        FROM books
        JOIN genres ON books.genre_id = genres.id
    ''')

    results = cursor.fetchall()

    for row in results:
        print(f"Книга: {row[0]}, Автор: {row[1]}, Жанр: {row[2]}")

    conn.close()

if __name__ == "__main__":
    create_tables()
    insert_data()
    select_books_with_genres()
