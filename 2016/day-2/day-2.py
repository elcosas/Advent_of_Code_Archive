def main():
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    input_map = {
        'U': [0, -1],
        'D': [0, 1],
        'L': [-1, 0],
        'R': [1, 0]
    }
    pos = [1, 1] # start at '5' (middle)
    code = ''
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.rstrip()
            for sym in line:
                pos = [a + b for a, b in zip(pos, input_map[sym])]
                pos = [max(0, min(x, 2)) for x in pos]
            digit = keypad[pos[1]][pos[0]]
            code += str(digit)
    print(f'Code: {code}')

if __name__ == '__main__':
    main()
