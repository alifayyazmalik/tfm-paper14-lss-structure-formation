import numpy as np
import matplotlib.pyplot as plt

def calculate_Pk(k, sigma8_TFM, sigma8_LCDM=0.81):
    """
    TFM vs ΛCDM power spectrum (Fig. 1)
    """
    Pk_TFM = (sigma8_TFM / sigma8_LCDM)**2 * k**(-3)
    Pk_LCDM = k**(-3)
    return Pk_TFM, Pk_LCDM

k = np.logspace(-2, 1, 100)  # h/Mpc
Pk_TFM, Pk_LCDM = calculate_Pk(k, 0.76)

plt.loglog(k, Pk_TFM, label='TFM')
plt.loglog(k, Pk_LCDM, label='ΛCDM')
plt.xlabel('k [h/Mpc]'); plt.ylabel('P(k)')
plt.legend(); plt.savefig('power_spectrum.png')
