import argparse
from scipy import misc

parser = argparse.ArgumentParser(description='Znajdywanie miejsc zerowych metoda Newtona')

parser.add_argument('-func', type=str, required=True, help='Function to find roots of')
parser.add_argument('-start', type=int, required=False, help='Starting point')
parser.add_argument('-step_size', type=float, required=False, help='Step size')
parser.add_argument('-step_number', type=int, required=False, help='Number of steps')
parser.add_argument('-acc', type=float, required=False, help='Accuracy')

args = parser.parse_args()

def f(x):
  return eval(args.func)

def newton(x0, step_size, step_number, accurracy):
  x = x0
  for i in range(step_number):
    tmp = x - f(x) / misc.derivative(f, x) * step_size
    if abs(tmp - x) < accurracy:
      x = tmp
      break
    x = tmp
  return x

x = 1
if args.start:
  x = args.start

step_size = 0.6
if args.step_size:
  step_size = args.step_size

step_number = 10
if args.step_number:
  step_number = args.step_number

accurracy = 0.001
if args.acc:
  accurracy = args.acc

print(newton(x, step_size, step_number, accurracy))
