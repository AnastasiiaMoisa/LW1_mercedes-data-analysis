# Lab 1

# TASK 1
# a) Create a program that generates random and non-random arrays in various ways,
# specified in the theoretical information.

import pandas as pd
import numpy as np

n = int(input("Enter the number of elements in the array: "))

print("\nNON-RANDOM arrays\n")

# Array of a given dimension with a step
arr_range = np.arange(1, n + 1)
print(f"Range array (1 to {n}):\n{arr_range}")

# Array of dimension n consisting of integer (1) units
arr_ones = np.ones(n, dtype=int)
print(f"Ones array of {n} elements:\n{arr_ones}")

# Two-dimensional array n*n, floating-point data type
arr_zeros_2d = np.zeros((n, n), dtype=float)
print(f"Zeros {n}x{n} array:\n{arr_zeros_2d}")

# Uniform distribution between 0 and 1 over n number of elements
arr_lin = np.linspace(0, 1, n)
print(f"Linspace array (0 to 1, {n} steps):\n{arr_lin}")

print("\nRANDOM arrays\n")

# Array n*2 of uniformly distributed random numbers from 0 to 1
arr_rand_uni = np.random.random((n, 2))
print(f"Random uniform array ({n} x 2):\n{arr_rand_uni}")

# Array n*(n*2) of normally distributed random numbers
# (mathematical expectation is 1, standard deviation is 10)
arr_rand_norm = np.random.normal(1, 10, size=(n, n * 2))
print(f"Random normal array (mean=1, std=10, size={n}*({n}*2) ):\n{arr_rand_norm}")

# Array of n*n random integers from 0 to n**2.
arr_rand_int = np.random.randint(0, n**2, (n, n))
print(f"Random Integers {n}x{n}:\n{arr_rand_int} \n")


# b) Demonstration of accessing array elements using indices, including negative ones;
# highlighting subarrays of both one-dimensional and multidimensional arrays.

print("INDEXING and SLICING\n")
print(f"Second element of range array: {arr_range[1]}")
print(f"Reversed linspace array: {arr_lin[::-1]}")
print(f"Last element of first row in random uniform array: {arr_rand_uni[0, -1]}")

print(f"First row of random integers array: {arr_rand_int[0, :]}")
print(f"Third column of random integers array: {arr_rand_int[:, 2] if n > 2 else 'N/A'}")
print(f"Top-left 2*2 square of random integers array\n{arr_rand_int[:2, :2]}")
print("Buttom-right 2*2 square of random integers array:\n", arr_rand_int[1:, 1:])

arr_series = pd.Series(['A', 'B', 'C', 'D'], index=[1, 4, 8, 10])
print("\nEXPLICIT INDEXING\n", arr_series.loc[1:4])
print("\nEXPLICIT INDEXING\n", arr_series.iloc[1:4])

# c) Demonstration of basic arithmetic operations on arrays,
# as well as the operation of the reduce, accumulate, outer methods.

print("\nARITHMETIC OPERATIONS\n")
arr_1 = np.random.randint(1, 10, (3, 3))
arr_2 = np.random.randint(1, 5, (3, 3))

print(f"\nMatrix_1:\n {arr_1}")
print(f"\nMatrix_2:\n {arr_2}")

print("\n(-(Matrix_1 + 5) * 0.2) % 2:\n", (-(arr_1 + 5) * 0.2) % 2)
print("\n((Matrix_2 - 1) / 3) ** 2:\n" , ((arr_2 - 1) / 3) ** 2)

print("\nMatrix_1 + Matrix_2:\n", np.add(arr_1, arr_2))
print("\nMatrix_1 - Matrix_2:\n", np.subtract(arr_1, arr_2))
print("\nMatrix_1 * Matrix_2:\n", np.multiply(arr_1, arr_2))
print("\nMatrix_1 / Matrix_2:\n", np.divide(arr_1, arr_2))
print("\nMatrix_1 ** Matrix_2:\n", np.power(arr_1, arr_2))
print("\nMatrix_1 % Matrix_2:\n", np.mod(arr_1, arr_2))
print("\n-Matrix_1:\n", np.negative(arr_1), "\n")


print("Reduce add (+) of ones array and range array:\n", np.add.reduce(arr_1, axis=0)) # the operation goes from top to bottom (collapses rows into one row)
print("Accumulate subtract (-) of ones array and range array:\n", np.subtract.accumulate(arr_2, axis=1)) # the operation goes from left to right (collapses columns into one column)
print("Outer power (**) of ones array and range array:\n", np.power.outer(np.arange(1, 4), np.arange(1, 4)), "\n")


# TASK 2
# FILE OUTPUT settings
pd.set_option('display.max_columns', None) # to output all columns (NONE restrictions)
pd.set_option('display.width', 1000) # to increase the output width so text won't wrap to next row
pd.options.display.float_format = '{:.2f}'.format # format the float numbers output

# READ CSV file
data_frame = pd.read_csv('merc - merc.csv')

# a) Deduce the main statistical characteristics of quantitative characteristics;
print("STATISTICAL VALUES")
stats = data_frame.describe()
numeric_data_frame = data_frame.select_dtypes(include=[np.number])

stats.loc['median'] = numeric_data_frame.median()
stats.loc['var'] = numeric_data_frame.var()
print(stats, '\n')

# b) Find diesel cars with automatic transmission that are cheaper than 15 thousand;
cars = data_frame.query(
    "price < 15000 & transmission == 'Automatic' & fuelType == 'Diesel'" )
print("CARS: ", len(cars))
print(cars, '\n')

# c) Add a new column that contains information about how much of the price is tax.
data_frame['ratio'] = (data_frame['tax']/data_frame['price']) * 100
print(data_frame)

