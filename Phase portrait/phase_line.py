import numpy as np
import matplotlib.pyplot as plt

# Define the grid
x = np.arange(-8, 8, 0.5)
y = np.arange(-8, 8, 0.5)
X, Y = np.meshgrid(x, y)

# Define the vector field
u = X*(3-X-Y)
v = Y*(4-2*X-Y)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(9, 9), dpi=300)

# Add axis lines
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Compute the magnitude of the vector field
magnitude = np.sqrt(u**2 + v**2)

# Create a colorful stream plot
ax.streamplot(X, Y, u, v, color=magnitude, cmap='viridis', density=3, linewidth=0.6, arrowstyle='->', arrowsize=1.5)

# Set aspect ratio to be equal
ax.set_aspect('equal')

# Save the figure
fig.savefig("phaseline.jpg", bbox_inches="tight")

# Display the plot
plt.show()
