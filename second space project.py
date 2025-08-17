import matplotlib.pyplot as plt
import numpy as np

planets = [
    {"r" : 1, "color" : "blue", "size" : 50, "name" : "Planet 1"},
    {"r" : 1.5, "color" : "red", "size" : 70, "name" : "Planet 2"},
    {"r" : 2, "color" : "green", "size" : 90, "name" : "Planet 3"}
    ]

theta = np.linspace(0, 2*np.pi, 200)

plt.figure(figsize=(6,6))
plt.scatter(0, 0, color='yellow', s=300, label='Star')

for planet in planets:
    x = planet["r"] * np.cos(theta)
    y = planet["r"] * np.sin(theta)
    plt.plot(x, y, label=planet["name"])
    plt.scatter(planet["r"], 0, color=planet["color"], s=planet["size"])

plt.title("Mini Solar System Simulation")
plt.xlabel("X position")
plt.ylabel("Y position")
plt.legend()
plt.axis('equal')
plt.show()