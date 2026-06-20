import math


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Error: Division by zero is not defined.")
    return x / y


def power(x: float, y: float) -> float:
    return x ** y


def sqrt(x: float) -> float:
    if x < 0:
        raise ValueError(
            "Error: The square root is not defined for negative numbers.")
    return math.sqrt(x)


def factorial(x: float) -> int:
    if x < 0 or not x.is_integer():
        raise ValueError(
            "Error: The factorial is only defined for non-negative integers.")
    return math.factorial(int(x))


def main():
    menu = (" 1: add \n 2: subtract \n 3: multiply \n 4: divide \n 5: power \n 6: sqrt \n 7: factorial \n 0: End of operation")
    while True:
        print("Please select one of the operations below:")

        try:
            operation = int(input(menu))
            if operation == 0:
                break
            if operation in [1, 2, 3, 4, 5]:
                x = float(input("enter the first number: "))
                y = float(input("enter the second number: "))
                if operation == 1:
                    print(f"The answer is equal to: {add(x, y)} ")
                elif operation == 2:
                    print(f"The answer is equal to: {subtract(x, y)}")
                elif operation == 3:
                    print(f"The answer is equal to: {multiply(x, y)}")
                elif operation == 4:
                    print(f"The answer is equal to: {divide(x, y)}")
                elif operation == 5:
                    print(f"The answer is equal to: {power(x, y)}")

            elif operation in [6, 7]:
                x = float(input("enter a number: "))
                if operation == 6:
                    print(f"The answer is equal to: {sqrt(x)}")
                elif operation == 7:
                    print(f"The answer is equal to: {factorial(x)}")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
