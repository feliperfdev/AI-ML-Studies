import random

random.seed(42) 
for _ in range(2000):
    entry1 = random.randint(387, 487)
    entry2 = random.randint(387, 487)
    print(f"{entry1},{entry2}")