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
            print("Функционал в разработке...")
        elif choice == "6":
            print("До встречи!")
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")


if __name__ == "__main__":
    main()