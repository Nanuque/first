
word_1 = input("Enter word 1")
word_2 = input("Enter word 2")
print(word_1 + "," + word_2)

a = int(input("enter first num (a): "))
b = int(input("enter second num(b): "))
c = int(input("enter third num(c): "))
sum_result = a + b + c
print("sum of", a, ",", b, "and", c,"=", sum_result)

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
D = b**2 - 4*a*c
x1 = (-b + (D)**0.5) / (2*a)
x2 = (-b - (D)**0.5) / (2*a)
print(f"The roots of the equation are: x1 = {x1}, x2 = {x2}")

array = [1, 2, 'Hello', 'World']

array[0:2] == [1, 2, 'Hello']
array[-1] == 'World'
array[2] == 'Hello'


sum_result = 0
string = input("Please enter string: ")

for c in string[0:10]:
    num = ord(c)
    sum_result += num

print(sum_result)



string = input("please enter string: ")
result = ""

for c in reversed(string):
    result += c

print(result)



r = float(input("enter radius of circule"))
pi = 3.14
s = pi*r*r
print(s)



length = 700
velocity = 90
driving_time = length / velocity
print(driving_time)



name = input("enter name")
age = input("enter age")
print("My name is " + str(name) + " and age is " + str(age))

