# 딥러닝기초-1차과제
# 소프트웨어 20200848 유다영

# 1. 다층 퍼셉트론을 이용해 반가산기 구현
# 입력: 2비트(A, B)
# 출력: 2비트(S, C)

import numpy as np

# AND 게이트 구현하기
def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum(x * w) + b
  if tmp <= 0: 
    return 0
  else:
    return 1 # 임계값을 넘으면 1을 반환 그외에는 0을 반환

# NAND 게이트 구현하기
def NAND(x1, x2):
    X = np.array([x1, x2])
    W = np.array([-0.5, -0.5])
    b = 0.7
    tmp = sum(X * W) + b
    if tmp <= 0:
      return 0 
    else:
       return 1

# OR 게이트 구현하기
def OR(x1,x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = - 0.1
  tmp = np.sum(x * w) + b
  if tmp <= 0:
    return 0
  else:
    return 1

# XOR 게이트 구현하기
def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)
  return y

# 반가산기 구현하기
def HA(A, B):
    S = XOR(A, B)
    C = AND(A, B)
    return (S, C)

print(HA(0, 0))
print(HA(0, 1))
print(HA(1, 1))
print(HA(1, 0))

# 2. 다층 퍼셉트론을 이용해 전가산기 구현
def FA(A, B, Cin):
  A1 = XOR(A, B)
  B1 = AND(A, B)
  S = XOR(A1, Cin)
  A2 = AND(A1, Cin)
  C2 = OR(A2, B1)
  return(np.array([S, C2]))

print(FA(0, 0, 0))
print(FA(0, 0, 1))
print(FA(0, 1, 0))
print(FA(0, 1, 1))
print(FA(1, 1, 1))
