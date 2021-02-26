
import re

"""
1-3 a: abcde  -- means must contain a at least once and up to three times
1-3 b: cdefg  -- means must contain b at least once and up to three times
2-9 c: ccccccccc  -- means must contain c at least twice and up to nine times
"""

def day2():
    part_one, part_two = 0, 0
    for l in passwords:
        (start, end, letter, password) = re.split(r'[-: ]+', l)
        if int(start) <= password.count(letter) <= int(end):
            part_one += 1
        letters = {password[int(k) - 1] for k in (start, end)}
        if len(letters) == 2 and letter in letters:
            part_two += 1
    print((part_one, part_two))


if __name__ == "__main__":
    day2()
