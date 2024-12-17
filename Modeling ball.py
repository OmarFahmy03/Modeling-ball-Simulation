import numpy as np
import turtle
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Gravitational acceleration (m/s^2)
e = 0.9   # Coefficient of restitution (bounce factor)
h0 = 400.0  # Initial height (turtle pixels)
v0 = 0.0    # Initial velocity (m/s)
t_end = 5.0  # Simulation time (s)
dt = 0.01    # Time step (s)
scale = 20.0  # Scale factor to convert meters to turtle pixels

# Function to simulate the bouncing ball
def simulate_bouncing_ball():
    positions = []
    times = []
    velocities = []

    t = 0.0
    y = h0 / scale  # Convert initial height to meters
    v = v0

    while t < t_end:
        times.append(t)
        positions.append(y)
        velocities.append(v)

        # Update position and velocity using Euler's method
        y = y + v * dt
        v = v - g * dt

        # Check for collision with the ground
        if y <= 0:
            y = 0  # Reset position to ground level
            v = -v * e  # Invert velocity and apply restitution factor

        t += dt

    return times, positions, velocities

# Run the simulation
times, positions, velocities = simulate_bouncing_ball()

#calculate kinetic energy
kinetic_energy = 0.5 * 1 * velocities[-1]**2


# Plot the trajectory of the ball
plt.figure(figsize=(10, 6))
plt.plot(times, [p * scale for p in positions], label="Bouncing Ball Trajectory", color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Height (pixels)")
plt.title("Bouncing Ball Simulation")
plt.grid()
plt.legend()
plt.show()

# Plot for Kinetic Energy
plt.figure(figsize=(10, 6))
plt.plot(times, [0.5 * 1 * v**2 for v in velocities], label="Kinetic Energy", color='green')
plt.xlabel("Time (s)")
plt.ylabel("Kinetic Energy (J)")
plt.title("Kinetic Energy vs. Time")
plt.grid()
plt.legend()
plt.show()

# Set up the Turtle screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulation")
wn.setup(width=400, height=600)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, h0 - 200)  # Adjust starting height to match turtle screen coordinates

# Animate the ball
for pos in positions:
    y = pos * scale - 200  # Scale and adjust for turtle screen
    ball.goto(0, y)

# Wait for user to close the window
wn.mainloop()
