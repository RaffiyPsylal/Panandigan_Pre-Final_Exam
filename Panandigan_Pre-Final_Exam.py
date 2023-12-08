def prime1(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes2(start, end):
    prime = [n for n in range(start, end + 1) if prime1(n)]
    return prime

def main1():
    while True:
        start = int(input("Enter the start number: "))

        if start < 0:
            print("Enter a non-negative number.")
            continue

        if start == 0:
            break

        end = int(input("Enter the end number: "))

        if end == 0:
            break

        if end <= start:
            print("Enter a number greater than", start)
            continue

        num = primes2(start, end)

        print(f'The Prime number between {start} and {end} are: ')
        for prime in num:
            print(prime)

if __name__ == "__main__":
   main1()