
import os
import numpy as np
import pandas as pd

os.makedirs("data", exist_ok=True)

rng = np.random.default_rng(42)
n = 1000

# Reference data: normal container conditions
reference = pd.DataFrame({
    "temperature": rng.normal(5, 1.5, n),
    "humidity": rng.normal(85, 4, n),
    "vibration": rng.normal(0.3, 0.08, n)
})

# Current data: simulate environmental changes
current = pd.DataFrame({
    "temperature": rng.normal(9, 2.0, n),
    "humidity": rng.normal(72, 7, n),
    "vibration": rng.normal(0.3, 0.08, n)
})

reference.to_csv("data/reference_data.csv", index=False)
current.to_csv("data/current_data.csv", index=False)

print("Datasets generated successfully.")
print(f"Reference records: {len(reference)}")
print(f"Current records: {len(current)}")
print("\nReference data summary:")
print(reference.describe().round(2))
print("\nCurrent data summary:")
print(current.describe().round(2))
