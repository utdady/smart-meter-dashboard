import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Config
num_meters = 100
days = 7
readings_per_day = 24
total_readings = num_meters * readings_per_day * days

data = []
start_time = datetime(2025, 6, 1, 0, 0, 0)

for meter_id in range(1, num_meters + 1):
    timestamp = start_time
    for _ in range(readings_per_day * days):
        # Normal Usage
        usage = round(np.random.normal(3.5, 1.0), 2)

        # Simulate outliers
        if random.random() < 0.01:
            usage = round(usage * random.randint(5, 10), 2) # huge spike

        # Simulate missing readings
        if random.random() < 0.005:
            continue

        data.append({
            "meter_id": f"MTR{meter_id:04d}",
            "timestamp": timestamp,
            "kWh": usage
        })
        timestamp += timedelta(hours=1)

df = pd.DataFrame(data)
df.to_csv("smart_meter_data.csv", index=False)
