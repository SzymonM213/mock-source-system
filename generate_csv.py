import pandas as pd

from dinosaurs import generate_dinosaur

df = pd.DataFrame(generate_dinosaur() for _ in range(10_001))
df.to_csv('dinosaurs.csv', index=False)