def Esieve(n):
    n += 1
    sieve = [True] * n

    for i in range(2, n):
        if sieve[i]:
            for j in range(i ** 2, n, i):
                sieve[j] = False

    primes = []
    for i in range(2, n):
        if sieve[i]:
            primes.append(i)
    return primes