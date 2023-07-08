import hashlib

def main():
    password = ''
    with open('input.txt', 'r') as file:
        door_id = file.readline().rstrip()
    index = 0
    while len(password) < 8:
        current_id = door_id + str(index)
        hashed_id = hashlib.md5(current_id.encode()).hexdigest()
        if hashed_id[:5] == '00000':
            password += hashed_id[5]
        index += 1
    print(f'Password: {password}')

if __name__ == '__main__':
    main()
