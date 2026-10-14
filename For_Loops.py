fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

for number in range(1, 6):
    if number == 3:
        print("Skipping number 3 (continue in action)")
        continue
    
    print(f"Current number: {number}")
else:
    print("Loop completed, all numbers checked!")