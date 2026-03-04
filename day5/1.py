import sys


input = sys.stdin.read().strip().split("\n")[::-1]
output = 0

print(input)

for i, char in enumerate(input):
    if char == "O":
        print("adding", 2**i)
        output += 2**i

print(output)
