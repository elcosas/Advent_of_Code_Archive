def main():
    # define file_len
    file_len = 0
    # with file open:
    with open('input.txt', 'r') as file:
        # for line in file:
        for line in file.readlines():
            # define decompressed line
            decompressed = ''
            # for index in line:
            i = 0
            while i < len(line.rstrip()):
                # if char is '[':
                if line[i] == '(':
                    # get marker
                    marker = line[i:i+5]
                    size, amount = int(marker[1]), int(marker[3])
                    # get data
                    data = line[i+5:i+5+size]
                    # add repeated data to decompressed line
                    decompressed += data*amount
                    # increment index to end of data
                    i += 5 + size
                # else:
                else:
                    # append char to decompressed line
                    decompressed += line[i]
                    i += 1
            # add length of decompressed line to file_len
            print(f'{decompressed}|{len(decompressed)}')
            file_len += len(decompressed)
    # print file_len
    print(f'Total file length: {file_len}')

if __name__ == '__main__':
    main()
