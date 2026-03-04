import sys


input = sys.stdin.read().strip().split("\n")
input = [line.split(" ") for line in input]
pairs = []


def letter_number(letters: str) -> int:
    out = 0
    for i, letter in enumerate(letters[::-1]):
        out += (1 + ord(letter) - ord("A")) * (26 ** (i))
    return out


for pair in input:
    out_pair = []
    for coord in pair:
        out_coord = ["", ""]
        for char in coord:
            if char in "0123456789":
                out_coord[1] += char
            else:
                out_coord[0] += char
        out_pair.append(
            [
                letter_number(out_coord[0]),
                int(out_coord[1]),
            ]
        )
    pairs.append(out_pair)


new_pairs = []

output = 0

for pair in pairs:
    moves = 0
    dist = [pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]]
    while abs(dist[0]) > 4 or abs(dist[1]) > 4:
        # print("dist before step:", dist)
        x_dir = 1 if dist[0] <= 0 else -1
        y_dir = 1 if dist[1] <= 0 else -1
        if abs(dist[0]) > abs(dist[1]):
            dist[0] += 2 * x_dir
            dist[1] += y_dir
        else:
            dist[1] += 2 * y_dir
            dist[0] += x_dir
        # print("dist after step:", dist)
        moves += 1
    # print(dist)
    dist = [abs(d) for d in dist]
    x, y = dist if dist[0] > dist[1] else dist[::-1]
    dis = x, y
    if dis == (1, 0):
        moves += 3
    elif dis == (2, 0):
        moves += 2
    elif dis == (3, 0):
        moves += 3
    elif dis == (4, 0):
        moves += 2
    elif dis == (1, 1):
        moves += 2
    elif dis == (2, 1):
        moves += 1
    elif dis == (2, 2):
        moves += 4
    elif dis == (3, 1):
        moves += 2
    elif dis == (3, 2):
        moves += 3
    elif dis == (3, 3):
        moves += 2
    elif dis == (4, 1):
        moves += 3
    elif dis == (4, 2):
        moves += 2
    elif dis == (4, 3):
        moves += 3
    elif dis == (4, 4):
        moves += 4
    elif dis == (0, 0):
        pass
    else:
        raise ValueError(f"Unexpected coords: {dis}")

    output += moves

print(output)
