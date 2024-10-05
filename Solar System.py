from ursina import *
import math

app = Ursina()

# Set the window title
window.title = 'Solar System'
window.fullscreen = False

# Create the EditorCamera for editing
camera = EditorCamera()

# Create a Sun
sun = Entity(model='sphere', scale=2, texture = 'sun.png')
sun.collider = 'sphere'  # Enable collision for the sun

# Define planets as a list of dictionaries
planets = [
    {'name': 'Mercury', 'distance': 4, 'scale': 0.2, 'speed': 0.05, 'texture' : 'mercury.png'},
    {'name': 'Venus', 'distance': 6, 'scale': 0.4, 'speed': 0.03, 'texture' : 'venus.png'},
    {'name': 'Earth', 'distance': 8, 'scale': 0.5, 'speed': 0.02, 'texture' : 'earth.png'},
    {'name': 'Mars', 'distance': 10, 'scale': 0.3, 'speed': 0.015, 'texture' : 'mars.png'},
    {'name': 'Jupiter', 'distance': 12, 'scale': 0.7, 'speed': 0.01, 'texture' : 'jupiter.png'},
    {'name': 'Saturn', 'distance': 14, 'scale': 0.6, 'speed': 0.008, 'texture' : 'saturn.png'},
    {'name': 'Uranus', 'distance': 16, 'scale': 0.5, 'speed': 0.005, 'texture' : 'uranus.png'},
    {'name': 'Neptune', 'distance': 18, 'scale': 0.5, 'speed': 0.004, 'texture' : 'neptune.png'},
]

# Create planets
for planet in planets:
    planet_entity = Entity(
        model='sphere',
        texture=planet['texture'],
        scale=planet['scale'],
        position=(planet['distance'], 0, 0)
    )
    planet_entity.collider = 'sphere'
    planet['entity'] = planet_entity  # Store the entity in the planet dictionary

# Update function to move planets
def update():
    for planet in planets:
        planet['entity'].rotation_y += planet['speed']  # Rotate planet around the Sun
        # Create an orbit effect
        angle = time.time() * planet['speed']
        planet['entity'].position = (
            planet['distance'] * math.cos(angle), 
            0, 
            planet['distance'] * math.sin(angle)
        )

window.fullscreen = True
Sky(texture = 'space.jpg')

app.run()
