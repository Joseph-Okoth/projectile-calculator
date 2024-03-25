# Projectile Flight Path Simulator

This Python program simulates the flight path of a projectile launched with user-defined initial velocity (m/s) and launch angle (degrees). It calculates and displays the projectile positions throughout its flight path.

## Overview

The program utilizes the following projectile motion equations:

- Horizontal position (x) = v * cos(angle) * t
- Vertical position (y) = v * sin(angle) * t - 0.5 * g * t^2

- \( v \) is the initial velocity of the projectile (m/s).
- \( {angle} \) is the initial angle of the projectile (in degrees).
- \( g \) is the acceleration due to gravity (9.81 m/s²).

## Usage

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/jonyach/projectile-calculator.git

2. Open a terminal or command prompt and navigate to the directory containing the script.
    ```bash
    cd ./projectile-calculator/

3. Run the script by executing the following command:
   ```bash
   python3 flight_path.py
