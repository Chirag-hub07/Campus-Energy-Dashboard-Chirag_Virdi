import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------------------
# TASK 1: DATA INGESTION
# ------------------------------

def load_all_data():
    data_folder = Path("data")
    all_files = list(data_folder.glob("*.csv"))
    combined = []

    for file in all_files:
        try:
            df = pd.read_csv(file, on_bad_lines='skip')
            df['Building'] = file.stem
            combined.append(df)
        except FileNotFoundError:
            print(f"Missing file: {file}")
        except Exception:
            print(f"Corrupt file skipped: {file}")

    if combined:
        df_combined = pd.concat(combined, ignore_index=True)
        df_combined['timestamp'] = pd.to_datetime(df_combined['timestamp'])
        return df_combined
    else:
        return pd.DataFrame()


# ------------------------------
# TASK 2: AGGREGATION FUNCTIONS
# ------------------------------

def calculate_daily_totals(df):
    return df.resample('D', on='timestamp')['kwh'].sum()

def calculate_weekly_aggregates(df):
    return df.resample('W', on='timestamp')['kwh'].sum()

def building_wise_summary(df):
    return df.groupby('Building')['kwh'].agg(['mean', 'min', 'max', 'sum'])


# ------------------------------
# TASK 3: OOP MODELING
# ------------------------------

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, timestamp, kwh):
        self.meter_readings.append(MeterReading(timestamp, kwh))

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_entry(self, building, timestamp, kwh):
        if building not in self.buildings:
            self.buildings[building] = Building(building)
        self.buildings[building].add_reading(timestamp, kwh)


# ------------------------------
# TASK 4: VISUAL DASHBOARD
# ------------------------------

def create_dashboard(daily, weekly, df):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].plot(daily.index, daily.values)
    axs[0].set_title("Daily Consumption")

    weekly_building = df.groupby('Building')['kwh'].mean()
    axs[1].bar(weekly_building.index, weekly_building.values)
    axs[1].set_title("Avg Weekly Usage per Building")

    axs[2].scatter(df['timestamp'], df['kwh'])
    axs[2].set_title("Peak Hours Scatter")

    plt.tight_layout()
    plt.savefig("dashboard.png")
    plt.close()


# ------------------------------
# TASK 5: EXPORT + SUMMARY
# ------------------------------

def export_and_summary(df, summary_df):
    df.to_csv("cleaned_energy_data.csv", index=False)
    summary_df.to_csv("building_summary.csv")

    total_energy = df['kwh'].sum()
    highest_building = summary_df['sum'].idxmax()
    peak_time = df.loc[df['kwh'].idxmax(), 'timestamp']

    with open("summary.txt", "w") as f:
        f.write(f"Total Campus Consumption: {total_energy}\n")
        f.write(f"Highest Consuming Building: {highest_building}\n")
        f.write(f"Peak Load Time: {peak_time}\n")


# ------------------------------
# MAIN EXECUTION
# ------------------------------

def main():
    df = load_all_data()

    if df.empty:
        print("No data found.")
        return

    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_aggregates(df)
    summary_df = building_wise_summary(df)

    create_dashboard(daily, weekly, df)
    export_and_summary(df, summary_df)

    print("Dashboard, cleaned CSV, summary CSV, and summary.txt generated!")


if __name__ == "__main__":
    main()
