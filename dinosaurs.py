import pandas as pd
import numpy as np

species = ['Tyrannosaurus', 'Velociraptor', 'Stegosaurus', 'Triceratops', 'Brachiosaurus', 'Ankylosaurus', 'Allosaurus', 'Diplodocus', 'Pterodactyl', 'Spinosaurus']
names = ['Rex', 'Blue', 'Spike', 'Cera', 'Tiny', 'Tank', 'One-eye', 'Longneck', 'Pterry', 'Spiny']

def generate_dinosaur():
    return {'species': np.random.choice(species), 'name': np.random.choice(names), 'age': np.random.randint(0, 100)}