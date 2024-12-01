from argparse import ArgumentParser
from importlib import import_module


def main():
    parser = ArgumentParser()
    group = parser.add_argument_group()
    group.add_argument("day", type=int, default=1)
    group.add_argument("task", type=int, default=1)

    args = parser.parse_args()

    day = import_module(f"advent_of_code_24.days.day_{args.day}")

    task = getattr(day, f"task_{args.task}")

    print(f"Running day {args.day} task {args.task}")
    task()
