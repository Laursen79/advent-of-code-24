from collections import Counter
from pathlib import Path


def get_lists() -> (int, int):
    file_loc = Path(__file__).parent / "input.txt"
    right = []
    left = []
    with open(file_loc, "r") as file:
        for line in file.readlines():
            nums = line.split()
            right.append(int(nums[0]))
            left.append(int(nums[1]))
    return right, left

def task_1():
    left, right = get_lists()
    pairs = list(zip(sorted(right), sorted(left)))
    answer = []
    for right, left in pairs:
        answer.append(abs(right - left))

    print(sum(answer))

def task_2():
    left, right = get_lists()
    count = Counter(right)
    sim_score = []
    for loc_id in left:
        sim_score.append(loc_id * count[loc_id])

    print(sum(sim_score))