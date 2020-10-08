"""
Write decorator called log_to_file that log any call of decorated function onto file “function_call.log“
file should be created if not exist, else should append any new call as new line
 “Calling function {function_name} with arguments:
{arguments in a row}”. Decorator should be used with @ notation.
See how to get function name https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string
"""


# decorator
def log_to_file(func):
    def wrapper(*args):
        with open("function_call.log", "a+") as file:
            file.write("Calling function '{}' with arguments: {}\n".format(func.__name__, args))

    return wrapper


@log_to_file
def new_function_1(a, b):
    pass


@log_to_file
def new_function_2(a, b, c):
    pass


new_function_1(1, 2)
new_function_2("1", "2", "3")

new_function_1(233, 6)
new_function_2("8", None, "322")
