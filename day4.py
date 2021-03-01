import re

with open('day_four.txt') as f:
    data = f.read().split('\n\n')
    data = [dict(entry.split(':') for entry in item.split()) for item in data]


def day4a(passwords):
    keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    print(sum(not keys - i.keys() for i in passwords))


def day4b(passwords):
    valid_count = 0
    keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for i in passwords:
        valid_count += \
            not keys - i.keys() and \
            all((1920 <= int(i['byr']) <= 2002,
                 2010 <= int(i['iyr']) <= 2020,
                 2020 <= int(i['eyr']) <= 2030,
                 (i['hgt'].endswith('cm') and 150 <= int(i['hgt'][:-2]) <= 193) or
                 (i['hgt'].endswith('in') and 59 <= int(i['hgt'][:-2]) <= 76),
                 re.match(r'^#[\da-f]{6}$', i['hcl']),
                 i['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                 re.match(r'^\d{9}$', i['pid'])))
    print(valid_count)


if __name__ == '__main__':
    day4a(data)
    day4b(data)
