# Задача 1:
# Создайте две переменные, name и age, и присвойте им значения.
# Напечатайте сообщение, используя эти переменные.

# Решение:
name = "shyn1ck"
age = 21
print(f"Меня зовут {name}, мне {age} лет.")

# Задача 2:
# Создайте список чисел до 10.
# Используйте нарезку списка, чтобы напечатать первые три элемента и последние три элемента списка.

# Решение:
numbers = list(range(10))  # Список чисел от 0 до 9
print("Первые три элемента:", numbers[:3])
print("Последние три элемента:", numbers[-3:])

# Задача 3:
# Создайте словарь с именем student с ключами: имя, возраст и оценка.
# Заполните значения к предыдущим ключам вашими данными.
# Добавьте новый ключ subject со значением math.
# Распечатайте обновленный словарь.

# Решение:
student = {"имя": "shyn1ck", "возраст": 20, "оценка": "A"}

print(student)
# Добавление нового ключа
student["subject"] = "math"

print(student)



# Задача 4
# Создайте, два набора, set1 и set2, с некоторыми общими элементами.
# Выведите объединение и пересечение двух наборов.

# Решение:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
intersection = set1.intersection(set2)

print("Объединение:", union)
print("Пересечение:", intersection)

# Задача 5:
# Создайте словарь, представляющий цены товаров в магазине.
# Используйте цикл для перебора товаров и распечатайте каждый товар вместе с его ценой.


# Решение:
prices = {
    "яблоко": 50,
    "банан": 30,
    "апельсин": 40
}

for item, price in prices.items():
    print(f"{item}: {price} сум")

# Задача 6:
# Напишите программу, которая принимает два числа в качестве вводимых пользователем данных input.
# Выполните основные арифметические операции (сложение, вычитание, умножение, деление) с числами.


# Решение:
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print("Сложение:", num1 + num2)
print("Вычитание:", num1 - num2)
print("Умножение:", num1 * num2)
print("Деление:", num1 / num2 if num2 != 0 else "На ноль делить нельзя!")

