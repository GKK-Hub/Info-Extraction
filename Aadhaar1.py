with open("customers.txt") as f:
    for line in f:
        print(line)
        print(type(line))
        break