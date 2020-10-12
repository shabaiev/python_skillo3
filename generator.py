def square_nums(n):
    for num in range(n):
        yield num ** 2


mygen = square_nums(1000000)



