def type_check(correct_type):
    """
    function that check if the argument is as the type he needs to be or not
    contains a decorator that checks the type and return exception if its not as needed
    :param correct_type: correct type argument
    :return: return exception if its not as needed or the number*2 if it is
    """
    def decorator_type_check(function):
        def inner_type_check(argument):
            try:
                if not correct_type == type(argument):
                    raise Exception(f"{argument} is not of type {correct_type}")
                return function(argument)
            except Exception as error:
                print(error)
        return inner_type_check
    return decorator_type_check


@type_check(int)
def times2(number):
    return number * 2


if __name__ == "__main__":
    print(times2(1.4))
