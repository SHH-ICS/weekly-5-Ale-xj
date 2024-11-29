import sys

def calculate_pi(iterations):
    pi = 0
    for i in range(iterations):
        if i % 2 == 0:
            pi += 4 / (2 * i + 1)
        else:
            pi -= 4 / (2 * i + 1)
    return pi

try:
    iterations = int(input().strip())
    if iterations <= 0:
        raise ValueError
    print(calculate_pi(iterations))
except:
    print("Error")
    sys.exit(1)
