
x = 5
y = 3.14
z = 2+3j

print(type(x))
print(type(y))
print(type(z))

num = -15.786

# Знаходження модуля та округлення
abs_val = abs(num)
round_val = round(num, 2)

# Вивід результатів
print(abs_val)
print(round_val)

a = 10

# Перетворення типів
float_a = float(a)
complex_a = complex(a)

# Вивід значень та їх типів
print(float_a, type(float_a))
print(complex_a, type(complex_a))

apples = 23
people = 5

# Обчислення
per_person = apples // people
leftover = apples % people

# Вивід
print(per_person)
print(leftover)