import copy
from collections import Counter
from functools import cache
from itertools import count
from pathlib import Path
from sys import stdout


@cache
def get_reports() -> list[list[int]]:
    file_loc = Path(__file__).parent / "input.txt"
    reports = []
    with open(file_loc, "r") as file:
        for line in file.readlines():
            reports.append(list(map(int, line.split())))
    return reports


def is_safe(report: list[int]) -> bool:
    # Rule 1:
    if not (report == sorted(report) or report == list(reversed(sorted(report)))):
        return False
    # Rule 2:
    for num in range(len(report) - 1):
        diff = abs(report[num] - report[num + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def task_1():
    reports = get_reports()
    safe_count = Counter(map(is_safe, reports))[True]
    print(safe_count)
    # 526


def problem_damper(report: list[int]) -> bool:
    for i in range(len(report)):
        clone = copy.deepcopy(report)
        clone.pop(i)
        if is_safe(clone):
            return True

    return False


def task_2():
    reports = get_reports()
    safe_count = Counter(map(problem_damper, reports))[True]
    print(safe_count)
    # 566
