from asyncio import as_completed
from concurrent.futures import ProcessPoolExecutor, wait
from pathlib import Path
from functools import cache


def get_input():
    file_loc = Path(__file__).parent / "input.txt"
    with open(file_loc, "r") as file:
        return list(map(int, file.read().split()))


@cache
def recursive_cached(nums, iterations: int):
    if iterations == 0:
        return len(nums)
    result = 0
    for number in nums:
        str_num = str(number)
        if number == 0:
            result += recursive_cached((1,), iterations - 1)
        elif len(str_num) % 2 == 0:
            mid = int(len(str_num) / 2)
            high = int(str_num[:mid])
            low = int(str_num[mid:])
            result += recursive_cached((high, low), iterations - 1)
        else:
            result += recursive_cached((number * 2024,), iterations - 1)
    return result


def task_1():
    input = get_input()
    result = recursive_cached(tuple(input), 25)
    print(result)


def task_2():
    input = get_input()
    result = recursive_cached(tuple(input), 75)
    print(result)
