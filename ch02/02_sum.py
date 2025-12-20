from collections.abc import Iterable, Sequence


def mysum(nums: Iterable[float], start: float = 0.0) -> float:
    result = float(start)
    for num in nums:
        result += num
    return result


def avg(nums: Sequence[float]) -> float:
    return mysum(nums) / len(nums)


if __name__ == "__main__":
    print(mysum([], 15))
    print(mysum([1, 2, 3], 10))
    print(mysum((15, 15, 24)))
    print(avg([10, 10, 10]))
