import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import pandas as pd

from sensor_simulator import generate_sensor_data
from health_monitor import calculate_health
from fault_detector import detect_faults


# ============================================================
# DATA STORAGE
# ============================================================

cycles = []
health_scores = []
records = []


# ============================================================
# SYSTEM START
# ============================================================

print("================================")
print("  PREDICTIVE MAINTENANCE SYSTEM")
print("================================")


# ============================================================
# SIMULATION
# ============================================================

for cycle in range(1, 31):

    data = generate_sensor_data(cycle)

    health_score, status, recommendation = calculate_health(data)

    faults = detect_faults(data)

    records.append({
        "cycle": cycle,
        "temperature": data["temperature"],
        "vibration": data["vibration"],
        "current": data["current"],
        "rpm": data["rpm"],
        "health_score": health_score,
        "status": status,
        "recommendation": recommendation,
        "faults": ", ".join(faults) if faults else "None"
    })

    cycles.append(cycle)
    health_scores.append(health_score)

    print(f"\n--- Cycle {cycle} ---")

    print(f"Temperature    : {data['temperature']} °C")
    print(f"Vibration      : {data['vibration']} mm/s")
    print(f"Current        : {data['current']} A")
    print(f"RPM            : {data['rpm']}")
    print(f"Health Score   : {health_score}%")
    print(f"Machine Status : {status}")
    print(f"Recommendation : {recommendation}")

    if faults:
        print("\nFAULT ALERTS:")

    for fault in faults:

        if fault.startswith("CRITICAL"):
            print(f"🔴 {fault}")

        elif fault.startswith("WARNING"):
            print(f"🟡 {fault}")

        else:
            print(f"🔵 {fault}")

# ============================================================
# SIMULATION COMPLETE
# ============================================================

print("\n================================")
print("       SIMULATION COMPLETE")
print("================================")


# ============================================================
# MAINTENANCE SUMMARY
# ============================================================

final_record = records[-1]

print("\n================================")
print("       MAINTENANCE SUMMARY")
print("================================")

print(f"Final Health Score : {final_record['health_score']}%")
print(f"Final Status       : {final_record['status']}")
print(f"Recommendation     : {final_record['recommendation']}")

if final_record["faults"] != "None":
    print(f"Detected Faults    : {final_record['faults']}")
else:
    print("Detected Faults    : None")

print("================================")

# ============================================================
# FAULT STATISTICS
# ============================================================

total_faults = 0
critical_faults = 0
warning_faults = 0

for record in records:

    if record["faults"] != "None":

        faults = record["faults"].split(", ")

        total_faults += len(faults)

        for fault in faults:

            if fault.startswith("CRITICAL"):
                critical_faults += 1

            elif fault.startswith("WARNING"):
                warning_faults += 1


print("\n================================")
print("         FAULT STATISTICS")
print("================================")

print(f"Total Faults Detected : {total_faults}")
print(f"Critical Faults       : {critical_faults}")
print(f"Warning Faults        : {warning_faults}")

print("================================")

# ============================================================
# MAINTENANCE ALERT
# ============================================================

if final_record["health_score"] < 50:

    print("\n🔴 MAINTENANCE ALERT")
    print("Machine condition is CRITICAL.")
    print("Immediate maintenance is recommended.")

elif final_record["health_score"] < 80:

    print("\n🟡 MAINTENANCE ALERT")
    print("Machine condition requires attention.")
    print("Schedule a maintenance inspection.")

else:

    print("\n🟢 MACHINE STATUS")
    print("Machine is operating within normal conditions.")


# ============================================================
# SAVE DATA TO CSV
# ============================================================

df = pd.DataFrame(records)

df.to_csv(
    "data/motor_sensor_data.csv",
    index=False
)

print("\nSensor data saved to data/motor_sensor_data.csv")


# ============================================================
# PREPARE DATA
# ============================================================

temperatures = [
    record["temperature"]
    for record in records
]

vibrations = [
    record["vibration"]
    for record in records
]

currents = [
    record["current"]
    for record in records
]

rpms = [
    record["rpm"]
    for record in records
]


# ============================================================
# CREATE DASHBOARD
# ============================================================

fig = plt.figure(
    figsize=(16, 12)
)

fig.suptitle(
    "PREDICTIVE MAINTENANCE — INDUSTRIAL MOTOR DASHBOARD",
    fontsize=20,
    fontweight="bold",
    y=0.98
)


# ============================================================
# 1. HEALTH SCORE — LONG GRAPH
# ============================================================

ax1 = plt.subplot2grid(
    (3, 2),
    (0, 0),
    colspan=2
)

ax1.plot(
    cycles,
    health_scores,
    marker="o",
    linewidth=2.5,
    markersize=5
)

