def day1A(numbers, target):
    for i, number in enumerate(numbers[:-1]):
        complement = target - number
        if complement in numbers[i+1:]:
            print("Solution: {} and {}; product = {}".format(number, complement, number*complement))
            break
    else:
        raise ValueError("No solutions exist")


def day1B(number_list, numbers_len, target):
    for i in range(0, numbers_len - 2):

        for j in range(i + 1, numbers_len - 1):

            for k in range(j + 1, numbers_len):
                if number_list[i] + number_list[j] + number_list[k] == target:
                    print("Solution: ", number_list[i],
                          ",", number_list[j], ",", number_list[k])
                    print("Product = ", number_list[i] * number_list[j] * number_list[k])
                    return True

    return False


if __name__ == "__main__":
    day1A(numbers,2020)
    day1B(numbers, len(numbers), 2020)
