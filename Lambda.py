def filter_lambda() -> None:
    """
    using filter function, filtering the input based on lambda condition
    :return: None
    """
    nums = [7, 3, 9, 6, 8, 1]
    lam = lambda x: x % 2 == 0
    print(list(filter(lam, nums)))

def simple_lambda(number: int) -> None:

    square = lambda x: x * x
    print(square(number))

def map_lambda() -> None:
    """
    using map function mapping all the iterable element to lambda
    :return: None
    """
    # nums = [1, 2, 5, 6, 8, 9]
    # lam = lambda x: x ** 2
    # print(list(map(lam, nums)))

    # Single line
    print(list(map(lambda x: x ** 2, [1, 2, 5, 6, 8, 9])))

def sort_str_lambda() -> None:
    """
    sorting based on the length of the string
    :return: None
    """
    strings = ['good', 'bad', 'ugly', 'worst']
    lam = lambda x: len(x)
    print(list(sorted(strings, key = lam, reverse=True)))

def sort_tuple_lambda() -> None:
    """
    sorting based on the second index of tuple in list
    :return: None
    """
    container = [('anime', 5), ('movie', 2), ('series', 4), ('cartoons', 0), ('others', 8)]
    lam = lambda x: x[1]
    print(list(sorted(container, key=lam, reverse=False)))

def main() -> None:
    """
    Calling all the functions one by one
    :return: None
    """
    simple_lambda(4)
    filter_lambda()
    map_lambda()
    sort_str_lambda()
    sort_tuple_lambda()

if __name__ == '__main__':
    main()
