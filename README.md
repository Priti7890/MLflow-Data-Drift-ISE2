# Container Sensor Data Drift Detection using MLflow

## 1. Project Overview

This project demonstrates data drift detection for container sensor data using MLflow. It is based on a simulated micro-climate monitoring scenario inspired by the AtmoSync use case.

Temperature, humidity, and vibration readings are compared between a reference dataset and a current dataset to identify changes in their statistical distributions.

## 2. Objectives

- Generate reference and current sensor datasets.
- Simulate changes in temperature and humidity.
- Detect distribution changes using the Kolmogorov-Smirnov (KS) test.
- Track experiment parameters, metrics, and artifacts using MLflow.
- Generate a CSV report and visualizations for analysis.

## 3. Technologies Used

- Python 3.11
- MLflow 3.17.2
- Pandas and NumPy
- SciPy
- Matplotlib

## 4. Dataset Description

Both datasets contain 1,000 simulated records and three features:

- `temperature`: container temperature readings
- `humidity`: container humidity readings
- `vibration`: container vibration readings

The reference dataset represents normal sensor conditions. The current dataset simulates an increase in temperature and a decrease in humidity. Vibration remains approximately unchanged.

These datasets are synthetic and are used to demonstrate the drift detection workflow. They are not live sensor readings.

## 5. Drift Detection Method

The two datasets are compared using the two-sample Kolmogorov-Smirnov test.

A significance threshold of 0.05 is used:

- p-value below 0.05: statistically significant distribution difference detected.
- p-value greater than or equal to 0.05: insufficient evidence of a distribution difference.

## 6. Results

The experiment produced the following results:

| Feature | KS Statistic | p-value | Drift Detected |
|---|---:|---:|---|
| Temperature | 0.756 | 3.774125e-280 | Yes |
| Humidity | 0.778 | 1.712983e-299 | Yes |
| Vibration | 0.029 | 0.794664 | No |

Temperature and humidity show statistically significant distribution changes. Vibration does not show statistically significant drift at the selected threshold.

## 7. MLflow Experiment Tracking

The experiment is named `AtmoSync_Sensor_Data_Drift`.

The run is named `Sensor_Drift_Detection`.

MLflow records the dataset sizes, drift detection method, significance threshold, KS statistics, p-values, drift flags, CSV report, and plots.

## 8. Project Structure

```text
MLflow-Data-Drift-ISE2/
├── generate_data.py
├── detect_drift.py
├── requirements.txt
├── README.md
├── data/
│   ├── reference_data.csv
│   └── current_data.csv
└── reports/
    ├── drift_report.csv
    ├── temperature_drift.png
    ├── humidity_drift.png
    └── vibration_drift.png
```

## 9. Execution Instructions

Create and activate a Python virtual environment, then install the dependencies:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Generate the datasets:

```powershell
.\.venv\Scripts\python.exe generate_data.py
```

Run drift detection and log the experiment:

```powershell
.\.venv\Scripts\python.exe detect_drift.py
```

Start the MLflow interface:

```powershell
.\.venv\Scripts\python.exe -m mlflow ui --port 5000
```

Open `http://localhost:5000` in a browser to inspect the experiment, metrics, parameters, and artifacts.

## 10. Conclusion

This project demonstrates a reproducible workflow for detecting simulated sensor data drift and tracking the experiment with MLflow. The results identify distribution changes in temperature and humidity while vibration remains statistically similar to the reference data.

In a real container-monitoring system, detected drift should trigger further investigation of sensor conditions and data quality. Statistical drift alone does not prove that spoilage has occurred.
