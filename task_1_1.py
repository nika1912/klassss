
import sys

print("Версия Python:", sys.version.split()[0])
print("Интерпретатор:", sys.executable)

print("Количество путей поиска:", len(sys.path))
for p in sys.path[:4]:
    print("  ", p)

import math, random

print("math.pi =", math.pi)
print("random.random() =", random.random())

mods = sorted(sys.modules)
print("Всего загружено модулей:", len(mods))
print("Пример:", mods[:5])

# TODO 1: выведите количество публичных имён в модуле math
public = [n for n in dir(math) if not n.startswith('_')]
print("Публичных имён в math:", len(public))
print("Первые 8:", public[:8])

# TODO 2: выведите __name__ и __file__ этого скрипта
print("Мой __name__ =", __name__)
print('Мой __file__ =', __name__) 
