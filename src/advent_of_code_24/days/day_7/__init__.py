from functools import cache
from pathlib import Path


@cache
def get_calibrations() -> list[(int, list[int])]:
    lines = []
    with open(Path(__file__).parent / "input.txt") as file:
        for line in file.readlines():
            line = line.split()
            lines.append((int(line[0].strip(":")), list(map(int, line[1:]))))

    return lines


def check(answer: int, operands: list[int]) -> int:
    return _check(answer, 0, operands)

def _check(answer: int, total: int, operands: list[int]) -> int:
    new_ops = operands.copy()
    _next = new_ops.pop(0)

    if len(new_ops) == 0:
        return answer if total + _next == answer or total * _next == answer else 0
    else:
        return _check(answer, total + _next, new_ops) or _check(answer, total * _next, new_ops)


def task_1():
    calibrations = get_calibrations()
    result = 0
    for answer, operands in calibrations:
        result += check(answer, operands)
    print(result)
    #6083020304036

def check_with_concat(answer: int, operands: list[int]) -> int:
    return _check_with_concat(answer, 0, operands)


def _check_with_concat(answer: int, total: int, operands: list[int]) -> int:
    new_ops = operands.copy()
    _next = new_ops.pop(0)
    concat = int(f"{total}{_next}")
    if len(new_ops) == 0:
        return answer if total + _next == answer or total * _next == answer or concat == answer else 0

    return _check_with_concat(answer, total + _next, new_ops) or _check_with_concat(answer, total * _next, new_ops) or _check_with_concat(answer, concat, new_ops)


def task_2():
    calibrations = get_calibrations()
    result = 0
    for answer, operands in calibrations:
        result += check_with_concat(answer, operands)
    print(result)
    #32980335983500, low
    #55650069826714, low
    #59002246504791, Correct