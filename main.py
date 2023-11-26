import os, colorama, random
from art import *
from colorama import Fore, Style
colorama.init(True)

n = 23

def clear_screen():
    os.system("cls")

def print_menu():
    clear_screen()
    art = text2art("LB_12")
    print(f"{Fore.LIGHTBLACK_EX + art}")
    print(f"{Style.BRIGHT}{Fore.BLUE}Лабораторна робота 12{Fore.RESET}{Style.RESET_ALL}")
    print(f"""{Fore.CYAN}
    |1| Завдання 1.1
    |2| Завдання 1.2
    |3| Завдання 1.3
    |4| Завдання 1.4
    |5| Завдання 1.5
    |6| Завдання 1.6
    |7| Завдання 2.1
    |8| Завдання 2.2
    |9| Завдання 2.3
    |10| Завдання 2.4
    |11| Завдання 2.5
    |12| Завдання 2.6
    |13| Завдання 3.1
    |14| Завдання 3.2
    |15| Завдання 3.3
    |0| Вихід{Fore.RESET}
    """)

def main_menu():
    while True:
        print_menu()  
        choose = input(f"{Fore.CYAN}Виберіть завдання : {Fore.RESET}")
        if choose == "1" :
            clear_screen()
            task_1_1()
        elif choose == "2" :
            clear_screen()
            task_1_2()
        elif choose == "3" :
            clear_screen()
            task_1_3()
        elif choose == "4" :
            clear_screen()
            task_1_4()
        elif choose == "5" :
            clear_screen()
            task_1_5()
        elif choose == "6" :
            clear_screen()
            task_1_6()
        elif choose == "7" :
            clear_screen()
            task_2_1()
        elif choose == "8" :
            clear_screen()
            task_2_2()
        elif choose == "9" :
            clear_screen()
            task_2_3()
        elif choose == "10" :
            clear_screen()
            task_2_4()
        elif choose == "11" :
            clear_screen()
            task_2_5()
        elif choose == "12" :
            clear_screen()
            task_2_6()
        elif choose == "13" :
            clear_screen()
            task_3_1()
        elif choose == "14" :
            clear_screen()
            task_3_2()
        elif choose == "15" :
            clear_screen()
            task_3_3()
        elif choose == "0" :
            exit()

def float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            clear_screen()
            print("Помилка! Введіть коректне число.")
def default_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            clear_screen()
            print("Помилка! Введіть коректне число.")


def task_1_1():
    print("Завдання 1\n")
    a = float_input("Введіть перше число: ")
    b = float_input("Введіть друге число: ")

    if a < b:
        print(f"{a} - менше за {b}, тому їх значення:\n a = 0\n b = 1\n")
    elif a > b:
        print(f"{a} більше {b}, тому їх значення:\n a = 1\n b = 0\n")
    else:
        print("Числа рівні\n")  

    input("\nНатисніть, щоб повернутись до меню\n")


def task_1_2():
    print("Завдання 2\n")
    if n > 15:
        res = n+7
    elif n <= 15:
        res = n-5
    print(f"Число дорівнює : {res}")
    input("\nНатисніть, щоб повернутись до меню\n")

def task_1_3():
    print("Завдання 3\n")
    b = float_input("Введіть сторону трикутника : ")
    r = float_input("Введіть радіус кола : ")
    d = 2 * r
    if d <= b:
        print("Коло можна вписати у такий трикутник")
    else:
        print("Коло не можна вписати у такий трикутник")
    input("\nНатисніть, щоб повернутись до меню\n")


