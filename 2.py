for x in 0,1:
  for y in 0,1:
    for z in 0,1:
      for w in 0,1:
        F = ((x <= y) == (z and w)) and (x <= z)
        if F == 1:
          print(y,z,x,w)

# 0 X 0 X
# X X X 0
# 0 X X 0

# 0 0 0 0
# 1 0 0 0
# 0 1 1 0