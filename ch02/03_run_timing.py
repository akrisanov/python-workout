def run_timing() -> tuple[float, int]:
    total = 0.0
    runs = 0

    while run := input("Enter 10 km run time: "):
        try:
            total += float(run)
            runs += 1
        except ValueError:
            print("Please enter a number")
            continue

    if runs == 0:
        return 0.0, 0

    avg_time = total / runs
    return avg_time, runs


if __name__ == "__main__":
    avg_time, runs = run_timing()
    print(f"Average of {avg_time:.2f}, over {runs} runs")
