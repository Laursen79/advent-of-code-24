import re
from functools import cache
from pathlib import Path


@cache
def get_mul_instructions():
    file_loc = Path(__file__).parent / "input.txt"
    pattern = re.compile("mul\(\d*,\d*\)")
    with open(file_loc, "r") as file:
        text = file.read()
        return pattern.findall(text)


def task_1():
    instructions = get_mul_instructions()
    pattern = re.compile("\((\d*),(\d*)\)")
    result = []
    for instruction in instructions:
        groups = pattern.search(instruction).groups()
        res = int(groups[0]) * int(groups[1])
        result.append(res)
    print(sum(result))
    # 178886550


def get_instructions():
    file_loc = Path(__file__).parent / "input.txt"
    pattern = re.compile("mul\((\d*),(\d*)\)|(don't\(\))|(do\(\))")
    with open(file_loc, "r") as file:
        text = file.read()
        return pattern.findall(text)


def task_2():
    instructions = get_instructions()
    do = True
    results = []
    for instruction in instructions:
        if "do()" in instruction:
            do = True
            continue
        if "don't()" in instruction:
            do = False
            continue
        if do:
            results.append(int(instruction[0]) * int(instruction[1]))

    print(sum(results))
    # 87163705
