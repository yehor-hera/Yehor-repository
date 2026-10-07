# Create variables
x = 5
y = 3.14
z = "Hello"

# Print the data type of each variable
print(type(x))
print(type(y))
print(type(z))


# Створення змінних
is_online = True
colors = ["red", "green", "blue"]

# Виведення типів даних
print(type(is_online))
print(type(colors))

# Текстова змінна
num_text = "100"

# Перетворення у ціле число
num_int = int(num_text)

# Обчислення та виведення результату й типу
print(num_int + 50)
print(type(num_int))

price = 19.99

# Перевірка типу (повертає True або False)
result = isinstance(price, float)
print(result)

a, b, c = 10, "Python", False

# Форматований вивід
print(f"a = {a}, тип: {type(a)}")
print(f"b = {b}, тип: {type(b)}")
print(f"c = {c}, тип: {type(c)}")