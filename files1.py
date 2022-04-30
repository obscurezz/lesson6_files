with open('miles.txt') as miles_file:
    try:
        with open('kilometers.txt', 'a') as kilometers_file:
            for line in miles_file.readlines():
                kilometers_file.write(f'{round(float(line) * 1.60934, 2)}\n')
    except FileNotFoundError:
        print(f'File {kilometers_file} not found')
