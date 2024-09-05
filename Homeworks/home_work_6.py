# Створіть список та введіть його значення. 
# Знайдіть найбільший та найменший елемент списку, а також суму та середнє арифметичне його значень. 
values = [int(x) for x in input("Введіть значення списку через пробіл: ").split()]
max_value = max(values)
min_value = min(values)
sum_values = sum(values)
average_value = sum_values / len(values)
print("Найбільший елемент:", max_value)
print("Найменший елемент:", min_value)
print("Сума елементів:", sum_values)
print("Середнє арифметичне значень:", average_value)

# Є два списки, які наповнюються користувачем з клавіатури. Сформувати список,
# в якому будуть міститися унікальні значення першого відносно другого списку та навпаки без повторень.
# Роздрукувати підсумковий об'єкт на екран в прямій послідовності, зворотній, а також виконати сортування за зростанням та спаданням.

list1 = input("Введіть перший список (через кому): ").split(',')
list2 = input("Введіть другий список (через кому): ").split(',')


unique_list1 = set(list1) - set(list2)
unique_list2 = set(list2) - set(list1)

result_list = list(unique_list1 | unique_list2)

print("Підсумковий список:", result_list)

print("Підсумковий список у зворотній послідовності:", result_list[::-1])
sorted_asc = sorted(result_list)
sorted_desc = sorted(result_list, reverse=True)

print("Підсумковий список за зростанням:", sorted_asc)
print("Підсумковий список за спаданням:", sorted_desc)

# Простим називається число, яке ділиться націло лише на одиницю і на саме себе. 
# Число 1 не вважається простим. Напишіть програму, яка знаходить усі прості числа в заданому проміжку, 
# виводить їх на екран, а потім на вимогу користувача виводить їхню суму або добуток.

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

primes = []

# Знаходження простих чисел в заданому діапазоні
for num in range(start, end + 1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

if not primes:
    print("У вказаному діапазоні немає простих чисел.")
else:
    print("Прості числа у вказаному діапазоні:", primes)
    
    choice = input("Введіть 'sum' для обчислення суми простих чисел або 'prod' для обчислення добутку: ")

    if choice == 'sum':
        total_sum = 0
        for prime in primes:
            total_sum += prime
        print(f"Сума простих чисел: {total_sum}")

    elif choice == 'prod':
        if len(primes) == 0:
            total_product = 0
        else:
            total_product = 1
            for prime in primes:
                total_product *= prime
        print(f"Добуток простих чисел: {total_product}")

    else:
        print("Неправильний вибір.")

  # Створіть цілочисельний список, введіть кількість його елементів і самі значення. 
  # Передбачити меню, в якому: після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку, 
  # а після натискання клавіші 2 – за зростанням.  

um_elements = int(input("Введіть кількість елементів списку: "))

numbers = []

for i in range(num_elements):
    value = int(input(f"Введіть елемент {i + 1}: "))
    numbers.append(value)

while True:
    print("\nМеню:")
    print("1 - Вивести значення у зворотному порядку")
    print("2 - Вивести значення за зростанням")
    print("0 - Вихід")

    choice = input("Виберіть опцію (1, 2 або 0): ")

    if choice == '1':
        print("Список у зворотному порядку:")
        print(numbers[::-1])
    
    elif choice == '2':
        sorted_numbers = sorted(numbers)
        print("Список за зростанням:")
        print(sorted_numbers)
    
    elif choice == '0':
        print("Вихід з програми.")
        break
    
    else:
        print("Невірний вибір, будь ласка, спробуйте ще раз.")   

# Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового списку new_list. 
# Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть дублювання списку new_list, repeat кількість разів. 
# Очистіть список int_list. 

int_list = [int(x) for x in input("Введіть натуральні числа через пробіл: ").split()]

new_list = [num for num in int_list if num % 2 != 0]

repeat = int(input("Введіть кількість повторів: "))


duplicated_list = new_list * repeat

int_list.clear()

print("Оригінальний список int_list (після очищення):", int_list)
print("Список new_list (непарні числа):", new_list)
print("Дубльований список:", duplicated_list)      

# Для цього завдання вихідний список значень беремо з підсумкового списку new_list завдання 5.
#  Користувач вводить з клавіатури значення; якщо таке є у цьому списку — вивести кількість його повторів та його позицію у цьому списку.

new_list = [3, 5, 7, 3, 8, 5, 3]

search_value = int(input("Введіть значення для пошуку: "))

count = new_list.count(search_value)
positions = [index for index, value in enumerate(new_list) if value == search_value]

if count > 0:
    print(f"Значення {search_value} зустрічається {count} раз(и) у списку.")
    print(f"Його позиції у списку: {positions}")
else:
    print(f"Значення {search_value} не знайдено у списку.")
    