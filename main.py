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

def list_books():
    books = load_books()
    if not books:
        print("Ваш трекер пока пуст.")
        return
    print("\n--- Список книг ---")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book['author']} — «{book['title']}» | Оценка: {book['rating']} | Дата: {book['date_read']}")


def show_average_rating():
    books = load_books()
    if not books:
        print("Нет данных для расчета средней оценки.")
        return
    avg = sum(book['rating'] for book in books) / len(books)
    print(f"\nСредняя оценка прочитанных книг: {avg:.2f}")


def show_author_stats():
    books = load_books()
    if not books:
        print("Нет данных для статистики.")
        return
    stats = {}
    for book in books:
        stats[book['author']] = stats.get(book['author'], 0) + 1

    print("\n--- Статистика по авторам ---")
    for author, count in stats.items():
        print(f"{author}: прочитано книг — {count}")

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
            list_books()
        elif choice == "3":
            show_average_rating()
        elif choice == "4":
            show_author_stats()
        elif choice == "5":
            print("Функционал в разработке...")
        elif choice == "6":
            print("До встречи!")
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")


if __name__ == "__main__":
    main()