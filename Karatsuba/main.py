from karatsuba import k
import sys

if __name__ == "__main__":
    # python main.py number1 number2 
    a, b = sys.argv[1], sys.argv[2]
    print(k(a, b))