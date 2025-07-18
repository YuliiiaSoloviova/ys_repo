import re
from datetime import datetime, timedelta

# --- Дані ---
contacts = [
    {
        "ФІО": "Іваненко Іван Іванович",
        "Адреса": "Київ, вул. Хрещатик 1",
        "Телефон": "+380991112233",
        "Email": "ivan@gmail.com",
        "День народження": "2000-08-15"
    },
    {
        "ФІО": "Петренко Олена Миколаївна",
        "Адреса": "Львів, вул. Шевченка 22",
        "Телефон": "+380671234567",
        "Email": "olena@gmail.com",
        "День народження": "1995-07-20"
    }
]

notes = [
    {
        "Текст": "Купити подарунок",
        "ФІО": "Іваненко Іван Іванович"
    },
    {
        "Текст": "Подзвонити щодо зустрічі",
        "ФІО": "Петренко Олена Миколаївна"
    }
]

# --- Валідації ---
def validate_phone(phone):
    return re.match(r'^\+380\d{9}$', phone)

def validate_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def pause():
    input("\nНатисніть Enter щоб продовжити...")

# --- Контакти ---
def add_contact():
    print("\n--- Додавання нового контакту ---")
    name = input("ФІО: ")
    address = input("Адреса: ")
    phone = input("Телефон (+380XXXXXXXXX): ")
    if not validate_phone(phone):
        print("❌ Некоректний номер телефону!")
        return
    email = input("Email: ")
    if not validate_email(email):
        print("❌ Некоректний email!")
        return
    birthday = input("Дата народження (рррр-мм-дд): ")
    try:
        datetime.strptime(birthday, "%Y-%m-%d")
    except:
        print("❌ Некоректна дата!")
        return
    contacts.append({
        "ФІО": name,
        "Адреса": address,
        "Телефон": phone,
        "Email": email,
        "День народження": birthday
    })
    print("✅ Контакт додано.")

def list_birthdays(days):
    print(f"\n--- Контакти з днем народження через {days} днів ---")
    today = datetime.today()
    for contact in contacts:
        bday = datetime.strptime(contact["День народження"], "%Y-%m-%d")
        next_bday = bday.replace(year=today.year)
        if next_bday < today:
            next_bday = next_bday.replace(year=today.year + 1)
        delta = (next_bday - today).days
        if delta == days:
            print(f'{contact["ФІО"]} - День народження: {contact["День народження"]}')

def search_contacts():
    print("\n--- Пошук контакту ---")
    query = input("Введіть значення для пошуку: ").lower()
    found = False
    for c in contacts:
        if any(query in str(value).lower() for value in c.values()):
            print(c)
            found = True
    if not found:
        print("Контакти не знайдено.")

def edit_contact():
    print("\n--- Редагування контакту ---")
    name = input("Введіть ФІО контакту для редагування: ")
    for c in contacts:
        if c["ФІО"].lower() == name.lower():
            print("Поточна інформація:", c)
            c["Адреса"] = input("Нова адреса: ")
            phone = input("Новий телефон: ")
            if validate_phone(phone):
                c["Телефон"] = phone
            else:
                print("❌ Некоректний номер. Не змінено.")
            email = input("Новий email: ")
            if validate_email(email):
                c["Email"] = email
            else:
                print("❌ Некоректний email. Не змінено.")
            c["День народження"] = input("Нова дата народження (рррр-мм-дд): ")
            print("✅ Контакт оновлено.")
            return
    print("❌ Контакт не знайдено.")

def delete_contact():
    print("\n--- Видалення контакту ---")
    name = input("Введіть ФІО для видалення: ")
    global contacts
    before = len(contacts)
    contacts = [c for c in contacts if c["ФІО"].lower() != name.lower()]
    if len(contacts) < before:
        print("✅ Контакт видалено.")
    else:
        print("❌ Контакт не знайдено.")

# --- Нотатки ---
def add_note():
    print("\n--- Додавання нотатки ---")
    text = input("Текст нотатки: ")
    name = input("ФІО контакту: ")
    notes.append({
        "Текст": text,
        "ФІО": name
    })
    print("✅ Нотатку додано.")

def search_notes():
    print("\n--- Пошук нотаток ---")
    query = input("Введіть текст або ФІО: ").lower()
    found = False
    for note in notes:
        if query in note["Текст"].lower() or query in note["ФІО"].lower():
            print(note)
            found = True
    if not found:
        print("❌ Нотатки не знайдено.")

def edit_note():
    print("\n--- Редагування нотатки ---")
    name = input("ФІО: ")
    for note in notes:
        if note["ФІО"].lower() == name.lower():
            print("Поточна нотатка:", note)
            note["Текст"] = input("Новий текст: ")
            print("✅ Нотатку оновлено.")
            return
    print("❌ Нотатку не знайдено.")

def delete_note():
    print("\n--- Видалення нотатки ---")
    name = input("ФІО: ")
    global notes
    before = len(notes)
    notes = [n for n in notes if n["ФІО"].lower() != name.lower()]
    if len(notes) < before:
        print("✅ Нотатку видалено.")
    else:
        print("❌ Нотатку не знайдено.")

# --- Меню ---
def main_menu():
    while True:
        print("\n" + "="*40)
        print("📘 Меню контактів та нотаток")
        print("="*40)
        print("1. Додати новий контакт")
        print("2. Пошук у книзі контактів")
        print("3. Редагувати контакт")
        print("4. Видалити контакт")
        print("5. Список днів народження через N днів")
        print("6. Додати нотатку")
        print("7. Пошук у нотатках")
        print("8. Редагувати нотатку")
        print("9. Видалити нотатку")
        print("0. Вихід")
        choice = input("Оберіть дію: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            try:
                n = int(input("Введіть кількість днів: "))
                list_birthdays(n)
            except:
                print("❌ Введіть число.")
        elif choice == "6":
            add_note()
        elif choice == "7":
            search_notes()
        elif choice == "8":
            edit_note()
        elif choice == "9":
            delete_note()
        elif choice == "0":
            print("👋 Вихід з програми.")
            break
        else:
            print("❌ Невірний вибір.")
        
        pause()

# Запуск програми
if __name__ == "__main__":
    main_menu()