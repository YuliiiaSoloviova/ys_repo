#################################################################################
#Завдання 1 - Лічильник дата

#Імпортуйте модуль datetime
from datetime import datetime

def get_days_from_today(date_str):

    #Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    #Якщо вхідний рядок не відповідає формату дати
    except ValueError:
        raise ValueError("Невірний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
    
    #Отримайте поточну дату, використовуючи datetime.today()
    today = datetime.today().date()

    #Розрахуйте різницю між поточною датою та заданою датою
    delta = today - input_date

    #Поверніть різницю у днях як ціле число
    return delta.days

if __name__ == "__main__":
    user_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
    try:
        days_diff = get_days_from_today(user_input)
        print(f"Кількість днів від введеної дати до сьогодні: {days_diff}")
    except ValueError as e:
        print(e)

#################################################################################
#Завдання 2 - Лотерея

#Використовуйте модуль random для генерації випадкових чисел.
import random

def get_numbers_ticket(min, max, quantity):
  
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= (max - min + 1)):
        return []
    
    #Використовуйте множину або інший механізм для забезпечення унікальності чисел
    #random.sample повертає список унікальних випадкових чисел із вказаного діапазону — без повторів
    numbers = random.sample(range(min, max + 1), quantity)

    #Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел
    return sorted(numbers)

try:
    min_number = int(input("Введіть мінімальне число (не менше 1): "))
    max_number = int(input("Введіть максимальне число (не більше 1000): "))
    quantity_numbers = int(input("Скільки чисел потрібно вибрати: "))

    result = get_numbers_ticket(min_number, max_number, quantity_numbers)

    if result:
        print("Ваші лотерейні числа:", result)
    #Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
    else:
        print("Некоректні параметри. Перевірте, що:\n- мін ≥ 1\n- макс ≤ 1000\n- quantity між 1 і кількістю чисел у діапазоні.")

except ValueError:
    print("Будь ласка, вводьте лише цілі числа.")

#################################################################################
#Завдання 3 - SMS-розсилки

#Використовуйте модуль re для регулярних виразів для видалення непотрібних символів.
import re

def normalize_phone(phone_number):

    #Видаліть всі символи, крім цифр та '+', з номера телефону.
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)

    if cleaned_number.startswith('+380'):
        return cleaned_number

    #Перевірте, чи номер починається з '+', і виправте префікс згідно з вказівками.
    elif cleaned_number.startswith('380'):
    #На забувайте повертати нормалізований номер телефону з функції.
        return '+' + cleaned_number

    # Якщо номер починається з '+' але не з '+380' — замінювати на '+38'
    elif cleaned_number.startswith('+') and not cleaned_number.startswith('+380'):
    #На забувайте повертати нормалізований номер телефону з функції.
        return '+38' + cleaned_number[1:]

    # Якщо номер без міжнародного коду — додаємо '+38' на початок
    else:
    #На забувайте повертати нормалізований номер телефону з функції.
        return '+38' + cleaned_number

#Введення номерів через кому
raw_numbers_input = input("Введіть телефонні номери через кому: ")

#Перетворення введеного рядка у список номерів
raw_numbers = raw_numbers_input.split(',')

#Нормалізація кожного номера
sanitized_numbers = [normalize_phone(num.strip()) for num in raw_numbers]

#Виведення результату
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#################################################################################
#Завдання 4 - Дні народження

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    #Визначте поточну дату системи за допомогою datetime.today().date().
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        #Ви повинні перетворити дати народження з рядків у об'єкти datetime. 
        #Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Дата народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        #Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        #Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
        days_diff = (birthday_this_year - today).days

        if 0 <= days_diff <= 7:
            #Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
            if birthday_this_year.weekday() >= 5:
                congratulation_date = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
            else:
                congratulation_date = birthday_this_year

            #Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

#Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:)
#Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата')
users = [
    {"name": "John Doe", "birthday": "1985.06.15"},
    {"name": "Jane Smith", "birthday": "1990.06.16"},
    {"name": "Ann Black", "birthday": "1995.06.21"},
    {"name": "Tom White", "birthday": "2000.01.25"},
    {"name": "Sam Green", "birthday": "1988.01.26"},
    {"name": "Alice Blue", "birthday": "1992.01.28"},
    {"name": "Greg Pink", "birthday": "1980.01.29"}
]

#Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:)
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:")
for person in upcoming_birthdays:
    #Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань
    print(f"{person['name']} — {person['congratulation_date']}")
    