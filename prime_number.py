import time
import math

def get_prime1(num) :
    if num == 1 :
        return False
    if num == 2 :
        return True
    for i in range (2, num) :
        if num % i == 0 :
            return False
    return True

def get_prime2(num) :
    if num == 1 :
        return False
    if num == 2 :
        return True
    for i in range (2, int(math.sqrt(num))) :
        if num % i == 0 :
            return False
    return True

number = int(input("Enter a number: "))
prime_number = []

start = time.time()
for i in range (1, number + 1) :
    if get_prime1(i) :
        prime_number.append(i)

end = time.time()
print(end - start)
# print(prime_number)

start = time.time()
for i in range (1, number + 1) :
    if get_prime2(i) :
        prime_number.append(i)

end = time.time()
print(end - start)
# print(prime_number)