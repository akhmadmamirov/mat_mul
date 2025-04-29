from built_mat import build_matrix
from matrix_500x500 import matrix

def mat_mul(matix_a, matrix_b):
  rows_a, cols_a = len(matix_a), len(matix_a[0])
  rows_b, cols_b = len(matrix_b), len(matrix_b[0])
  if cols_a != rows_b:
    raise ValueError("Number of columns in matrix A must be equal to number of rows in matrix B")

  res = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
  for i in range(rows_a):
    for j in range(cols_b):
      for k in range(cols_a):
        res[i][j] += matix_a[i][k] * matrix_b[k][j]
  return res

# matrix_a = build_matrix(500, 500)
# matrix_b = build_matrix(500, 500)
mat_mul(matrix, matrix)


