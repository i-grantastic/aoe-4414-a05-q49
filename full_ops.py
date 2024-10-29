# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
#   determines the output shape and operation count of a fully-connected layer

# Parameters:
#   c_in: input channel count
#   n_wv: number of weight vectors

# Output:
#   channel count, height count, width count, number of additions performed,
#   number of multiplications performed, and number of divisions performed
#
# Written by Grant Chapman
# Other contributors: None

# import Python modules
import sys
import math

# initialize script arguments
c_in = float('nan')
w_wv = float('nan')

# parse script arguments
if len(sys.argv) == 3:
  c_in = int(sys.argv[1])
  n_wv = int(sys.argv[2])
else:
  print(\
    'Usage: '\
    'python3 full_ops.py c_in n_wv'\
  )
  exit()

## script below this line

# height of the output map
h_out = 1

# width of the output map
w_out = 1

# number of channels
c_out = n_wv

# total number of multiplications
muls = n_wv*c_in

# total number of additions
adds = n_wv*c_in

# total number of divisions
divs = 0

# print
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))