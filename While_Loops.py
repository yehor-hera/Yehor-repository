i = 0

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i <= 10:
    if i == 5:
        print("Found number 5, stopping the loop!")
        break
    print(f"Current number: {i}")
    i += 1