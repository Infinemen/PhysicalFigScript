import numpy as np
import matplotlib.pyplot as plt
import os



r=np.linspace(0,30,1500)

spi = 1/np.sqrt(np.pi)
fourpi = 4*np.pi
R100 = spi *np.exp(-r)
R200 = 1/np.sqrt(8)*spi*(1-r/2)*np.exp(-r/2)
R210 = 1/4/np.sqrt(6)*spi*r*np.exp(-r/2)
R300 = 1/3/np.sqrt(3)*spi*(1-2/3*r+2/27*r**2)*np.exp(-r/3)
R310 = 4/27/np.sqrt(6)*spi*(1-r/6)*r*np.exp(-r/3)
R320 = 2/81/np.sqrt(30)*spi*r**2*np.exp(-r/3)


P100=fourpi*(r*R100)**2
P200=fourpi*(r*R200)**2
P210=fourpi*(r*R210)**2
P300=fourpi*(r*R300)**2
P310=fourpi*(r*R310)**2
P320=fourpi*(r*R320)**2

f = plt.figure(figsize=(12,7.416), dpi= 300)

plt.xkcd(scale=1,length=70,randomness=4)

plt.fill(r,P100,'red',alpha=0.8)
plt.text(1,0.55,'100',color='red')
plt.fill(r,P200,'blue',alpha=0.8)
plt.text(6,0.21,'200',color='blue')
plt.fill(r,P210,'green',alpha=0.4)
plt.text(3,0.21,'210',color='green')
plt.fill(r,P320,'gray',alpha=0.7)
plt.text(10,0.13,'320',color='gray')
plt.fill(r,P310,'purple',alpha=0.4)
plt.text(13,0.13,'310',color='purple')
plt.fill(r,P300,'orange',alpha=0.5)
plt.text(16,0.13,'300',color='orange')
plt.xlabel('q/a_0')
plt.ylabel('Radical Probability 4\pi r^2R_{nl}^2')


plt.title('Probability Density Functions of Hydrogen Atom Electron')
#plt.show()
plt.savefig('/home/men/picture/ProbabilityofHydrogenAtom.pdf')