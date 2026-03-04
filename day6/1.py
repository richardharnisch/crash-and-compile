import sys


input = [int(i) for i in sys.stdin.read().strip().split("\n")]
highest = max(*input)
print(highest)
rolls = len(input)

probs = []


def e(arr):
    return arr[1]


for die_size in range(highest, 21):
    # we need p of s given d
    p_d = (1 / 20) ** rolls
    p_s = 1 / 20
    p_d_given_s = (1 / die_size) ** rolls

    p_s_given_d = (p_d_given_s * p_s) / p_d

    probs.append([die_size, p_s_given_d])

probs.sort(key=e)

print(probs)
