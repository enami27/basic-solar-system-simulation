# Solar system simulation

## Description
Simple way to visualize the Solar system, made using the pygame library. It helps at visualizing the motion and speed of the different planets aroud the sun, showing their orbits and providing a basic representation of their relative distances and velocities

## Installation and usage

### Pre-requisites
- Python 3.x
- Pygame library

### Installation
to run this simulation, you will first need to install the Pygame library by running the following command in your project directory : `pip install pygame`

### Usage
Execute the script to start the simulation using the following command : `python main.py` or `python3 main.py`(make sure to replace `main.py` by your file name, and to be in your project durectory

A window will open displaying the solar system. Each planet is following its orbit around the Sun, and their current distances are displayed in kilometers.

## Features
**Planetary orbits** : Displays orbits for Earth, Mars, Mercury and Venus around the sun
**Dynamic simulation** : Shows the movement and distance of the planets relative to the sun in real time
**Distance display** : Shows the current diatnce of each planet around the sun
**Custom Physics engine** : Uses Newton's law of universal gravitation to simulate planetary motion

## How it works
- The simulation initializes with predefined planet objects, each having specific attributes like radius, mass, color and initial velocity
- The `Planet`class calculates gravitational forces between each planet and updates their velocities and positions accordingly
- Pygame renders the planets and their orbits, updating the display in real time

## Possible customization
You can customize the simulation by adding more planets, altering their initial conditions, or tweaking the physics constants

## Limitations
- This is a basuc representation, and does not account for factors like orbital eccentricity and inclination
- Planetary sizes and distances are not at scale for visualization and aesthetic purposes
