def main():
    # define powered-off grid [50x6]
    grid = [['.' for x in range(50)] for y in range(6)]
    # while file is open:
    with open('input.txt', 'r') as file:
        # for line in file:
        for line in file.readlines():
            # parse line into split instructions
            instructions = line.rstrip().split()
            print(instructions)
            # call function depending on first elem in instructions, pass rest of list as args
            if instructions[0] == 'rect':
                rect(grid, instructions[1:])
            elif instructions[0] == 'rotate':
                rotate(grid, instructions[1:])
    # print screen
    display_grid(grid)

def rect(grid, instructions):
    # set A to instructions[0]
    a = int(instructions[0][0])
    # set B to instructions[2]
    b = int(instructions[0][2])
    # for row:
    for i in range(b):
        # for point in row:
        for j in range(a):
            # set grid pixel to '#' (on) at index pos
            grid[i][j] = '#'

def rotate(grid, instructions):
    a = int(instructions[1][2])
    b = int(instructions[3])
    # for count in B:
    for x in range(b):
        if instructions[0] == 'row':
            for i in range(len(grid[a]), 0, -1):
                cur, nxt = i % 50, (i + 1) % 50
                tmp = grid[a][nxt]
                grid[a][nxt] = grid[a][cur]
                grid[a][cur] = tmp
        if instructions[0] == 'column':
            for i in range(len(grid), 0, -1):
                cur, nxt = i % 6, (i + 1) % 6
                tmp = grid[nxt][a]
                grid[nxt][a] = grid[cur][a]
                grid[cur][a] = tmp

def display_grid(grid):
    for line in grid:
        print(''.join(line))

if __name__ == '__main__':
    main()
