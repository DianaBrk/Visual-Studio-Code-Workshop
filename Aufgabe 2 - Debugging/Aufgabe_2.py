def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    x = 10
    y = 0

    addition = add(x, y)
    print(f"Addition: {addition}")

    subtraction = subtract(x, y)
    print(f"Subtraction: {subtraction}")

    multiplication = multiply(x, y)
    print(f"Multiplication: {multiplication}")

    try:
        division = divide(x, y)
        print(f"Division: {division}")
    except ValueError as e:
        print(er) 

    text = "Result: " + 12345
    print(text)

    my_list = [1, 2, 3]
    print(my_list[3])

if __name__ == "__main__":
    main()
