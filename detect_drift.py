
import os
import pandas as pd
import matplotlib.pyplot as plt
import mlflow
from scipy.stats import ks_2samp

# Load datasets
reference = pd.read_csv("data/reference_data.csv")
current = pd.read_csv("data/current_data.csv")

# MLflow experiment setup
mlflow.set_experiment("AtmoSync_Sensor_Data_Drift")

# Output folders
os.makedirs("reports", exist_ok=True)

results = []
threshold = 0.05

with mlflow.start_run(run_name="Sensor_Drift_Detection"):
    mlflow.log_param("reference_records", len(reference))
    mlflow.log_param("current_records", len(current))
    mlflow.log_param("drift_method", "Kolmogorov-Smirnov test")
    mlflow.log_param("p_value_threshold", threshold)

    for feature in reference.columns:
        statistic, p_value = ks_2samp(
            reference[feature],
            current[feature]
        )

        drift_detected = p_value < threshold

        results.append({
            "feature": feature,
            "ks_statistic": statistic,
            "p_value": p_value,
            "drift_detected": drift_detected
        })

        mlflow.log_metric(f"{feature}_ks_statistic", float(statistic))
        mlflow.log_metric(f"{feature}_p_value", float(p_value))
        mlflow.log_param(f"{feature}_drift_detected", str(drift_detected))

    results_df = pd.DataFrame(results)
    results_df.to_csv("reports/drift_report.csv", index=False)

    # Plot reference and current distributions
    for feature in reference.columns:
        plt.figure(figsize=(8, 5))
        plt.hist(reference[feature], bins=30, alpha=0.6,
                 label="Reference data", density=True)
        plt.hist(current[feature], bins=30, alpha=0.6,
                 label="Current data", density=True)
        plt.xlabel(feature)
        plt.ylabel("Density")
        plt.title(f"Data Drift Analysis: {feature}")
        plt.legend()
        plt.tight_layout()

        plot_path = f"reports/{feature}_drift.png"
        plt.savefig(plot_path)
        plt.close()

        mlflow.log_artifact(plot_path)

    mlflow.log_artifact("reports/drift_report.csv")

    print("\nDRIFT DETECTION RESULTS")
    print(results_df.to_string(index=False))
    print("\nDrift report and plots saved in the reports folder.")
