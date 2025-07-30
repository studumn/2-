import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    conn.commit()

def insert_books():
    books = [
        ("1984", "George Orwell", 1949, "Dystopian", 328, 12),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 281, 10),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 8),
        ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy", 223, 20),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 15),
        ("Pride and Prejudice", "Jane Austen", 1813, "Romance", 279, 5),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Coming-of-age", 234, 6),
        ("Brave New World", "Aldous Huxley", 1932, "Science Fiction", 268, 9),
        ("Moby-Dick", "Herman Melville", 1851, "Adventure", 635, 4),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Philosophical", 430, 7)
    ]

    cursor.executemany("""
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)
    conn.commit()

def select_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    create_table()
    insert_books()
    select_books()
    conn.close()
