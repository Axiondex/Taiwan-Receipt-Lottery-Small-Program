import new_proj.firstprog
import sys
print(new_proj.firstprog)
#input('c:\work===>')
print('iC:\work')
print('{} is {}'.format(10, 'Even' if 10 % 2 else 'odd'))
squares = [int(arg) ** 2 for arg in sys.argv[1:]]
print(squares)
if squares[0] > 2:
    print("yes")
