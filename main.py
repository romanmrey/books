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

def add_book():
    books = load_books()
    author = input("Введите автора: ").strip()
    title = input("Введите название книги: ").strip()

    # Проверка на дубликаты (для закрытия Issue #1)
    for book in books:
        if book['author'].lower() == author.lower() and book['title'].lower() == title.lower():
            print("Ошибка: Такая книга уже есть в трекере!")
            return

    # Валидация оценки
    while True:
        try:
            rating = int(input("Введите оценку (от 1 до 5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть целым числом от 1 до 5.")
        except ValueError:
            print("Пожалуйста, введите число.")

    date_read = input("Введите дату прочтения (например, ГГГГ-ММ-ДД): ").strip()

    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date_read": date_read
    })
    save_books(books)
    print(f"Книга «{title}» успешно добавлена!")

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
            add_book()
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