
name = input("enter your name:")
if name == "Mykhailo":
    print("Wow, Me too!")
else:
    print(f"Hello, {name} !")



import math
x = float(input("Введіть значення x (в радіанах), де -π <= x <= π: "))
if -math.pi <= x <= math.pi:
    y = math.cos(3 * x)
    print(f"Значення y = cos(3x) при x = {x} радіанів: {y}")
else:
    print("Значення x повинно бути в межах від -π до π.")


    


import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
c = float(input("Введіть значення c: "))
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Рівняння має два дійсні корені: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"Рівняння має один дійсний корінь: x = {x}")
else:
    print("Рівняння не має дійсних коренів")

 import math

def calculator():
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Зведення в ступінь")
    print("6. Квадратний корінь")
    print("7. Кубічний корінь")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    
    operation = int(input("Введіть номер операції (1-10): "))
    
    if operation in [1, 2, 3, 4, 5]:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        
        if operation == 1:
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        elif operation == 3:
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        elif operation == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")
            else:
                print("Помилка: Ділення на нуль!")
        elif operation == 5:
            result = num1 ** num2
            print(f"Результат: {num1} ^ {num2} = {result}")
    
    elif operation in [6, 7, 8, 9, 10]:
        num = float(input("Введіть число: "))
        
        if operation == 6:
            if num >= 0:
                result = math.sqrt(num)
                print(f"Результат: √{num} = {result}")
            else:
                print("Помилка: Квадратний корінь з від'ємного числа!")
        elif operation == 7:
            result = num ** (1/3)
            print(f"Результат: ³√{num} = {result}")
        elif operation == 8:
            result = math.sin(math.radians(num))
            print(f"Результат: sin({num}) = {result}")
        elif operation == 9:
            result = math.cos(math.radians(num))
            print(f"Результат: cos({num}) = {result}")
        elif operation == 10:
            result = math.tan(math.radians(num))
            print(f"Результат: tan({num}) = {result}")
    
    else:
        print("Невірний номер операції! Будь ласка, оберіть номер від 1 до 10.")

        

number = int(input("Введіть число:"))
message = "число парне" if number % 2 == 0 else "Число не парне"
print(message)


день_тижня = input("Напиши, який сьогодні день тижня: ")

робочі_дні = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця"]
вихідні = ["субота", "неділя"]

if день_тижня in робочі_дні:
    print("Сьогодні на роботу")
elif день_тижня in вихідні:
    print("Сьогодні вихідний")
else:
    print("Такого дня не існує")



