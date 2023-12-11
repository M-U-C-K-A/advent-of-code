def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, "r") as f:
        for line in f:
            if line.count("#") == 0:
                for _ in range(2):
                    matrix.append([char for char in line.replace("\n", "")])
            else:
                matrix.append([char for char in line.replace("\n", "")])

    matrix = [list(x) for x in zip(*matrix)]
    return matrix

def calculate_part1(matrix):
    mat = []
    for line in matrix:
        if line.count("#") == 0:
            for _ in range(2):
                mat.append(line)
        else:
            mat.append(line)

    locs = [(i, j) for i in range(len(mat)) for j in range(len(mat[i])) if mat[i][j] == "#"]

    res = 0
    done = set()

    for a in locs:
        for b in locs:
            if (a, b) not in done and (b, a) not in done and a != b:
                done.add((a, b))
                res += (max(a[0], b[0]) - min(a[0], b[0])) + (max(a[1], b[1]) - min(a[1], b[1]))

    print("PART 1:", res)

def sig(a):
    return 0 if a == 0 else int(a / abs(a))

def dist(a, b, mat):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    x = [mat[i][a[1]] for i in range(a[0] + sig(dx), b[0], sig(dx))] if dx != 0 else []
    y = [mat[a[0]][i] for i in range(a[1] + sig(dy), b[1], sig(dy))] if dy != 0 else []

    return x.count("E") * 1000000 + len(x) - x.count("E") + y.count("E") * 1000000 + len(y) - y.count("E")

def calculate_part2(matrix):
    mat = [["E" if char != "#" else char for char in line] for line in matrix]

    locs = [(i, j) for i in range(len(mat)) for j in range(len(mat[i])) if mat[i][j] == "#"]

    res = 0
    done = set()

    for a in locs:
        for b in locs:
            if (a, b) not in done and (b, a) not in done and a != b:
                done.add((a, b))
                res += dist(a, b, mat)

    print('PART 2:', res)

if __name__ == "__main__":
    input_file_path = "input.txt"
    matrix = read_matrix_from_file(input_file_path)
    calculate_part1(matrix)
    calculate_part2(matrix)
