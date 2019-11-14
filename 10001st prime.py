import math
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True
count = 1
num = 2
while (count < 10001):
    num += 1
    if isPrime(num):
        count += 1
print('The 10001th prime is: ' + str(num))