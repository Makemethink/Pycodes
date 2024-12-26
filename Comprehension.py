def list_comprehension() -> None:
    lists = [1, 2, 3, 7, 8, 9]
    res = [num ** 2 for num in lists]
    print(res)

def list_comprehension_with_condition() -> None:
    lists = [7, 3, 9, 6, 8, 0, 2, 5, 1]
    res = [num for num in lists if num % 2 == 0]
    print(res)
    res = ['Even' if num % 2 == 0 else 'Odd' for num in lists]
    print(res)

def list_simple_comprehension() -> None:
    words = ['hi', 'hello', 'world', 'python', 'happy']
    res = [word.upper() for word in words]
    print(res)

def list_comprehension_to_flatten() -> None:
    nested_list = [[1, 2, 3], [4, 5], [6]]
    res = [digit for lists in nested_list for digit in lists]
    print(res)

def dict_comprehension() -> None:
    squares = {x: x ** 2 for x in range(1, 6)}
    print(squares)

def dict_comprehension_with_condition() -> None:
    res = {x: x ** 2 for x in range(1, 10) if x % 2 == 0}
    print(res)

    res = {x: 'Even' if x % 2 == 0 else 'Odd' for x in range(1, 10)}
    print(res)

def list_to_dict() -> None:
    items = [('apple', 1), ('banana', 2), ('cherry', 3)]
    dicts = {x: y for x, y in items}
    print(dicts)

def dict_comprehension_modify() -> None:
    original = {'a': 1, 'b': 2, 'c': 3}
    duplicate = {y: x for x, y in original.items()}
    print(duplicate)

def dict_comprehension_complex() -> None:
    res = {x: [y for y in range(1, x + 1)] for x in range(1,5)}
    print(res)

def main() -> None:
    list_comprehension()
    list_comprehension_with_condition()
    list_simple_comprehension()
    list_comprehension_to_flatten()

    list_to_dict()

    dict_comprehension()
    dict_comprehension_with_condition()
    dict_comprehension_modify()
    dict_comprehension_complex()

if __name__ == '__main__':
    main()
