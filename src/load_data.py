import pandas as pd
import numpy as np

n_samples = 1000
normal_mean = 100
normal_std = 10
anomaly_rate = 0.05
anomaly_factor = 3

np.random.seed(42)
data = np.random.normal(loc=normal_mean, scale=normal_std, size=n_samples)

anomaly_indexes = np.random.choice(n_samples, size=int(n_samples * anomaly_rate), replace=False)
data[anomaly_indexes] += np.random.normal(normal_mean * anomaly_factor, normal_std * 2, len(anomaly_indexes))

data = data.reshape(-1, 1).astype(np.float32)

df = pd.DataFrame(data, columns=['response_time_ms'])
df.to_csv('data/synthetic_metrics.csv', index=False)