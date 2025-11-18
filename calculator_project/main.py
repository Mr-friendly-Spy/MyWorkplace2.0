# main.py
import sys
from calculator.basic import add, subtract
from calculator.advanced import power, square_root
from calculator.basic import multiply
from calculator.advanced.trigonometry import sin, cos, tan

print(add(2, 3))             # Вывод: 5
print(subtract(5, 2))        # Вывод: 3
print(power(2, 3))           # Вывод: 8
print(square_root(16))       # Вывод: 4.0
print(multiply(4, 5))        # Вывод: 20

print("\n--- Тригонометрические функции ---")
angles = [0, 30, 45, 60, 90]

for angle in angles:
    print(f"\nУгол {angle}°:")
    print(f"  sin({angle}°) = {sin(angle):.3f}")
    print(f"  cos({angle}°) = {cos(angle):.3f}")

    # Тангенс 90° не определен, обрабатываем исключение
    if angle != 90:
        print(f"  tan({angle}°) = {tan(angle):.3f}")
    else:
        print(f"  tan(90°) = не определен")
print(sys.path)