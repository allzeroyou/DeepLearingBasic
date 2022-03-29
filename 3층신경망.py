# 3층 신경망 구현 정리

import numpy as np

# 시그모이드 함수 구현
def sigmoid(x):
  return 1/(1+np.exp(-x)) 

# 항등 함수 구현(입력을 그대로 출력)
def identify_function(x):
  return x 

# 가중치, 편향을 초기화 하고 network에 저장
# 딕셔너리 변수인 network에는 각 층에 필요한 매개변수(가중치와 편향) 저장

def init_network():
  network = {}
  network['W1'] = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]]) # 0->1 가중치
  network['b1'] = np.array([0.1, 0.2, 0.3]) # 0->1 편향
  network['W2'] = np.array([[0.1, 0.4],[0.2 ,0.5], [0.3, 0.6]]) # 1->2 가중치
  network['b2'] = np.array([0.1, 0.2]) # 1->2 편향
  network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]]) # 2->3 가중치
  network['b3'] = np.array([0.1, 0.2]) # 2->3 편향

  return network

def forward(network, x): # 신호: 순방향(입력->출력)
  W1, W2, W3 = network['W1'], network['W2'], network['W3']
  b1, b2, b3 = network['b1'], network['b2'], network['b3']

  a1 = np.dot(x, W1) + b1 # 0->1 가중치 계산
  z1 = sigmoid(a1) # 0->1 활성화
  a2 = np.dot(z1, W2) + b2 # 1->2 가중치 계산
  z2 = sigmoid(a2) # 1->2 활성화
  a3 = np.dot(z2, W3) + b3 # 2->3 가중치 계산
  y = identify_function(a3) # 2->3 활성화

  return y

network = init_network()
x = np.array([1.0, 0.5]) # 입력값
y = forward(network, x) # 출력값
print(y) # [0.31682708 0.69627909]