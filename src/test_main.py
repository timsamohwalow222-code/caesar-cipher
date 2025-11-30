import main


def test_add_book():
    initial_length = len(main.books)
    test_book = {"title": "Test", "author": "Author"}
    main.books.append(test_book)
    assert len(main.books) == initial_length + 1
    main.books.pop()


def test_empty_list():
    original = main.books.copy()
    main.books.clear()
    assert len(main.books) == 0
    main.books.extend(original)
