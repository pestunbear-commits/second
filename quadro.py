# Quadratic equations solver            23.09.2026

import matplotlib
matplotlib.use("TkAgg")          # задаём бэкенд ДО import pyplot
import matplotlib.pyplot as plt
import numpy as np

def calc_det(a,b,c):
    return b**2-4*a*c

def solve(a,b,c):
    D=calc_det(a,b,c)
    print(f"D={D}")
    print(f"Координаты вершины: x0={-b/2*a} y0={-D/(4*a)}")

x = np.linspace(-10, 10, 100)
# --- Фигура и оси создаём ОДИН раз ---
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-50, 50)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Параболы")
ax.grid(True)
fig.show()
print('Вторая строка для Git!')
while True:
    print("Hello! This is a program to  solve quadratic equations.")
    print("Enter 'a' koefficient or 'q' for quit:",end="")
    a_str=input().strip()
    if a_str=='q': break
    print("Enter 'b' koefficient or 'q' for quit:",end="")
    b_str=input().strip()
    if b_str=='q': break
    print("Enter 'c' koefficient or 'q' for quit:",end="")
    c_str=input().strip()
    if c_str=='q': break

    try:
        a=float(a_str)
        b=float(b_str)    
        c=float(c_str)
    except ValueError:
        print("Enter values correctly, please. Try again!")
        continue
        
    solve(a,b,c)
    y=a*x*x+b*x+c
    ax.plot(x, y)
    
    fig.canvas.draw_idle()
    fig.canvas.flush_events()



    
