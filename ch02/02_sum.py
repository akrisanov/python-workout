from collections.abc import Iterable


def mysum(nums: Iterable[float], start: float = 0.0) -> float:
    result = float(start)
    for num in nums:
        result += num
    return result


if __name__ == "__main__":
    print(mysum([], 15))
    print(mysum([1, 2, 3], 10))
    print(mysum((15, 15, 24)))
