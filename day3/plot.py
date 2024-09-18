import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0, 2*np.pi,30)
y=np.cos(x)


plt.xlabel('x(radians)')
plt.ylabel('y(cos)')
plt.title('Graph du cosinus')
plt.plot(x,y)
plt.grid()

plt.savefig('plot.png')