def task_1_4():
    db = {
        "Башук Юлія": round(random.uniform(1.0, 5.0), 2),
        "Білан Тарас": round(random.uniform(1.0, 5.0), 2),
        "Богдан Артем": round(random.uniform(1.0, 5.0), 2),
        "Василишин Андрій": round(random.uniform(1.0, 5.0), 2),
        "Гнатишин Степан": round(random.uniform(1.0, 5.0), 2),
        "Городиський Сергій": round(random.uniform(1.0, 5.0), 2),
        "Дзюма Вікторія": round(random.uniform(1.0, 5.0), 2),
        "Заваринська Марія": round(random.uniform(1.0, 5.0), 2),
        "Заяць Тимофій": round(random.uniform(1.0, 5.0), 2),
        "Креховецький Роман": round(random.uniform(1.0, 5.0), 2),
        "Кручківський Кирил": round(random.uniform(1.0, 5.0), 2),
        "Кухтін Владислав": round(random.uniform(1.0, 5.0), 2),
        "Левицька Оксана": round(random.uniform(1.0, 5.0), 2),
        "Мідик Станіслав": round(random.uniform(1.0, 5.0), 2),
        "Оскірко Владислав": round(random.uniform(1.0, 5.0), 2),
        "Оліярник Орест": round(random.uniform(1.0, 5.0), 2),
        "Правда Юрій": round(random.uniform(1.0, 5.0), 2),
        "Продивус Олег": round(random.uniform(1.0, 5.0), 2),
        "Ремарчук Владислав": round(random.uniform(1.0, 5.0), 2),
        "Свідерська Софія": round(random.uniform(1.0, 5.0), 2),
        "Серафинович Максим": round(random.uniform(1.0, 5.0), 2),
        "Суровий Данило": round(random.uniform(1.0, 5.0), 2),
        "Титаренко Юрій": round(random.uniform(1.0, 5.0), 2),
        "Фольварчук Владислав": round(random.uniform(1.0, 5.0), 2),
        "Хамуляк Соломія": round(random.uniform(1.0, 5.0), 2),
        "Хамуляк Христина": round(random.uniform(1.0, 5.0), 2),
        "Чабан Денис": round(random.uniform(1.0, 5.0), 2),
        "Шингельска Тетяна": round(random.uniform(1.0, 5.0), 2),
        "Юсів Павло": round(random.uniform(1.0, 5.0), 2),
    }
    
    sorted_db = sorted(db.items(), key=lambda x: x[1], reverse=True)
    
    top_count = min(3, len(sorted_db))
    print("Топ 3 результати:")
    for i in range(top_count):
        nick, result = sorted_db[i]
        print(f"{i+1}. {nick}: {result} метра")
    
    while True:
        choice = input("\n|1| Пошук за результатом\n|2| Топ 10 стрибків\n|0| Вихід\nОберіть опцію: ")
        
        if choice == '1':
            search_result = float_input("Введіть результат для пошуку: ")
            if search_result in db.values():
                result_names = [name for name, res in db.items() if res == search_result]
                print(f"Учні з результатом {search_result} метра: {', '.join(result_names)}")
            else:
                print(f"Результат {search_result} метра не знайдено в базі даних.")

        elif choice == '2':
            print("Топ 10 результатів:")
            for i in range(min(10, len(sorted_db))):
                nick, result = sorted_db[i]
                print(f"{i+1}. {nick}: {result} метра")

        elif choice == '0':
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")
            input("\nНатисніть, щоб повернутись до меню\n")

def task_1_5():
    timetable = {
        1: "історія",
        2: "математика",
        3: "географія",
        4: "інформатика",
        5: "фізкультура"
    }    
    number_lesson = default_input("Введіть номер уроку : ")
    if number_lesson in timetable:
        result = timetable[number_lesson]
        print(result)
    else :
        print("Урок з таким номером відсутній")

    input("\nНатисніть, щоб повернутись до меню\n")

def task_1_6():
    towns = {
        1: "Київ",
        2: "Харків",
        3: "Одеса",
        4: "Дніпро",
        5: "Миколаїв"
    }

    town_number = int(input("Введіть номер міста (від 1 до 5): "))

    if town_number in towns:
        result = towns[town_number]
        print(f"Місто {town_number} - {result}")

    else:
        print("Місто з таким номером відсутнє в списку")

    input("\nНатисніть, щоб повернутись до меню\n")

