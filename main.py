import math

numbers = (1, 2, 3, 4, 5)
product = math.prod(numbers)
print(product)  # Output: 120
import math

angle_degrees = 45
angle_radians = math.radians(angle_degrees)

sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

print(f"Sin({angle_degrees}°) = {sin_value:.4f}")
print(f"Cos({angle_degrees}°) = {cos_value:.4f}")
print(f"Tan({angle_degrees}°) = {tan_value:.4f}")
numbers = list(range(1, 11))
squares = [num ** 2 for num in numbers]

even_squares = [square for square in squares if square % 2 == 0]
odd_squares = [square for square in squares if square % 2 != 0]

print(f"Squares: {squares}")
print(f"Even Squares: {even_squares}")
print(f"Odd Squares: {odd_squares}")
