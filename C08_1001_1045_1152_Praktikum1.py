import matplotlib.pyplot as plt
import numpy as np

def f(constants: list, x):
    result = 0
    for i, c in enumerate(constants):
        result = result + c * x**i
    
    return result

def bolzano(left, right, g, constants, iterations):
    mid = (left + right) / 2
    print('{:>5s} | {:>20s} | {:>20s} | {:>20s} | {:>20s} | {:>20s} | {:>20s}'.format(
        'No.', 'X1', 'X2', 'X3', 'f(X1)', 'f(X2)', 'f(X3)'
    ))
    print('-'*(125+18))
    for iteration in np.arange(0, iterations):
        mid = (left + right) / 2
        gright = g(constants, right)
        gleft = g(constants, left)
        gmid = g(constants, mid)
        print('{:5} | {:20.10f} | {:20.10f} | {:20.10f} | {:20.10f} | {:20.10f} | {:20.10f}'.format(
            iteration, left, right, mid,
            gleft, gright, gmid
        ))

        if gmid == 0:
            return mid

        if gright * gmid > 0:
            right = mid
        elif gleft * gmid > 0:
            left = mid
    
    return mid
        
print('Degree of polynomial:', end=' ')
degree = int(input())

title = ''
constants = []
for i in np.arange(0, degree+1):
    print('Constant of x^{}:'.format(i), end=' ')
    constants.append(float(input()))
    polynomial = 'x' if i == 1 else 'x^{}'.format(i)
    if i == 0:
        title = '+' if constants[-1] > 0 else ''
        title = title + str(constants[-1])
    elif constants[-1] > 1:
        title = '+' + str(constants[-1]) + polynomial + title
    elif constants[-1] < -1:
        title = str(constants[-1]) + polynomial + title
    elif constants[-1] == 1:
        title = '+' + polynomial + title
    elif constants[-1] == -1:
        title = '-' + polynomial + title

if constants[-1] >= 1:
    title = title[1::]

print('Left limit of x:', end=' ')
left = int(input())
print('Right limit of x:', end=' ')
right = int(input())

print('Number of iterations:', end=' ')
iterations = int(input())

x = np.linspace(left, right, 1000)
y = f(constants, x)
root = bolzano(left, right, f, constants, iterations)
print('Root estimated at x = {}'.format(root))

plt.style.use('bmh')
plt.axhline(0, left, right, color='black', linewidth=1)
plt.axvline(0, min(y), max(y), color='black', linewidth=1)
plt.plot(x, y, color='C1')
plt.scatter(root, f(constants, root), color='C1', linewidth=4)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('$f(x) = {}$'.format(title))
plt.show()
