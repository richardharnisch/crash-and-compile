import sys


input = sys.stdin.read().strip().split("\n")
output = 0

for line in input:
    number = 0
    total = 0
    for char in line:
        if char in "0123456789":
            number *= 10
            number += ord(char) - ord("0")
        else:
            total += number
            number = 0
    total += number
    output += total

print(output)
