import math

def point_in_spherical_shell(x, y, z, r1, r2):
    distance = math.sqrt(x**2 + y**2 + z**2)
    
    if r1 <= distance <= r2:
        return True
    else:
        return False

x = float(input("Введите координату x точки: "))
y = float(input("Введите координату y точки: "))
z = float(input("Введите координату z точки: "))
r1 = float(input("Введите радиус r1 слоя: "))
r2 = float(input("Введите радиус r2 слоя: "))

if point_in_spherical_shell(x, y, z, r1, r2):
    print(f"Точка ({x}, {y}, {z}) принадлежит шаровому слою с радиусами {r1} и {r2}.")
else:
    print(f"Точка ({x}, {y}, {z}) не принадлежит шаровому слою с радиусами {r1} и {r2}.")
