from typing import List

def read_integers() -> List[int]:
    inp_str = input()
    num_list = list(map(int, inp_str.split(",")))
    return num_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
