import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("1D Array:")
print(arr_1d)

print("\n2D Array:")
print(arr_2d)

print("\nIndexing:")
print("First element of 1D array:", arr_1d[0])
print("Element at row 1, column 2 of 2D array:", arr_2d[1, 2])

print("\nSlicing:")
print("First three elements of 1D array:", arr_1d[:3])
print("First row of 2D array:", arr_2d[0, :])


reshaped_array = arr_1d.reshape(5, 1)
print("\nReshaped 1D array to 2D (5x1):")
print(reshaped_array)

#Manual Multiplication without np.dot
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result_manual = np.zeros((A.shape[0], B.shape[1]))

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            result_manual[i][j] += A[i][k] * B[k][j]

print("\nManual Matrix Multiplication Result:")
print(result_manual)

#Multiplication np.dot
result_numpy = np.dot(A, B)

print("\nMatrix Multiplication using np.dot:")
print(result_numpy)
