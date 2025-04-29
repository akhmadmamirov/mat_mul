import time
import py_compile
import timeit
from mat_mul import mat_mul, build_matrix

start_time = time.time()
py_compile.compile('mat_mul.py')
end_time = time.time()

compilation_time = end_time - start_time

# Run-time benchmark
matrix_a = build_matrix(500, 500)
matrix_b = build_matrix(500, 500)
execution_time = timeit.timeit(lambda: mat_mul(matrix_a, matrix_b), number=5)

print(f"Execution time: {execution_time:.6f} seconds")
print(f"Compilation time: {compilation_time:.6f} seconds")


