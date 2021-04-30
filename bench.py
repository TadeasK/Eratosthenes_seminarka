import main
from timeit import repeat

n_values = [
    20,
    50,
    100,
    500,
    1_000,
    10_000,
    100_000,
    1_000_000,
    10_000_000,
    100_000_000,
]


for n in n_values:
    time = min(repeat("main.Esieve(n)", number=1, repeat=5, globals=globals()))
    print(f"Při hledání prvočísel do {n} je čas:\t\t {time: .7f}s")

print("Benchmarking finished.")



