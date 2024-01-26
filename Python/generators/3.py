def divisible_by_three_and_four_generator(n):
    return (num for num in range(n + 1) if num % 3 == 0 and num % 4 == 0)

def main():
    try:
        n = int(input())
        divisible_numbers = divisible_by_three_and_four_generator(n)
        print(f"Numbers between 0 and {n} divisible by both 3 and 4: {', '.join(map(str, divisible_numbers))}")
    except ValueError:
        print("Please enter a valid integer for n.")

if __name__ == "__main__":
    main()