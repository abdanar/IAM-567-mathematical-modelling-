import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# Generate data
x = np.arange(-8, 8, 0.5)
y = np.arange(-8, 8, 0.5)
X, Y = np.meshgrid(x, y)

# Define vector field
u = (3/2) * X - Y
v = X + Y

# Set a constant value for normalization
n = -2 * np.ones_like(u)

# Calculate color values based on vector magnitudes
color = np.sqrt(((v - n) / 2)**2 + ((u - n) / 2)**2)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(9, 9), dpi=300)

# Normalize color values
norm = Normalize()

# Create quiver plot with arrows colored based on magnitudes
ax.quiver(X, Y, u, v, color, alpha=1, cmap='viridis', norm=norm, scale=120)

# Add x and y axes lines
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Uncomment the following lines to customize the plot further
# ax.set_xlim(-3, 3)
# ax.set_ylim(-3, 3)

# Set aspect ratio to 'equal'
ax.set_aspect('equal')

# Save the figure as an image
#fig.savefig("phase.jpg", bbox_inches="tight")

# Display the plot
plt.show()
