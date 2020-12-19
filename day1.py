
def day1(numbers, target):
    for i, number in enumerate(numbers[:-1]):
        complement = target - number
        if complement in numbers[i+1:]:
            print("Solution: {} and {}; product = {}".format(number, complement, number*complement))
            break
    else:  # note 3
        raise ValueError("No solutions exist")
        
if __name__ == "__main__":
    subset_sum([...],2020)
