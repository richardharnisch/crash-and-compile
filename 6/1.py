import sys


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
