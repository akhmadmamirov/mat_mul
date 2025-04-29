import random

def build_matrix(rows, cols):
  low = 0
  high = 10
  return [[random.randint(low, high) for _ in range(cols)] for _ in range(rows)]
