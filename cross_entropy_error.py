from cmath import e
import numpy as np
import math

def cross_entropy_error(y, t):
  delta = 1e-7
  return -np.sum(t * np.log(y + delta))
  # 예측값 y에 아주 작은 값인 delta를 더함

# 잘 추정된 값
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
# 잘못 추정된 값
y2 = [0.1, 0.05, 0.3, 0.0, 0.25, 0.6, 0.0, 0.1, 0.0, 0.0]
# 정답 레이블
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

print(cross_entropy_error(np.array(y), np.array(t)))
print(cross_entropy_error(np.array(y2), np.array(t)))