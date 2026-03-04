import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip().split("\n")[::-1]
output = 0

print(input)

for i, char in enumerate(input):
    if char == "O":
        print("adding", 2**i)
        output += 2**i

print(output)
