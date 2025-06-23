import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, firwin

length = 512
# Generisanje impulsnog odziva FIR filtera
h = firwin(111, 0.3)

# Generisanje bijelog Gaussovog šuma
w = np.random.normal(0, 1, length)

# Generisanje izlaznog signala y[n] konvolucijom h[n] * w[n]
y = convolve(h, w)

# Inverz šuma: w[-n]
w_ = w[::-1]

# Estimacija impulsnog odziva: konvolucija y[n] sa w[-n], normalizovano
h_est = convolve(y, w_) / length

start = length - 1
h_est = h_est[start : start + 111]

# Plot 1: Poređenje stvarnog i estimiranog odziva
plt.figure(figsize=(10, 5))
plt.plot(h, 'r.', label='Stvarni impulsni odziv $h[n]$')
plt.plot(h_est, 'b', label='Estimirani odziv $\~h[n]$')
plt.grid(True)
plt.legend()
plt.title('Poređenje stvarnog i estimiranog impulsnog odziva')
plt.xlabel('n')
plt.ylabel('Amplituda')
plt.tight_layout()
plt.show()

# Plot 2: Greška estimacije
error = h - h_est
plt.figure(figsize=(10, 4))
plt.plot(error, 'k-', label='Greška estimacije $h[n] - \~h[n]$')
plt.grid(True)
plt.title('Greška estimacije impulsnog odziva')
plt.xlabel('n')
plt.ylabel('Greška')
plt.legend()
plt.tight_layout()
plt.show()

