def multiplication(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
def main():
    n = int(input("Enter the number for its multiplication: "))
    multiplication(n)
if __name__ == "__main__":
    main()

