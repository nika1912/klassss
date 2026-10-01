import random
import math

winning_numbers = random.sample(range(1, 46), 6)
winning_numbers.sort()
print("Выигрышные номера:", winning_numbers)
total_combinations = math.comb(45, 6)
probability = 1 / total_combinations
print(f"Общее число комбинаций: {total_combinations}")
print(f"Вероятность угадать все 6 чисел: {probability:.10f}")
print(f"Это примерно 1 шанс из {total_combinations}")