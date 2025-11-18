import math


def sin(angle_degrees):
    """
    Вычисляет синус угла в градусах.

    Args:
        angle_degrees (float): Угол в градусах

    Returns:
        float: Синус угла
    """
    angle_radians = math.radians(angle_degrees)
    return math.sin(angle_radians)


# Способ 1: ОТНОСИТЕЛЬНЫЙ импорт
try:
    print("\n1. Относительный импорт:")
    from ..root import square_root
    result = square_root(25)
    print(f"   √25 = {result} ✅ УСПЕХ")
except ImportError as e:
    print(f"   ❌ ОШИБКА: {e}")

# Способ 2: АБСОЛЮТНЫЙ импорт
try:
    print("\n2. Абсолютный импорт:")
    from calculator.advanced.root import square_root
    result = square_root(36)
    print(f"   √36 = {result} ✅ УСПЕХ")
except ImportError as e:
    print(f"   ❌ ОШИБКА: {e}")

if __name__ == "__main__":
    # Тестирование
    print(f"sin(0°) = {sin(0):.3f}")
    print(f"sin(30°) = {sin(30):.3f}")
    print(f"sin(90°) = {sin(90):.3f}")