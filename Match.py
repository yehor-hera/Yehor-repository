day = 3
match day:
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

day = "Saturday"
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Це робочий день")
    case "Saturday" | "Sunday":
        print("Ура, вихідний!")
    case _:
        print("Невідомий день тижня")

age = 20
match age:
    case a if a < 18:
        print("Minor")
    case a if 18 <= a < 65:
        print("Adult")
    case _:
        print("Senior")