def task_2_1():
    a = float_input("Введіть число a : ")
    b = float_input("Введіть число b : ")
    c = float_input("Введіть число c : ")

    if a > b > c:
        a *= 2
        b *= 2
        c *= 2
        print(f"Результат: a = {a}, b = {b}, c = {c}")
    else:
        a -= 1
        b -= 1
        c -= 1
        print(f"Результат: a = {a}, b = {b}, c = {c}")
    input("\nНатисніть, щоб повернутись до меню\n")

def task_2_2():
    a = float_input("Введіть першу сторону трикутника : ")
    b = float_input("Введіть другу сторону трикутника : ")
    c = float_input("Введіть третю сторону трикутника : ")
    a_squared = a**2
    b_squared = b**2
    c_squared = c**2
    if a_squared + b_squared == c_squared or b_squared + a_squared == c_squared:
        print("Трикутник виконує теорему Піфагора, значить є прямокутним")
    else:
        print("Трикутник не виконує теорему Піфагора, тому не є прямокутним")
    input("\nНатисніть, щоб повернутись до меню\n")

def task_2_3():
    a = float_input("Введіть першу сторону трикутника : ")
    b = float_input("Введіть другу сторону трикутника : ")
    c = float_input("Введіть третю сторону трикутника : ")
    if a == b or a == c or b == c:
        print("Трикутник є рівнобедреним")
    else:
        print("Трикутник не є рівнобедреним")
    input("\nНатисніть, щоб повернутись до меню\n")

def task_2_4():
    a = default_input("Введіть скільки балів набрав перший учень : ")
    b = default_input("Введіть скільки балів набрав другий учень : ")
    c = default_input("Введіть скільки балів набрав третій учень : ")
    if a >= 5 and b >= 5 and c >= 5:
        print("Команда потрапить до фінальних змагань.")
    else:
        print("Команда не потрапить до фінальних змагань.")

    input("\nНатисніть, щоб повернутись до меню\n")

def task_2_5():
    k = random.randint(1, 5)
    a = default_input("Введіть кількість балів першого учня : ")
    b = default_input("Введіть кількість балів другого учня : ")

    if a >= k and b >= k:
        print(f"Обидва учні потраплять до команди, бо перший учень набрав {a} балів, а другий учень набрав {b} балів.")
    elif a >= k:
        print(f"Тільки перший учень потрапить до команди, бо він набрав {a} балів, а другий учень набрав менше {k} балів.")
    elif b >= k:
        print(f"Тільки другий учень потрапить до команди, бо він набрав {b} балів, а перший учень набрав менше {k} балів.")
    else:
        print(f"Обидва учні не змогли набрати необхідну кількість балів ({k}).")
    input("\nНатисніть, щоб повернутись до меню\n")

def task_2_6():
    win_dynamo_vs_vorskla = input("Чи виграло Динамо у матчі проти Ворскли? (Так/Ні): ").lower()
    lose_shakhtar_vs_dnipro = input("Чи програло Шахтар у матчі проти Дніпра? (Так/Ні): ").lower()
    if win_dynamo_vs_vorskla == "так" and lose_shakhtar_vs_dnipro == "так":
        print("Команда Динамо стане чемпіоном України!")
    else:
        print("Команда Динамо не стане чемпіоном України.")
    input("\nНатисніть, щоб повернутись до меню\n")

def task_3_1():
    sum = 0
    for number in range(8, 25, 2):
        sum += number
    print(f"Сума непарних чисел від 7 до 25 : {sum}")
    input("\nНатисніть, щоб повернутись до меню\n")

def task_3_2():
    max_value = 7
    sum = 0
    for i in range(1, max_value + 1):
        sum += i
    print(f"Сума чисел натурального ряду до {max_value} : {sum}")
    input("\nНатисніть, щоб повернутись до меню\n")


def task_3_3():
    sides = [3, 4.5, 6, 7.5, 9]
    for side in sides:
        result = side ** 3
        print(f"Об’єм куба зі стороною {side} дорівнює {result}")
    input("\nНатисніть, щоб повернутись до меню\n")



        





if __name__ == "__main__":
    main_menu()
    

