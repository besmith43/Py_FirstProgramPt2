#!/usr/bin/env python3

import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sides', default=20, choices=[4, 6, 8, 10, 12, 20, 100], type=int, help="Number of sides on the dice to be rolled")
args = parser.parse_args()
sides = args.sides

result = random.randint(1, sides)

print()
print()
print(result)
print()
print()
