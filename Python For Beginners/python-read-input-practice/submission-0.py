def add_two_numbers() -> int:
    inp = input()
    ls = list(map(int, inp.split(",")))
    return ls[0]+ls[1]


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
