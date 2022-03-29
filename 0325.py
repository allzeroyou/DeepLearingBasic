import numpy as np
import math



# A = np.array([[1,2],[3,4]])
# print(A.shape)  # 행렬 구조(?행?열)

# B = np.array([[5,6],[7,8]])
# print(B.shape)

# print(np.dot(A, B)) # 행렬의 곱

# # 2 x 3 행렬와 3 x 2 행렬의 곱 계산
# C = np.array([[1,2,3],[4,5,6]])
# print(C.shape)
# D = np.array([[1,2],[3,4],[5,6]])
# print(D.shape)

# print(np.dot(C, D))

# # 다음 코드의 문제점은?
# print(C.shape)

# E = np.array([[1,2],[3,4]])
# print(E.shape)

# print(np.dot(C, E))

# # 2 x 3 행렬과 2 x 2 행렬의 곱 계산으로 오류 발생

# a1 노드 계산의 파이썬 구현
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X, W1)+B1
print(A1)

def sigmoid(x):
    return 1 / (1 + math.e ** -x)

Z1 = sigmoid(A1) # 활성화함수
print(Z1)

# 1층 => 2층 신호전달 구현
W2 = np.array([[0.1, 0.4],[0.2, 0.5],[0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape) # (3, )
print(W2.shape) # (3, 2)
print(B2.shape) # (2, )

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

# 2층 => 출력층 신호전달 구현
def idenity_function(x):
  return x

W3 = np.array([[0.1, 0.3],[0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = idenity_function(A3) # or Y = A3 도 같은 결과
print(Y)

