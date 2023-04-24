import random
import pickle
import numpy as np

m = int(input("Enter matrix A size one: "))
n = int(input("Enter matrix A size two: "))
k = int(input("Enter matrix B size one: "))
values_type = input("Enter values type in matrix - 'int' or 'double': ")

if values_type == "int":
    matrix_A = [[random.randint(1, 100) for j in range(n)] for i in range(m)]
    matrix_B = [[random.randint(1, 100) for j in range(k)] for i in range(n)]
    matrix_C0 = [[random.randint(1, 100) for j in range(k)] for i in range(m)]
else:
    matrix_A = [[np.double(np.random.rand()) for j in range(n)] for i in range(m)]
    matrix_B = [[np.double(np.random.rand()) for j in range(k)] for i in range(n)]
    matrix_C0 = [[np.double(np.random.rand()) for j in range(k)] for i in range(m)]


# print("Matrix A", matrix_A)
# print("Matrix B", matrix_B)

pickle.dump(matrix_A, open("matrix_a.bin", "wb"))
pickle.dump(matrix_B, open("matrix_b.bin", "wb"))
pickle.dump(matrix_C0, open("matrix_c0.bin", "wb"))

