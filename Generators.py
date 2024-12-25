# Generators and Yield

from typing import Generator

players = ['swami', 'nathan', 'rahul', 'stranger', 'anonymous']
subs = ['user', 'unknown', 'missing']

def gen_one() -> Generator[str, None, None]:
    for _ in players:
        yield _

def gen_two() -> Generator[str, None, None]:
    for _ in subs:
        yield _

def gen() -> Generator[str, None, None]:
    yield from gen_one()
    yield from gen_two()

if __name__ == '__main__':
    game = gen()
    number_of_players = int(input('Enter no.of players needed : '))
    try:
        for _ in range(number_of_players):
            print(next(game))
    except StopIteration as exp:
        print(f'Players not available count breached, recruit more player', str(exp))
