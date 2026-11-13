import time
start = time.time()
primes = []
N = int(input("enter the number til which you want to sum the primes"))
for i in range(2, N+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
end = time.time()
print(f"Sum of primes: {sum(primes)}")
print(f"Time taken: {end - start} seconds")