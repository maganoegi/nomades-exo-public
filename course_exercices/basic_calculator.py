


def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def operation_factory(user_string):
    """takes a user input and returns a corresponding operation function.

    A function that represents a basic Factory design pattern.

    ARGS:
        user_string: str: user input.
    
    RETURNS:
        operation: Callable: the function representing an operation.
    """
    operation = None

    if user_string == "+":
        operation = addition
    elif user_string == "-":
        operation = substraction
    elif user_string == "*":
        operation = multiply
    else:
        operation = addition

    return operation

def get_valid_number_input():
    while True:
        user_input = input("please provide a number: ")
        try:
            result = int(user_input)
        except:
            continue
        finally:
            ...

        return result

def main():

    # get first numerical input (int)
    a = get_valid_number_input()

    # get second numerical input (int)
    b = get_valid_number_input()

    # get the operation (function)
    op_string = input("what is the operation ")
    operation = operation_factory(op_string)

    # perform the operation on the two numbers
    result = operation(a, b)

    # display the result
    print(f"{a} {op_string} {b} = {result}")

if __name__ == '__main__': # Ligne "imaginaire" de logique métier ==========
    main()





