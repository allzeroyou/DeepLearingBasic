import numpy as np

# 손실함수 정의
def sum_square_error(y, t):
  return 0.5 * np.sum((y-t)**2)

y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# 손실 함수 값 낮음 => 성능 좋음(정답)
print(sum_square_error(np.array(y), np.array(t)))

y = [0.1, 0.05, 0.1, 0.0, 0.7, 0.3, 0.0, 0.0, 0.0, 0.0]

print(sum_square_error(np.array(y), np.array(t)))