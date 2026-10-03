import matplotlib.pyplot as plt
import numpy as np

# Создаем массив комплексных чисел на окружности
t = np.linspace(0, 4*np.pi, 1000)
z = np.exp((1+1j) * t)+np.exp((0.3-2j) * 2*t) + np.exp((0.05-5j) * 6*t) # e^(i*t) — единичная окружность


plt.figure(figsize=(20, 20,'cm'))
plt.scatter(z.real, z.imag, color='blue')

mydot=0.1+0.3j;

plt.scatter(mydot.real, mydot.imag, color='red')
plt.axhline(y=0, color='black')   # Ось X
plt.axvline(x=0, color='black')   # Ось Y
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Комплексные числа на плоскости')
plt.axis('equal')  # Чтобы круги не выглядели эллипсами
plt.grid(True)
plt.show()