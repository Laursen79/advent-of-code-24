import copy
from collections import Counter
from functools import cache
from pathlib import Path


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

def is_safe_fast(report: list[int]) -> bool:
    prev_diff = 0
    for i in range(len(report) - 1):
        # Rule 1: strictly increasing or decreasing.
        diff = report[i + 1] - report[i]
        if not prev_diff ^ diff >= 0 and i != 0:
            return False
        prev_diff = diff

        # Rule 2: diff must be at least 1 and at most 3
        if not 0 < abs(diff) <= 3:
            return False

    return True


def task_1():
    reports = get_reports()
    safe_count = Counter(map(is_safe_fast, reports))[True]
    print(safe_count)
    # 526


def problem_damper(report: list[int]) -> bool:
    for i in range(len(report)):
        clone = copy.deepcopy(report)
        clone.pop(i)
        if is_safe_fast(clone):
            return True

    return False


def task_2():
    reports = get_reports()
    safe_count = Counter(map(problem_damper, reports))[True]
    print(safe_count)
    # 566
