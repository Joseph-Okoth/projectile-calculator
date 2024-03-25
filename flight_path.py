"""
Python program that simulates the flight path of a projectile 
launched with a user-defined initial velocity (m/s) and launch angle (degrees).
The output should be a display of the calculated projectile positions 
throughout its flight path.

The formulae behind the simulation are: 
          x = v * cos(angle) * t
          y = v * sin(angle) * t - 0.5 * g * t^2
  where x and y are the horizontal and vertical positions of the projectile,

"""

# Import the math module to use the sin and cos functions
import math

def main():
    # Ask the user to input the initial angle of the projectile in degrees
    angle = float(input("Please enter the initial angle of the projectile (in degrees): "))
    
    # Ask the user to input the initial velocity of the projectile in m/s
    velocity = float(input("Please enter the initial velocity of the projectile in m/s: "))

    # Print the entered angle and initial velocity to ensure they are correct
    print("The angle of projectile = ", angle, "degrees")
    print("The initial Velocity = ", velocity, "m/s")

    # Define acceleration due to gravity (m/s^2)
    g = 9.81
    
    # Initialize time variable
    t = 0
    
    # Introduce a Loop to calculate and print projectile positions until it hits the ground
    while True:
        # Calculate x and y positions using projectile motion equations
        x = velocity * math.cos(math.radians(angle)) * t
        y = velocity * math.sin(math.radians(angle)) * t - 0.5 * g * t**2
        
        # Check if the projectile has hit the ground
        if y < 0:
            break
        
        # Print the current position of the projectile
        print(f"({x:.2f}, {y:.2f})")

        # Increment time for the next iteration
        t += 0.1

        # Let the user know that the projectile has landed when y < 0

        # while True:
        #     if y == 0:
        #         print("The projectile has landed.")
        #         break
        #     else:
        #         break  




        # if y = 0:
        #     print("The projectile has landed.")

    # # Calculate and print the flight path of the projectile of y is < 0 then print that it has landed.
    # print(f"The flight path of the projectile is ({x:.2f}, {y:.2f})")

# Call the main function to execute the program
main()
