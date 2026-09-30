PI = 3.14159265358979
VERSION = "1.0.0"
_secret = "это скрытая константа"

def circle_area(r): return PI * r ** 2
def circle_len(r): return 2 * PI * r
def _helper(): return PI / 2

if __name__ == "__main__":
    print(f"[{VERSION}] Самопроверка mymodule:")
    print(" S(r=2) =", circle_area(2))
    print(" L(r=2) =", circle_len(2))
    
import mumodule 
from mymodule import circle_area,VERSION
from mymodule import circle_len as perimetr
import mymodule as mm 

print("1) mymodule.circle_area(5) =", mymodule.circle_area(5))
print("2) circle_area(5)          =", circle_area(5)) 
print("3) perimetr(5)             =", perimetr(5))
print("4 mm.PI                    =", mm.PI)

print("dir(mymodule ->", [ n for n in dir(mymodule) if not n.startswith('__')])
print("mymodule.__name__ =", mymodule.__name__)
print("mymodule.__file__ =", mymodule.__file__)

print("mm._helper() =", mm._helper())
