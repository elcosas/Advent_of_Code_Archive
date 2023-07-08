def main():
    ip_count = 0
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.rstrip()
            hypernet = line[line.find('['):line.find(']') + 1]
            sections = line.partition(hypernet)
            if is_abba(hypernet):
                continue
            if is_abba(sections[0]) or is_abba(sections[2]):
                ip_count += 1
    print(f'Valid IP addresses: {ip_count}')

def is_abba(section):
    i = 0
    while i + 4 <= len(section):
        pair = section[i] + section[i + 1]
        if pair[0] == pair[1]:
            i += 1
            continue 
        if section[i + 2] + section[i + 3] == pair[::-1]:
            return True
        i += 1
    return False

if __name__ == '__main__':
    main()
