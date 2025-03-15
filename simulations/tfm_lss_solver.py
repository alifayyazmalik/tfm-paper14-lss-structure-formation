import numpy as np
from scipy.integrate import odeint

def growth_factor(a, D, H, Omega_m, lambda_param, beta, H0):
    """
    Solves TFM-modified growth equation (Eq. 6)
    """
    dDda = [D[1], 
           -(3/a + H.derivative()(a)/H(a)) * D[1] 
           + (3 * Omega_m / (2 * a**5 * H(a)**2)) 
             * (1 + lambda_param * beta**2 * H0**2) * D[0]]
    return dDda

# Example usage with Planck parameters
H0 = 67.4  # Planck 2018
Omega_m = 0.31
lambda_param = 1.2e-5
beta = 14.8  # kpc to Mpc conversion needed

a_vals = np.linspace(0.001, 1, 1000)
D_init = [0.001, 0.001]  # Initial conditions
D_sol = odeint(growth_factor, D_init, a_vals, 
               args=(H, Omega_m, lambda_param, beta, H0))
