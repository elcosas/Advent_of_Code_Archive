def main():
    message = ''
    lines = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            lines.append(line.rstrip())
    for i in range(len(lines[0])):
        instances = {}
        for j in range(len(lines)):
            char = lines[j][i]
            instances[char] = instances.setdefault(char, 0) + 1
        message += max(instances.keys(), key=lambda x: instances[x])
    print(f'Message: {message}')

if __name__ == '__main__':
    main()
