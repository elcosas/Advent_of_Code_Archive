def main():
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    position = [0, 0]
    current_dir = 0
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.rstrip().split(', ')
            for coord in line:
                if coord[0] == 'R':
                    current_dir += 1
                elif coord[0] == 'L':
                    current_dir -= 1
                position[0] += directions[current_dir][0] * int(coord[1])
                position[1] += directions[current_dir][1] * int(coord[1])
    distance = abs(position[0]) + abs(position[1])
    print(f'Distance: {distance}')
            
if __name__ == '__main__':
    main()
