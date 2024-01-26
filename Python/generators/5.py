def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

def main():
    try:
        n = int(input())
        countdown = countdown_generator(n)
        print(f"Countdown from {n} to 0: {', '.join(map(str, countdown))}")
    except ValueError:
        print("Please enter a valid integer for n.")

if __name__ == "__main__":
    main()