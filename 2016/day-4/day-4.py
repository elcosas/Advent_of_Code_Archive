def main():
    id_sum = 0
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            instances = {}
            checksum = line[line.find('[') + 1:line.find(']')]
            sector_id = int(line[line.rfind('-') + 1:line.find('[')])
            for char in line[:line.rfind('-')]:
                if char.isalpha():
                    instances[char] = instances.setdefault(char, 0) + 1
            sorted_instances = sorted(instances.items(), key=lambda x: (-x[1], x[0])) 
            sorted_keys = ''.join([x[0] for x in sorted_instances])
            if checksum in sorted_keys:
                id_sum += sector_id

    print(f'Sector ID sum: {id_sum}')

if __name__ == '__main__':
    main()
