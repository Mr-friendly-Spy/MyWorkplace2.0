import math


def tan(angle_degrees):
    """
    Вычисляет тангенс угла в градусах.

    Args:
        angle_degrees (float): Угол в градусах

    Returns:
        float: Тангенс угла
    """
    angle_radians = math.radians(angle_degrees)
    return math.tan(angle_radians)


if __name__ == "__main__":
    # Тестирование
    print(f"tan(0°) = {tan(0):.3f}")
    print(f"tan(45°) = {tan(45):.3f}")