import numpy as np
import matplotlib.pyplot as plt

# 1. Create a grid of (x, y) points
x = np.linspace(-3.5, 3.5, 400)
y = np.linspace(-3.5, 3.5, 400)
X, Y = np.meshgrid(x, y)

# 2. Define the function for the 3D surface
Z = X**2 + Y**2

# 3. Create the contour plot (level curves)
plt.figure(figsize=(7, 6))
# Define the levels (heights) at which to draw the curves
levels = [1, 4, 9, 16] 
contours = plt.contour(X, Y, Z, levels=levels)

# Add labels to the contour lines showing their z-value
plt.clabel(contours, inline=True, fontsize=10)

# 4. Add labels and title
plt.title('Level Curves of z = x^2 + y^2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
# Ensure the circles look like circles, not ovals
plt.gca().set_aspect('equal', adjustable='box')

# 5. Show the plot
plt.show()