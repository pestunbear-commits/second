import matplotlib
matplotlib.use("TkAgg")          # задаём бэкенд ДО import pyplot
import matplotlib.pyplot as plt
import numpy as np

# --- Данные по оси X ---
x = np.linspace(-10, 10, 100)

# --- Фигура и оси создаём ОДИН раз ---
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-50, 50)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Прямые y = kx + b")
ax.grid(True)

# --- Интерактивный режим ---
plt.ion()
fig.show()

# --- Цикл ввода ---
while True:
    # --- Ввод k ---
    k_str = input("Введите коэффициент 'k' или Enter для выхода: ").strip()
    if k_str == "":
        print("Бай-бай!")
        break

    # --- Ввод b ---
    b_str = input("Введите коэффициент 'b': ").strip()

    # --- Преобразование в числа с обработкой ошибок ---
    try:
        k = float(k_str)
        b = float(b_str)
    except ValueError:
        print("Ошибка: нужны числа. Попробуйте снова.\n")
        continue

    # --- Считаем и рисуем ---
    y = x * k + b
    # line, = ax.plot(x, y, label=f"y = {k:g}x + {b:g}")
    ax.plot(x, y, label=f"y = {k:g}x + {b:g}")

    # --- Легенда: показываем все линии, но не даём ей разрастись ---
    handles, labels = ax.get_legend_handles_labels()
    if len(handles) > 10:
        # оставляем только последние 10
        handles, labels = handles[-10:], labels[-10:]
    ax.legend(handles, labels, loc="upper left", fontsize="small")

    # --- Перерисовать и дать окну обработать события ---
    # fig.canvas.draw()
    plt.pause(0.001)

print("Программа завершена.")
