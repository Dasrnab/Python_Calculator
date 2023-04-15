from art import logo
from replit import clear

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


calculator_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}


def calculator():
    n1 = float(input("type your 1st number: "))
    sign_list = []
    for sign in calculator_dictionary:
        sign_list += sign
    print(sign_list)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick a symbol from the list: ")
        n2 = float(input("Enter your number: "))
        operation = calculator_dictionary[operation_symbol]
        answer = operation(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        continue_choice = input(
            "Type 'y' if you want to continue if not or start fresh type'n'")
        if continue_choice == 'y':
            n1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()

# print(sign_list)
# operation_sign = input("pick up an operation from the list: ")
# operation = calculator_dictionary[operation_sign]
# n3 = int(input("type your 3rd number: "))
# answer2 = operation(answer1, n3)
# print(answer2)
