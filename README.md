# AIOps: Anomaly Detection Service

A service that detects anomalies in time series data (e.g., server response times) using a **PyTorch** autoencoder neural network. The model is served via a **Flask** API and packaged in **Docker** for Cloud deployments, enabling real-time monitoring in **AIOps** scenarios.

## Technologies
- **Python**, **NumPy**, **Pandas**: Synthetic data generation and preprocessing.
- **PyTorch**: Autoencoder for anomaly detection.
- **Flask**: API for real-time predictions.
- **Docker**: Containerization for scalable deployment.

## Project Structure
- `src/load_data.py`: Generates and loads synthetic server response time data.
- `src/detector.py`: Trains the PyTorch autoencoder model.
- `app.py`: Flask API for serving predictions.
- `Dockerfile`: Docker configuration for the service.
- `data/synthetic_metrics.csv`: Synthetic dataset of response times.
- `requirements.txt`: Project dependencies.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/carroyo03/AnomalyDetect
   cd AnomalyDetect
    ```
2. Install dependencies:
    ```bash
    pip install uv && uv pip install -r requirements.txt
    ```


3. Generate data and train the model:
    ```bash
    python src/load_data.py
    python src/detector.py
    ```


4. Start the API:
    ```bash
    python app.py
    ```

5. Access the API at http://localhost:4000.

## Docker Deployment

1. Build the image:
    ```bash
    docker build -t anomaly-detection-service .
    ```

2. Run the container:
    ```bash
    docker run -p 4000:5000 anomaly-detection-service
    ```

3. Test the API inside the container or from the host:
    ```bash
    curl -X POST http://localhost:4000/predict -H "Content-Type: application/json" -d '{"data": [100, 200, 100]}' # Example request
    ```


## Usage
The `/predict` endpoint accepts a JSON payload with a data field containing an array of numerical values (e.g., response times in milliseconds). The response includes a list of booleans (anomalies) indicating anomalies and the mean squared error (mse) for each point.

### Example Request
```bash
curl -X POST http://localhost:4000/predict -H "Content-Type: application/json" -d '{"data": [100, 300, 100]}'
```
### Example Response

```json
{
  "anomalies": [false, true, false],
  "mse": [0.019852712750434875, 4.74531888961792, 0.019852712750434875]
}
```


## Use Case
This service can be integrated with **Azure Monitor** or **AWS CloudWatch** to monitor server performance in real time, detecting anomalies like latency spikes. For example, it could trigger alerts via **Slack** or **PagerDuty** when response times exceed normal thresholds, optimizing IT operations in Cloud environments.



## Next Steps

Deploy the service on **Azure Functions** or **AWS Lambda** for serverless scaling.
Add a **Streamlit** dashboard for real-time visualization.
Integrate with **Grafana** for monitoring dashboards.



