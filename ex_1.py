import sympy
import matplotlib.pyplot as plt
import numpy as np

sympy.init_printing(order='rev-lex')

# Creation of symbols
# s: Laplace variable
# t: time
s, t = sympy.symbols('s t')

# Input exp(-2*t)*2 in the Laplace transform
def L(f): return sympy.laplace_transform(f, t, s, noconds=True)

# Inverse Laplace Transform 
def invL(F): return sympy.inverse_laplace_transform(F, s, t)

# input Laplace Transformation
F = L(sympy.exp(-2*t)*2)
print('input after Laplace Transformation', end='\n\n')
sympy.pprint(F)
print('\n')

# Transfer Function
G = 1/(s**2 + 5*s + 4)
print('Transfer Funtion', end='\n\n')
sympy.pprint(G)
print('\n')

# Response in the Laplace Domain
X = G*F
print('Response in the Laplace domain', end='\n\n')
sympy.pprint(X)
print('\n')

print('Response in the Laplace domain, but with partial functions', end='\n\n')
sympy.pprint(X.apart(s))
print('\n')

print('X inverse', end='\n\n')
sympy.pprint(invL(X))


plt.rcParams['figure.figsize'] = (10,10) # Graphic Size
plt.rcParams['font.size'] = 14 # Letter size

# Plot the response found
t = np.linspace(0, 20, 1001) # time vector
u = 2/3*(np.exp(-1*t))-1*(np.exp(-2*t))+1/3*(np.exp(-4*t)) # vector response

# figure
plt.plot(t, u, 'r', linewidth=2, label='resposta')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.1)
plt.ylabel('position (m)')
plt.xlabel('time (s)')
plt.show()