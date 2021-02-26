with open('day_three.txt') as f:
    data = f.read().split()


def day3a(xn, yn):
    count1 = 0
    for x in range(0, len(data), xn):
        y = int(x*yn/xn) % len(data[0])
        count1 += data[x][y] == '#'
    return count1


print(day3a(1, 3))


def day3b(slopes):
    count2 = 1
    for x, y in slopes:
        count2 *= (day3a(x, y))
    print(count2)


if __name__ == '__main__':
    day3b([[1,1], [1,3], [1,5], [1,7], [2,1]])
