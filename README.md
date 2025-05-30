# Anomaly Detection Service

An API service that uses an autoencoder neural network to detect anomalies in time series data. The model is trained to
identify unusual patterns in response time metrics.

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install uv && uv pip install -r requirements.txt
```
3. Start the service:
```bash
python main.py
```
4. Access the API at `http://localhost:4000`with the following parameters:
```bash
curl -X POST http://localhost:4000/predict \
-H "Content-Type: application/json" \```
-d '{"data": [100,200,100]}' # Example data
```

You can also use it with Docker:

```bash
docker build -t anomaly-detection-service .
docker exect -it anomaly-detection-service bash
# The above curl command can be used inside the container
```

## Usage
The service provides an endpoint `/predict` that accepts a JSON payload with a `data` field containing an array of numerical values representing the time series data. The service will return a JSON response indicating whether the data is normal or anomalous.
### Example Request
```bash
curl -X POST http://localhost:4000/predict \
-H "Content-Type: application/json" \
-d '{"data": [100, 200, 100]}'
```
### Example Response
```json
{
  "anomalies": [
    false,
    true,
    false
  ],
  "mse": [
    0.019852712750434875,
    4.74531888961792,
    0.019852712750434875
  ]
}
```