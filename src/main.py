books = []
def add_book():
    title = input("Название книги: ")
    author = input("Автор книги: ")
    books.append({'title': title, 'author': author})
    print("Книга добавлена!")
def show_books():
    if not books:
        print("Книг нет")
        return
        print("\nСписок книг:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} - {book['author']}")
def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать книги")
        print("3. Выйти")    
        choice = input("Выберите: ") 
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            break
        else:
            print("Неверный выбор")
if __name__ == "__main__":
    main()
