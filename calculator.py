

def add(a, b ):
    return a+b

def subtract(a, b):
    return a-b

def product(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a/b

def main():
    print("**************************")
    print("Welcome to the Simple Calculator")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("**************************")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == '1':
        print(f"{a} + {b} = {add(a, b)}")
    elif choice == '2':
        print(f"{a} - {b} = {subtract(a, b)}")
    elif choice == '3':
        print(f"{a} * {b} = {product(a, b)}")
    elif choice == '4':
        print(f"{a} / {b} = {divide(a, b)}")
    elif choice == '5':
        print("Exiting...")
        exit()
    else:
        print("Invalid Input")

main()