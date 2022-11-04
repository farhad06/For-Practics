nums = [33, 99, 63, 29, 25, 96, 61, 25, 22, 89, 90, 90]

def odds_test(n):
    n = True if n % 2 == 1 else False
    return n

print(list(filter(odds_test, nums)))