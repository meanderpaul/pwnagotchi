import time
import numpy as np

from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        # Initialize the Isolation Forest model
        self.model = IsolationForest(contamination=0.01)
        self.trained = False

    def fit(self, data):
        # Fit the model with the initial data
        self.model.fit(data)
        self.trained = True

    def predict(self, data):
        if not self.trained:
            raise Exception("Model not trained yet")
        # Predict anomalies (-1 indicates an anomaly)
        return self.model.predict(data)

    def log_anomaly(self, anomaly_data):
        anomaly_log = {
            'timestamp': time.time(),
            'data': anomaly_data
        }
        with open("anomaly_log.txt", "a") as log_file:
            log_file.write(f"{anomaly_log}\n")

# Initialize the anomaly detector
anomaly_detector = AnomalyDetector()
