import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6,6,600)
N = (np.pi)**-0.25

psi1 = N*np.exp(-x**2/2)
psi2 = N*np.sqrt(2)*np.exp(-x**2/2)*x
psi3 = N/np.sqrt(8)*np.exp(-x**2/2)*(4*x**2-2)
psi4 = N/np.sqrt(48)*np.exp(-x**2/2)*(8*x**3-12*x)
psi5 = N/np.sqrt(384)*np.exp(-x**2/2)*(16*x**4-48*x**2+12)
psi6 = N/np.sqrt(3840)*np.exp(-x**2/2)*(32*x**5-160*x**3+120*x)


P1   = psi1**2
P2   = psi2**2+1.5
P3   = psi3**2+3
P4   = psi4**2+4.5
P5   = psi5**2+6
P6   = psi6**2+7.5



plt.figure(figsize=(12,7.416), dpi=300)
plt.xkcd(scale=1,length=70,randomness=4)

plt.fill(x,P1)
plt.text(-4.5,0.6, "n=0")
plt.fill(x,P2)
plt.text(-4.5,1.98, "n=1")
plt.fill(x,P3)
plt.text(-4.5,3.48, "n=2")
plt.fill(x,P4)
plt.text(-4.5,4.98, "n=3")
plt.fill(x,P5)
plt.text(-4.5,6.48, "n=4")
plt.fill(x,P6)
plt.text(-4.5,7.98, "n=5")

plt.xlabel('Displacement from equilibrium position')
plt.ylabel('Probability Density')

plt.title('Probability Density Functions of Quantum Oscillator')
#plt.show()
plt.savefig('/home/men/picture/ProbabilityofQuantumOscillator.pdf')