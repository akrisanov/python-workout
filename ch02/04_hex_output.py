def hex_output(hexnum: str) -> int:
    decnum = 0
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16**power)
    return decnum


if __name__ == "__main__":
    hexnum = input("Enter a hex number to convert: ")
    print(hex_output(hexnum))
