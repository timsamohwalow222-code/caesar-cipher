# src/main.py
import json
import os

DATA_FILE = "data/books.json"
books = []


def load_data():
    """Загрузка данных из файла при запуске"""
    global books
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                books = json.load(f)
            print(f"Загружено {len(books)} книг")
        else:
            print("Файл данных не найден, начинаем с пустого списка")
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        books = []


def save_data():
    """Сохранение данных в файл"""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
        print("Данные сохранены!")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")


def add_book():
    """Добавление новой книги"""
    title = input("Название книги: ")
    author = input("Автор книги: ")
    books.append({"title": title, "author": author})
    print("Книга добавлена!")


def show_books():
    """Показать все книги"""
    if not books:
        print("Книг нет")
        return

    print("\nСписок книг:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} - {book['author']}")


def main():
    """Основная функция программы"""
    load_data()

    while True:
        print("\n1. Добавить книгу")
        print("2. Показать книги")
        print("3. Выйти и сохранить")

        choice = input("Выберите: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            save_data()
            print("До свидания!")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
