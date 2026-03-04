import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sorted([int(b) for b in sys.stdin.read().strip().split("\n")])
counter = 0

for b in input:
    print(b, end=" ")
    counter += 1
    if counter == 7:
        print("")
    if counter == 13:
        print("")
        counter = 0
