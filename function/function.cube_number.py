def cube(n):
    return n*n*n


def by_three(n):
    if n%3==0:
        return cube(n)
    else:
        return "False"

print(by_three(8))

