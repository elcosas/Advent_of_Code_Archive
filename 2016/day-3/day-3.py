def main():
    possible = 0
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.rstrip().split()
            line = [int(x) for x in line]
            line.sort()
            if (line[0] + line[1]) > line[2]:
                possible += 1
    print(f'Possible triangles: {possible}')

if __name__ == '__main__':
    main()
