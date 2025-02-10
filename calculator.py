#dictionaries & functions
#


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return round(n1 / n2, 2)

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}

result = float(input("Enter a number: "))

while True:
    operation = input("Enter operation: ")

    if operation in operations:  # Überprüfen, ob die Operation gültig ist
        num2 = float(input("Enter number: "))
        result = operations[operation](result, num2)  # Dynamischer Aufruf
        print(result)
    else:
        print("Invalid operation.")  # Fehlermeldung für ungültige Eingabe

    if input("Done? Y/N: ").lower() == "y":
        break
