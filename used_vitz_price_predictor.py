from io import StringIO
from random import randint

data = """
model_year, kms_driven, price,
2014, 39_000, 1_430_000,
2003, 69_000, 1_150_000,
2006, 200_000, 730_000,
2010, 40_000, 1_250_000,
2000, 250_000, 765_000,
"""

# Arbitrary sets of coefficients.
coefficient_sets = [
    [randint(10, 20), randint(5, 20)],
    [randint(10, 20), randint(5, 20)],
    [randint(10, 20), randint(5, 20)],
]

# Read in data.
file = StringIO(data)
data_samples = []

for sample in file:
    listed_sample = sample.split(",")
    # Remove new line.
    del listed_sample[-1]
    data_samples.append(listed_sample)

# Remove headers.
del data_samples[0]
del data_samples[0]

# Create a list of actual prices.
actual_prices = []
for data_sample in data_samples:
    actual_prices.append(int(data_sample[-1]))

# Calculate mean squares.
mean_squares = []
for coefficient_set in coefficient_sets:
    predicted_prices = []
    # Calculate predicted prices.
    for data_sample in data_samples:
        predicted_prices.append((coefficient_set[0] * int(data_sample[0])) +
                                (coefficient_set[1] * int(data_sample[1])))
    # Find difference between predicted prices and actual prices.
    zip_object = zip(predicted_prices, actual_prices)
    differences = [predicted_price - actual_price
                   for predicted_price, actual_price in zip_object]
    differences_squared = [difference ** 2 for difference in differences]
    mean_squares.append(sum(differences_squared))

# Find the least mean square and its corresponding set of coefficients.
least_mean_square = min(mean_squares)
best_coefficient_set = coefficient_sets[
    mean_squares.index(least_mean_square)]

print(f"The best least mean square found in this session with the current "
      f"set parameters for random coefficients is {least_mean_square}.")
print(f"The set of coefficients to obtain this least mean square is "
      f"{best_coefficient_set}.")
print(f"The predicted prices from this coefficient set are: "
      f"Stay tuned for the predicted prices after I refactor my code!")
print(f"The actual prices are {actual_prices}.")
