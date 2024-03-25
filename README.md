# Projectile Flight Path Simulator

This Python program simulates the flight path of a projectile launched with user-defined initial velocity (m/s) and launch angle (degrees). It calculates and displays the projectile positions throughout its flight path.

## Overview

The program utilizes the following projectile motion equations:

- Horizontal position (\( x \)): \( v \times \cos(\text{angle}) \times t \)
- Vertical position (\( y \)): \( v \times \sin(\text{angle}) \times t - 0.5 \times g \times t^2 \)

Where:
- \( x \) and \( y \) are the horizontal and vertical positions of the projectile respectively.
- \( v \) is the initial velocity of the projectile (m/s).
- \( \text{angle} \) is the initial angle of the projectile (in degrees).
- \( g \) is the acceleration due to gravity (9.81 m/s²).

## Usage

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/jonyach/projectile-calculator.git

2. Open a terminal or command prompt and navigate to the directory containing the script.
    ```bash
    cd projectile-calculator/flight_path

3. Run the script by executing the following command:
   ```bash
   python3 flight_path.py