ax1.set_title(
    "INDUSTRIAL MOTOR HEALTH MONITORING",
    fontsize=12,
    fontweight="normal",
    pad=8
)

ax1.set_ylabel(
    "HEALTH SCORE (%)",
    fontsize=9,
    labelpad=10
)

ax1.set_ylim(0, 105)

ax1.set_xticks(
    range(0, 31, 5)
)

# Machine health zones
ax1.axhspan(
    80,
    105,
    alpha=0.08
)

ax1.axhspan(
    50,
    80,
    alpha=0.08
)

ax1.axhspan(
    0,
    50,
    alpha=0.08
)

# Zone boundaries
ax1.axhline(
    80,
    linestyle="--",
    linewidth=1
)

ax1.axhline(
    50,
    linestyle="--",
    linewidth=1
)

ax1.grid(
    True,
    alpha=0.3
)

# ============================================================
# 2. TEMPERATURE
# ============================================================

ax2 = plt.subplot2grid(
    (3, 2),
    (1, 0)
)

ax2.plot(
    cycles,
    temperatures,
    marker="o",
    linewidth=2.2,
    markersize=5
)

ax2.set_title(
    "MOTOR TEMPERATURE TREND",
    fontsize=12,
    fontweight="normal",
    pad=8
)

ax2.set_ylabel(
    "TEMPERATURE (°C)",
    fontsize=9,
    labelpad=10
)

ax2.set_xlabel(
    "SIMULATION CYCLE",
    fontsize=9
)

ax2.set_xticks(
    range(0, 31, 5)
)

ax2.grid(
    True,
    alpha=0.3
)


# ============================================================
# 3. VIBRATION
# ============================================================

ax3 = plt.subplot2grid(
    (3, 2),
    (1, 1)
)

ax3.plot(
    cycles,
    vibrations,
    marker="o",
    linewidth=2.2,
    markersize=5
)

ax3.set_title(
    "MOTOR VIBRATION TREND",
    fontsize=12,
    fontweight="normal",
    pad=8
)

ax3.set_ylabel(
    "VIBRATION (MM/S)",
    fontsize=9,
    labelpad=10
)

ax3.set_xlabel(
    "SIMULATION CYCLE",
    fontsize=9
)

ax3.set_xticks(
    range(0, 31, 5)
)

ax3.grid(
    True,
    alpha=0.3
)


# ============================================================
# 4. CURRENT
# ============================================================

ax4 = plt.subplot2grid(
    (3, 2),
    (2, 0)
)

ax4.plot(
    cycles,
    currents,
    marker="o",
    linewidth=2.2,
    markersize=5
)

ax4.set_title(
    "MOTOR CURRENT TREND",
    fontsize=12,
    fontweight="normal",
    pad=8
)

ax4.set_ylabel(
    "CURRENT (A)",
    fontsize=9,
    labelpad=10
)

ax4.set_xlabel(
    "SIMULATION CYCLE",
    fontsize=9
)

ax4.set_xticks(
    range(0, 31, 5)
)

ax4.grid(
    True,
    alpha=0.3
)


# ============================================================
# 5. RPM
# ============================================================

ax5 = plt.subplot2grid(
    (3, 2),
    (2, 1)
)

ax5.plot(
    cycles,
    rpms,
    marker="o",
    linewidth=2.2,
    markersize=5
)

ax5.set_title(
    "MOTOR RPM TREND",
    fontsize=12,
    fontweight="normal",
    pad=8
)

ax5.set_ylabel(
    "RPM",
    fontsize=9,
    labelpad=10
)

ax5.set_xlabel(
    "SIMULATION CYCLE",
    fontsize=9
)

ax5.set_xticks(
    range(0, 31, 5)
)

ax5.grid(
    True,
    alpha=0.3
)


# ============================================================
# TICK LABEL SIZE
# ============================================================

for ax in [ax1, ax2, ax3, ax4, ax5]:

    ax.tick_params(
        axis="x",
        labelsize=8
    )

    ax.tick_params(
        axis="y",
        labelsize=8
    )


# ============================================================
# DASHBOARD SPACING
# ============================================================

plt.subplots_adjust(
    top=0.91,
    bottom=0.08,
    left=0.08,
    right=0.97,
    hspace=0.45,
    wspace=0.20
)

# ============================================================
# FINAL STATUS ON DASHBOARD
# ============================================================

fig.text(
    0.5,
    0.015,
    f"FINAL STATUS: {final_record['status']}   |   "
    f"HEALTH: {final_record['health_score']}%   |   "
    f"TOTAL FAULTS: {total_faults}",
    ha="center",
    fontsize=11,
    fontweight="bold"
)


# ============================================================
# DISPLAY DASHBOARD
# ============================================================

plt.show()