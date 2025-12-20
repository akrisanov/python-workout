def mysum(*nums: float) -> float:
    result = 0.0
    for num in nums:
        result += num
    return result


if __name__ == "__main__":
    print(mysum(*[1, 2, 3]))
