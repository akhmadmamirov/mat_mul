import time
import py_compile


start_time = time.time()
py_compile.compile('mat_mul.py')
end_time = time.time()
compilation_time = end_time - start_time
print(f"Compilation time: {compilation_time:.6f} seconds")