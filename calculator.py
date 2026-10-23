"""Simple command-line calculator built with Python.

Supports addition, subtraction, multiplication, and division.
Run with: python3 calculator.py
"""

def calculate(first, operator, second):
    """Return the result of applying operator to two numbers."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError("Unsupported operator. Choose +, -, *, or /.")


def main():
    print("=== Python Calculator ===")
    print("Operations: +  -  *  /")
    print("Type q at the operation prompt to quit.")

    while True:
        try:
            first_text = input("\nFirst number: ").strip()
            if first_text.lower() == "q":
                break
            first = float(first_text)

            operator = input("Operation (+, -, *, /): ").strip()
            if operator.lower() == "q":
                break

            second_text = input("Second number: ").strip()
            if second_text.lower() == "q":
                break
            second = float(second_text)

            result = calculate(first, operator, second)
            # Avoid showing .0 for whole-number results.
            if result.is_integer():
                result = int(result)
            print(f"Result: {result}")

        except ValueError as error:
            print(f"Input error: {error}")
        except ZeroDivisionError as error:
            print(f"Math error: {error}")

    print("Thanks for using the calculator!")


if __name__ == "__main__":
    main()
