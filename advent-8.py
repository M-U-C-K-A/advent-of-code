from math import lcm
def process_input(data):
    parts = data.strip().split("\n\n")
    mappings = {(directions := line.split("="))[0].strip(): directions[1].strip()[1:-1].split(", ") for line in parts[1].split("\n")}
    return parts[0].replace("L", "0").replace("R", "1"), mappings

def part1(dir_sequence, map):
    len_dir, position, counter = len(dir_sequence), "AAA", 0
    while position != "ZZZ":
        instruction = int(dir_sequence[counter % len_dir])
        counter += 1
        position = map[position][instruction]
    return counter

def part2t2(dir_sequence, map):
    len_dir, counter, destinations = len(dir_sequence), 0, []
    vector = [elem for elem in map if elem.endswith("A")]
    while vector:
        instruction, counter = int(dir_sequence[counter % len_dir]), counter + 1
        new_vector = [map[position][instruction] for position in vector if not map[position][instruction].endswith("Z")]
        if (reached := len(vector)-len(new_vector)) > 0:
            destinations.extend([counter]*reached)
        vector = new_vector
    return lcm(*destinations)

if __name__ == "__main__":
    with open("input.txt", "r") as ifile:
        i_data = ifile.read().strip()
    print("Nr. of steps, \n part 1 : {} \n part 2 : {}".format(part1(*process_input(i_data)), part2t2(*process_input(i_data))))