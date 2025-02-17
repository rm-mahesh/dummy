import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV file
file_path = "C:/Users/mahes/Desktop/L2M/MVIS_ACPS_CSV_27_01/T20250119002424.csv"  # Update with your file path
df = pd.read_csv(file_path)
print(df.columns)

# Convert timestamp column to datetime (assuming column name is 'timestamp')
# df['timestamp'] = pd.to_datetime(df['Time'])

# Function to compute differentiation and plot
def plot_sensor_with_derivative(sensor_column):
    if sensor_column not in df.columns:
        print(f"Error: Column '{sensor_column}' not found in CSV.")
        return

    # Compute first derivative (rate of change)
    df['diff'] = np.gradient(df[sensor_column], df['BufferId'].astype('int64') / 1e9)  # Convert ns to seconds

    # Plot both original and differentiated signals
    plt.figure(figsize=(12, 6))

    # Plot original sensor data
    plt.subplot(2, 1, 1)
    plt.plot(df[sensor_column],df['BufferId'],  marker='o', linestyle='-', label=f"Raw {sensor_column}")
    plt.xlabel("Timestamp")
    plt.ylabel("Sensor Value")
    plt.title(f"Original Sensor Data: {sensor_column}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Plot differentiated (rate of change) data
    plt.subplot(2, 1, 2)
    plt.plot(df['Time'], df['diff'], marker='o', linestyle='-', color='red', label=f"Derivative of {sensor_column}")
    plt.xlabel("Timestamp")
    plt.ylabel("Rate of Change")
    plt.title(f"First Derivative of {sensor_column}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Example usage
plot_sensor_with_derivative("S11")  # Change sensor_1 to your column name
