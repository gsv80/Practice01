import csv
import multiprocessing
import os
import pickle
# import time
import timeit
# import numpy

# "test matrices multiplication according to benchmark operation   С = alpha * ор(А) * ор(В) + beta * С"
#

matrix_A = pickle.load(open("matrix_a.bin", "rb"))
matrix_B = pickle.load(open("matrix_b.bin", "rb"))
matrix_C0 = pickle.load(open("matrix_c0.bin", "rb"))

alpha = 105  # random.randint(0, 101)
beta = 105  # random.randint(0, 101)


def matrix_mul_scalar(matrix, scalar):
    """
    matrix multiplication by scalar value
    :param matrix: matrix with any size
    :param scalar: positive integer
    :return: new matrix
    """
    matrix_scal = [[matrix[i][j] * scalar for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return matrix_scal


def matrices_mul(matrix_a, matrix_b):
    """
    multiply two matrices from parameters matrix_a and matrix_b
    :param matrix_a: matrix with size M x K
    :param matrix_b: matrix with size P x N
    :return: new matrix_c with size M x N as result of multiplication
    """
    # alternative MMUL through _zip_

    # zip_b = zip(*matrix_b)
    # zip_b = list(zip_b)
    # return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
    #          for col_b in zip_b] for row_a in matrix_a]

    # iterate through rows of matrix_a
    matrix_c = [[0 for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        # iterate through columns of matrix_b
        for j in range(len(matrix_b[0])):
            # iterate through rows of matrix_b
            for k in range(len(matrix_b)):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return matrix_c


def matrix_trans(matrix):
    """Transposition initial matrix
    :param matrix:
    :return: matrix T
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrices_sum(matrix_a, matrix_b):
    """
    Summarize two matrices with the same size
    :param matrix_a:
    :param matrix_b:
    :return: a new matrix_c as sum of received matrices in parameters
    """
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a))] for i in range(len(matrix_a[0]))]


def test_matrices_mul():
    text_test = "Test matrices multiplication:"
    matrix_test1 = [[1, 2],
                    [3, 4],
                    [5, 1]]
    matrix_test2 = [[1, 2, 3],
                    [2, 1, 1]]
    return f"{text_test} passed" if \
        matrices_mul(matrix_test1, matrix_test2) == [[5, 4, 5],
                                                     [11, 10, 13],
                                                     [7, 11, 16]] \
        else f"{text_test} failed"


def test_matrix_mul_scalar():
    text_test = "Test matrix multiplication by scalar:"
    matrix_test1 = [[1, 3, 4], [1, 5, 6]]
    scalar_test = 4
    return f"{text_test} passed" if \
        matrix_mul_scalar(matrix_test1, scalar_test) == [[4, 12, 16],
                                                         [4, 20, 24]] \
        else f"{text_test} failed"


def test_matrix_trans():
    text_test = "Test matrix transposition:"
    matrix_test2 = [[1, 2], [3, 4], [5, 8]]
    return f"{text_test} passed" \
        if matrix_trans(matrix_test2) == [[1, 3, 5],
                                          [2, 4, 8]] \
        else f"{text_test} failed"


def separate_mult(data):
    """
    dividing matrices multiplication by quantity of processors for parallel count
    :param data:
    :return: part of resulting matrix after counting
    """
    row, matrix_a, matrix_b = data
    res = [0 for row in range(len(matrix_a))]
    for column in range(len(matrix_b[0])):
        for i in range(len(matrix_b)):
            res[column] += matrix_a[row][i] * matrix_b[i][column]
    return res


#
def mmul_multiprocessors(matrix_a, matrix_b, threads):
    rows_a = len(matrix_a)
    with multiprocessing.Pool(threads) as pool:
        res = []
        data = [(row, matrix_a, matrix_b) for row in range(rows_a)]
        for row in pool.map(separate_mult, data):
            res.append(row)
    return res


def test_mmul_multiprocessors():
    text_test = "Test matrices multiplication with multiprocessing:"
    matrix_test1 = [[1, 2],
                    [3, 4],
                    [5, 1]]
    matrix_test2 = [[1, 2, 3],
                    [2, 1, 1]]
    return f"{text_test} passed" if \
        mmul_multiprocessors(matrix_test1, matrix_test2, 8) == [[5, 4, 5],
                                                                [11, 10, 13],
                                                                [7, 11, 16]] \
        else f"{text_test} failed"


# print("A matrix", matrix_A)
# print("B matrix", matrix_B)
# print("C matrix", matrix_C0)

matrix_test1 = [[1, 2],
                [3, 4],
                [5, 1]]
matrix_test2 = [[1, 2, 3],
                [2, 1, 1]]

if __name__ == "__main__":
    print(test_matrix_mul_scalar())
    print(test_matrices_mul())
    print(test_matrix_trans())
    print(test_mmul_multiprocessors())

    # print("Number of cpu : ", multiprocessing.cpu_count())

    # result = timeit.repeat(lambda: matrices_sum(matrix_mul_scalar(matrices_mul(matrix_A, matrix_B), alpha),
    #                                             matrix_mul_scalar(matrix_C0, beta)), number=10)
    result = timeit.repeat(lambda: matrices_sum(matrix_mul_scalar(mmul_multiprocessors(matrix_A, matrix_B, 4), alpha),
                                                matrix_mul_scalar(matrix_C0, beta))
                           , number=10)

    print(f"Time taken is {result} sec ")
    filename = "research_multiproc_x4_log.csv"
    num = 0

    if os.path.exists(filename):
        with open(filename, "a", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
            writer.writerow([f"test# {num}", len(matrix_A), type(matrix_A[0][0]), result])

    else:
        with open(filename, "a", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
            writer.writerow(["test#", "matrix size", "value type", "test_time"])
