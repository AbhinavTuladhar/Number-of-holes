from random import randint
import pandas as pd


ROWS = 500
LOWER = 1_000
UPPER = 10_000
numbers = []
holes_mapping = {
    0: 1,
    1: 0,
    2: 0,
    3: 0,
    4: 1,
    5: 0,
    6: 1,
    7: 0,
    8: 2,
    9: 1,
}

# Generate different numbers for the dataset and count the number of holes.
for _ in range(ROWS):
    random_number = randint(LOWER, UPPER)
    hole_count = 0
    for digit in str(random_number):
        hole_count += holes_mapping[int(digit)]
    numbers.append([int(random_number), hole_count])

df = pd.DataFrame(data=numbers, columns=['Number', 'Target'])
df.to_csv('Dataset.csv', index=False)

print("Success!")