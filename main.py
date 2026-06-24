import json
import os

FILENAME = "books.json"


def load_books():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_books(books):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def delete_book():
    books = load_books()
    if not books:
        print("Нечего удалять, трекер пуст.")
        return

    print("\n--- Доступные для удаления книги ---")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book['author']} — «{book['title']}»")

    while True:
        try:
            choice = int(input("\nВведите номер книги для удаления (или 0 для отмены): "))
            if choice == 0:
                return
            if 1 <= choice <= len(books):
                removed = books.pop(choice - 1)
                save_books(books)
                print(f"Книга «{removed['title']}» успешно удалена.")
                break
            print("Неверный номер.")
        except ValueError:
            print("Введите корректное число.")

def main():
    while True:
        print("\n=== Меню ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            print("Функционал в разработке...")
        elif choice == "2":
            print("Функционал в разработке...")
        elif choice == "3":
            print("Функционал в разработке...")
        elif choice == "4":
            print("Функционал в разработке...")
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("До встречи!")
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")


if __name__ == "__main__":
    main()