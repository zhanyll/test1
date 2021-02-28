# task 1
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

dicti = {}
for i in range(len(lst)):
    dicti.update({i: lst[i]})
    i += 1
print(dicti)

# task 2
import random
number = random.randint(1, 20)

for a in range(5):
    input_number = int(input("Введите число от 1 до 20: "))
    if input_number == number:
        print("Класс! Вы угадали!")
        break
    elif input_number < number:
        print("Слишком мало!")
    elif input_number > number:
        print("Слишком много!")
if input_number != number:
    print("Все, вы не выиграли. Игра завершена.")

# task 3
some_string = "something"
let = int((len(some_string) - 3)/2)
print(some_string[let: -let])

#task 4
a = "Aidana"
b = "Adilet"
h = 0
c = ''
while h < len(a):
    c += a[h] + b[h]
    h+=1
print(c)
