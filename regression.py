
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

# Generating synthetic data
n = 100
x = np.linspace(0, 2 * np.pi, n)
y = np.sin(x) + 0.3 * np.random.randn(n)

# Smoothing parameters
frac = 0.25
it = 3

# Apply lowess function
yest = lowess(y, x, frac=frac, it=it)

# Plotting the results
plt.plot(x, y, "r.", label="Original Data")
plt.plot(yest[:, 0], yest[:, 1], "b-", label="LOWESS Smoothing")
plt.legend()
plt.show()
