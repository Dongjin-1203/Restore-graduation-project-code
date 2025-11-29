import numpy as np  #삼각함수 사용하기 위한 모듈 적용
import matplotlib.pyplot as plt # 그래프 그리기 위한 모듈 적용
from pylab import cm
x = np.linspace(-np.pi, np.pi)  #X값 범위 지정

theta = [0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45] # 세타 값 리스트
#theta = [0,3,6,9,12]
k= 0.125
F_0 = 0.2
fig, ax = plt.subplots(figsize=(10, 10)) #그래프 그려주는 함수
for i in theta :    # i라는 변수가 b리스트(세타 값 리스트)에 있다면 아래 코드 반복해서 진행
  i = i*np.pi/180 +3  # i가 3씩 증가
  y= F_0+0.7*(-np.cos(2*i)*np.cos(x)+k*np.cos(2*x))   #free energy
  ax.plot(x, y) # 그래프를 그리기 위해 x축 y축에 해당값을 입력

plt.ylim(-1.0, 1.0, 0.5)
plt.axhline(y=0, color="grey")
plt.axvline(x=0, color="grey")
plt.xlabel("φ", fontsize=20)
plt.ylabel(" F (φ)", fontsize=20)
ax.text(1, -0.7, '$θ=0$', fontsize=15)
ax.text(1.5, -0.3, '$θ=θ_c$', fontsize=15)
ax.text(0, 0, '$θ=π/4$', fontsize=15)
plt.show() # 그래프 출력
