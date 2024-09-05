

# Дано числа a і b (a < b). Виведіть суму всіх натуральних чисел від a до b (включно).
a = int(input("Введіть число a (менше b): " ))
b = int(input("Введіть число b (більше a): "))
if a > b:
    print("а має бути менше b")
else:
    total_sum = sum(range(a,b +1))
print("Сума всіх натуральних чисел від" , a , "до" , b , "дорівнює", total_sum)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
number = int(input("Введіть число для обчислення факторіалу: "))
if number < 0:
    print("Факторіал не визначений для від'ємних чисел.")
else:
    fact = factorial(number)
    print(f"Факторіал числа {number} дорівнює {fact}.")

# Використовуючи вкладені цикли та функції print(‘*’, end=’’), print(‘ ‘, end=’’) та print() виведіть на екран прямокутний трикутник
for i in range(10):
    for i in range(1, + i):
        print("*", end="")
    print()  


# Дано числа a і b (a < b). Виведіть на екран суму всіх натуральних чисел від a до b (включно), які є кратними середньому арифметичному цього проміжку. 
a = int(input("Введіть число а (менше b): "))
b = int(input("Введіть число b (більше а): "))
if a > b :
    print("не вірно, а має бути менше за b")
else:
    average = (a + b) / 2
    total_sum = 0
    for i in range(a, b + 1):
        if i % average == 0:
            total_sum += i
    
    print(f"Сума всіх натуральних чисел від {a} до {b}, які є кратними {average}, дорівнює {total_sum}.")



# Створіть програму, яка малює на екрані прямокутник із зірочок заданою користувачем ширини та висоти.
y = int(input("введіть висоту прямокутника: "))
x = int(input("введіть ширину прямокутника: "))
for i in range(y):
    for i in range(x):
        print("*", end= "")
    print()    

    
# Створіть програму авторизації, в якій користувачеві дається 3 спроби ввести свої облікові дані (логін та пароль). Якщо користувач за меншу кількість спроб ввів вірні дані, програма достроково припиняє своє виконання та виводить на екран повідомлення: «Авторизацію успішно пройдено з «№» спроби». 
correct_login = "admin"
correct_password = "11111"
attempts = 3
for attempt in range(1, attempts + 1):
    login = input("enter your login: ")
    password = input("enter your password: ")
    if login == correct_login and password == correct_password:
        print(f"autorisation complete from {attempt} try ")
        break
    if attempt < attempts:
        print("invalid credentials, please try again: ")
    else:
        print("you have used all the attempts, access is denied ")
        







