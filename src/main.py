def main():
    start = int(input("Enter the start limit: "))
    end = int(input("Enter the end limit: "))
    divisors = []
    for i in range(start, end):
        if i % 3 == 0 or i % 5 == 0:
            divisors.append(i)
    print("The divisors are: " + str(divisors))
    print("The sum is " + str(sum(divisors)))

if __name__ == "__main__":
    main()
