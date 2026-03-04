import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
from utils import *

DEBUG = 0

input = sys.stdin.read().strip().split("\n")

people = int(input.pop(0))

debtors = 0

for person in range(people):
    products = int(input.pop(0).split()[-1])
    s_balance = input.pop(0)
    balance = (
        int(s_balance.split()[0].split(".")[0])
        + int(s_balance.split()[0].split(".")[1]) / 100
    )
    for product in range(products):
        cost = input.pop(0).split()[-2]
        balance -= int(cost.split(".")[0]) + int(cost.split(".")[1]) / 100
    if balance < 0:
        debtors += 1

print(debtors)
