import pandas as pd
import torch
import numpy as np
import torch.nn as nn

data = pd.read_csv('data/synthetic_metrics.csv').values.astype(np.float32)

data_tensor = torch.tensor(data)

class AutoEncoder(nn.Module):
    """
    Encapsulates an autoencoder model composed of sequential encoder and decoder layers.

    The AutoEncoder class defines a simple architecture for encoding and decoding
    input data. This class is designed for dimensionality reduction and feature extraction,
    and it reconstructs the input data after encoding and decoding.

    :ivar encoder: Sequential neural network layers that encode the input into
        a compressed representation.
    :type encoder: nn.Sequential
    :ivar decoder: Sequential neural network layers that decode the compressed
        representation back to the original input dimensions.
    :type decoder: nn.Sequential
    """
    def __init__(self):
        super(AutoEncoder, self).__init__()
        self.encoder = nn.Sequential(nn.Linear(1, 16), nn.ReLU(), nn.Linear(16, 8))
        self.decoder = nn.Sequential(nn.Linear(8, 16), nn.ReLU(), nn.Linear(16, 1))
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

model = AutoEncoder()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(100):
    outputs = model(data_tensor)
    loss = criterion(outputs, data_tensor)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch + 1}/100], Loss: {loss.item():.4f}")

# Save the model
torch.save(model.state_dict(), 'models/anomaly_model.pth')

with torch.no_grad():
    reconstructed_data = model(data_tensor)
    mse = torch.mean((reconstructed_data - data_tensor) ** 2, dim=1).numpy()
    anomalies = mse > 0.5
    print(f"Anomalies detected: {np.sum(anomalies)} points")