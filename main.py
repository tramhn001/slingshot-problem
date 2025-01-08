def hittable_targets(room):
    hits = 0

    for i, row in enumerate(room):
        for j, item in enumerate(row):
            if item == 'A':
                start_loc = (i, j)
    
    # Set r and c to Auberon's location
    r, c = start_loc
    # Search to the right
    while 0 <= r < len(room) and 0 <= c < len(room[0]):
        if room[r][c] == 'T':
            hits += 1
            break
        if room[r][c] == 'W':
            break
        c += 1

    # Search to the left
    r, c = start_loc
    while 0 <= r < len(room) and 0 <= c < len(room[0]):
        if room[r][c] == 'T':
            hits += 1
            break
        if room[r][c] == 'W':
            break
        c -= 1

    # Search up:
    r, c = start_loc
    while 0 <= r < len(room) and 0 <= c < len(room[0]):
        if room[r][c] == 'T':
            hits += 1
            break
        if room[r][c] == 'W':
            break
        r -= 1

    # Search down:
    r, c = start_loc
    while 0 <= r < len(room) and 0 <= c < len(room[0]):
        if room[r][c] == 'T':
            hits += 1
            break
        if room[r][c] == 'W':
            break
        r += 1

    return hits



room1 = [
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]
assert hittable_targets(room1) == 2

room2 = [
    [' ', 'T', ' ', ' '],
    ['T', 'A', 'T', ' '],
    [' ', 'T', ' ', ' '],
]
assert hittable_targets(room2) == 4

room3 = [
    ['T', ' ', 'T'],
    [' ', 'A', ' '],
    ['T', ' ', 'T'],
    [' ', ' ', ' '],
]
assert hittable_targets(room3) == 0

room4 = [
    ['T', 'A', ' ', 'W', ' ', 'T'],
]
assert hittable_targets(room4) == 1

room5 = [
    ['A'],
]
assert hittable_targets(room5) == 0

print("All tests passed!")
print("If time remains, discuss time & space complexity")
