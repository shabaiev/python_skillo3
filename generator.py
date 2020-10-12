def square_nums():
    i = 0
    while True:
        yield i ** 2
        i += 1


my_gen = square_nums()


