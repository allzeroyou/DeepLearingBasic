import numpy as np

def numerical_diff(f, x):
  h = 10e-4
  return (f(x+h)-f(x-h))/(2*h)


print(np.float32(10e-50)) # 0.0



def numerical_gradient(f, x):
  h = 1e-4
  grad = np.zeros_like(x) # x와 형상이 같은 배열 생성
  for idx in range(x.size):
    tmp_val = x[idx]
    # f(x+h) 계산
    x[idx] = tmp_val + h
    fxh1 = f(x)
    # f(x-h) 계산
    x[idx] = tmp_val - h
    fxh2 = f(x)

    grad[idx] = (fxh1 - fxh2) / (2*h)
    x[idx] = tmp_val # 값 복원

    return grad

def function_2(x): # 매개변수 x는 넘파이배열
  return x[0] ** 2 + x[1] ** 2

# (3, 4), (0, 2), (3, 0) 세 점에서의 기울기 구하기
print(numerical_gradient(function_2, np.array([3.0, 4.0])))
print(numerical_gradient(function_2, np.array([0.0, 2.0])))
print(numerical_gradient(function_2, np.array([3.0, 0.0])))

