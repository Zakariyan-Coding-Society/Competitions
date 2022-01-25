from math import ceil 

def solve (n, p):
  return ceil (n / p)

total_pc = int (input ())
pc_per_round = int(input())

print(solve(total_pc, pc_per_round))
