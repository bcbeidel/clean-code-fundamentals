def get_reciprocal(x):
    if x == 0:
        return None
    return 1 / x

def double_a_number(x):
    return 2 * x

def pass_a_number(x):
    return x

def manipulate_number(x):
    reciprocal = get_reciprocal(x)
    another_step = pass_a_number(reciprocal)
    double_reciprocal = double_a_number(another_step)

    return double_reciprocal

if __name__ == "__main__":
    print(manipulate_number(2))
    print(manipulate_number(-2))
    print(manipulate_number(0))
