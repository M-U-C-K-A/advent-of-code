with open('input.txt', 'r') as fichier:
    mtrx = [list(ligne.strip()) for ligne in fichier]

def get_pipe(xy_tuple):
    """ the mind makes it real """
    x, y = xy_tuple
    return mtrx[y][x]

def new_pos(pos, dir):
    """
    it is not the spoon that bends
    it's only yourself
    """
    return tuple(a + b for a, b in zip(pos, dir))


# reach for the red pill
for y, line in enumerate(mtrx):
    if 'S' in line:
        x = line.index('S')
        break
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# current previous move
# |       DOWN     DOWN
# |       UP       UP
# ...
moves = {
    ('|', DOWN): DOWN,
    ('|', UP): UP,
    ('-', RIGHT): RIGHT,
    ('-', LEFT): LEFT,
    ('L', LEFT): UP,
    ('L', DOWN): RIGHT,
    ('J', RIGHT): UP,
    ('J', DOWN): LEFT,
    ('7', RIGHT): DOWN,
    ('7', UP): LEFT,
    ('F', LEFT): DOWN,
    ('F', UP): RIGHT
}

start_pos = (x, y)
start_pipe = '|'
start_dir = DOWN

cur = start_pipe
dir = start_dir
posses = [start_pos]

pos = start_pos

while True:
    dir = moves[(cur, dir)]
    pos = new_pos(pos, dir)
    if pos == start_pos:
        break
    cur = get_pipe(pos)
    posses.append(pos)

print('Part 1:', len(posses) // 2)


# Part 2

mtrx[start_pos[1]][start_pos[0]] = start_pipe
insiders = []

for y in range(len(mtrx)):
    for x in range(len(mtrx[0])):
        if not (x, y) in posses:
            mtrx[y][x] = '.'

for y, line in enumerate(mtrx):
    in_simulated_reality = False
    for x, c in enumerate(line):
        # - flip simulated reality at |, J and L
        if c == '|' or c == 'J' or c == 'L':
            in_simulated_reality = not in_simulated_reality
        elif c == '.' and in_simulated_reality:
            mtrx[y][x] = 'I'
            insiders.append((x, y))


print('Part 2:', len(insiders))