# Memory profiling
import tracemalloc
from mat_mul import mat_mul
from matrix_500x500 import matrix

# Start memory profiling
tracemalloc.start()

mat_mul(matrix, matrix)
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
# Stop memory profiling
tracemalloc.stop()
