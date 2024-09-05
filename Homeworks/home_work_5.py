# Створіть програму, яка зчитує рядок, в якому знаходиться ПІБ користувача і перевіряє, чи складається рядок з літер, при чому кожне слово має бути записане з великої літери. Вивести результат на екран.

pib = input("Введіть ПІБ: ")
abetka = "абвгґдеєжзіїклмнопрстюфцщшчья'"

for c in pib:
    if str(c).lower() in abetka:
        pass
    else:
        print("ПІБ не складається з літер! Помилка")

for w in pib.split(" "):
    good = False

    for a in abetka:
        if str(a).upper() == w[0]:
            good = True
        
if good == False:
    print("ПІБ не починається з великої літери")

# Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел (в діапазоні має бути не менше 5 чисел). Вивести на екран суму другого, передостаннього, а також середнього арифметичного значення даної послідовності. 
user_input = input("Enter at least five numbers: ")
numbers = user_input.split(" ")
total = len(numbers)

if total < 5:
    print("Error, You must enter five or more numbers: ")

s = int(numbers[1]) + int(numbers[total - 2])

print("Sum of 2 and penultimate is ", s)

s = 0

for number in numbers:
    s = s + int(number)

print("Середнє арифметичне дорівнює ", s / total)


# Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору) у форматі RGB і виводить на екран кортеж, у якому зберігається колір.
r = int(input("Please enter red"))
g = int(input("Please enter green"))
b = int(input("Please enter blue"))

if r < 0 or r > 255:
    print("Red should be in range 0-255")
if g < 0 or g > 255:
    print("Green should be in range 0-255")
if b < 0 or b > 255:
    print("Blue should be in range 0-255")

print("Color is ", (r, g, b))

# Ознайомтеся за допомогою документації з класами namedtuple та deque модуля collections. Створіть фабрику іменованих кортежів оцінок для учнів однієї групи з предметів: алгебра, геометрія, історія, інформатика, географія. Вивести дані на екран.

from collections import namedtuple


Grades = namedtuple('Grades', ['алгебра', 'геометрія', 'історія', 'інформатика', 'географія'])


students = {
    'Олександр': Grades(алгебра=5, геометрія=4, історія=3, інформатика=5, географія=4),
    'Марія': Grades(алгебра=4, геометрія=5, історія=5, інформатика=4, географія=5),
    'Іван': Grades(алгебра=3, геометрія=3, історія=4, інформатика=3, географія=4),
    'Ольга': Grades(алгебра=5, геометрія=5, історія=5, інформатика=5, географія=5),
}


for student, grades in students.items():
    print(f"{student}:")
    print(f"  Алгебра: {grades.алгебра}")
    print(f"  Геометрія: {grades.геометрія}")
    print(f"  Історія: {grades.історія}")
    print(f"  Інформатика: {grades.інформатика}")
    print(f"  Географія: {grades.географія}")
    print()


# Напишіть програму, яка вводить з клавіатури послідовність чисел, перетворює послідовність на кортеж і виводить його відсортованим у порядку зростання. 
user_input = input("Enter at least five numbers: ")
almost_numbers = user_input.split(" ")

numbers = []

for n in almost_numbers:
    numbers.append( int(n) )

nums = sorted(numbers)
as_tuple = tuple(nums)

print(as_tuple)

#Напишіть програму для аналізу фідбеку від відвідувачів курорту «Морська зірка», яка повинна знаходити згадки про меню, спортзал, обслуговування(за кожне знайдене співпадіння нараховується 5% знижки на наступне відвідування). Якщо фідбек перевищив 60 символів, відвідувачу надається додаткова знижка 15% на наступне відвідування.
feedback = input("Напишіть свій відгук")
discount = 0

if "меню" in feedback:
    discount += 5
if "спортзал" in feedback:
    discount += 5
if "обслуговування" in feedback:
    discount += 5

if len(feedback) > 60:
    discount += 15

print("Ваша знижка ", discount)
