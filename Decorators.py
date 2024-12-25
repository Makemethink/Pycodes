from typing import Callable

# The function which is converted to decorator using wrapper and nested function
def greetings(func) -> Callable:
    def wrapper(movies_list):
        print(f'Entering to {func.__name__}')
        func(movies_list)
        print(f'Exiting from {func.__name__}')
    return wrapper

@greetings
def print_movies(movies_list: list[str]) -> None:
    """
    function using greetings decorator
    :param movies_list:
    :return:
    """
    for index, movie in enumerate(movies, start = 1):
        print(f'{str(index).zfill(2)}. {movie}')

if __name__ == '__main__':

    movies = ['The sixth sense', 'Fight club', 'Shutter island', 'Machinist', 'Seven', 'Black Swan',
              'Vertigo', 'Perfect Blue', 'The Prestige', 'Insomnia', 'Midsommar']
    print_movies(movies)
