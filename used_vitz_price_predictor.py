from io import StringIO

data = """
model_year, kms_driven, price,
2014, 39_000, 1_430_000,
2003, 69_000, 1_150_000,
2006, 200_000, 730_000,
2010, 40_000, 1_250_000,
2000, 250_000, 765_000,
"""

# Arbitrary sets of coefficients.
coefficients = [
    [1, 2],
    [2, 2],
    [2, 3],
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
