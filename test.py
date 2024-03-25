import math

def projectile_motion(initial_velocity, launch_angle):
    # Convert launch angle from degrees to radians
    launch_angle_rad = math.radians(launch_angle)
    
    # Constants
    g = 9.81  # acceleration due to gravity (m/s^2)
    time_interval = 0.1  # time interval for calculation (s)
    
    # Initial values
    x = 0
    y = 0
    vx = initial_velocity * math.cos(launch_angle_rad)
    vy = initial_velocity * math.sin(launch_angle_rad)
    t = 0
    
    print("Time(s)\t\tX(m)\t\tY(m)")
    
    # Simulation loop
    while y >= 0:
        # Update time
        t += time_interval
        
        # Calculate new position
        x = vx * t
        y = vy * t - 0.5 * g * t ** 2
        
        # Print results
        print(f"{t:.2f}\t\t{x:.2f}\t\t{y:.2f}")
        
    print("Projectile has landed.")

# Input from the user
initial_velocity = float(input("Enter initial velocity (m/s): "))
launch_angle = float(input("Enter launch angle (degrees): "))

# Call the function to simulate projectile motion
projectile_motion(initial_velocity, launch_angle)