def step_function(x):
  if x> 0:
    return 1
  else:
    return 0

import numpy as np
x = np.array([-1.0, 1.0, 2.0])
y = x>0
print(y)

B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(np.ndim(B))
print(B.shape)

A = np.array([[1,2],[3,4]])
print(A.shape)
B = np.array([[5,6],[7,8]])
print(B.shape)
print(np.dot(A,B)) # dot: 행렬에서의 곱 표현

A = np.array([[1,2,3],[4,5,6]])
print(A.shape)
B = np.array([[1,2], [3,4], [5,6]])
print(B.shape)
print(np.dot(A, B))

