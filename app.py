from flask import Flask, request, jsonify
import torch
from src.detector import AutoEncoder

app = Flask(__name__)


model = AutoEncoder()
model.load_state_dict(torch.load('models/anomaly_model.pth'))
model.eval()


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('data', [])
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    data_tensor = torch.tensor(data, dtype=torch.float32).reshape(-1, 1)

    with torch.no_grad():
        reconstructed_data = model(data_tensor)
        mse = torch.mean((reconstructed_data - data_tensor) ** 2, dim=1).numpy()
        anomalies = mse > 0.5

    return jsonify({'anomalies': anomalies.tolist(), 'mse': mse.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)