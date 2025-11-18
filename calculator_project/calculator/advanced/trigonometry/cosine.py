import math


def cos(angle_degrees):
    """
    Вычисляет косинус угла в градусах.

    Args:
        angle_degrees (float): Угол в градусах

    Returns:
        float: Косинус угла
    """
    angle_radians = math.radians(angle_degrees)
    return math.cos(angle_radians)


if __name__ == "__main__":
    # Тестирование
    print(f"cos(0°) = {cos(0):.3f}")
    print(f"cos(60°) = {cos(60):.3f}")
    print(f"cos(90°) = {cos(90):.3f}")