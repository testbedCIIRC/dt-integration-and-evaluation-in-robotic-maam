import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot


def read_deviation_from_file(filename):
    with open(filename, 'r') as file:
        capture = False
        deviations = []
        for line in file:
            if 'XC            YC             ZC           Deviation' in line:
                capture = True
                continue
            if '==================================================================' in line:
                capture = False
            if capture:
                parts = line.strip().split(',')
                if len(parts) > 3:
                    deviation_string = parts[-1].strip().split()
                    if deviation_string:
                        deviation = deviation_string[-1]
                        if deviation.replace('.', '', 1).replace('-', '', 1).isdigit():
                            deviations.append(float(deviation))
    return deviations

# Read deviations from files
files = ["Propeller_CAD_IPW.txt", "Propeller_SCAN_IPW.txt", "Propeller_SCAN_CAD.txt", "Tube_CAD_IPW.txt", "Tube_SCAN_IPW.txt", "Tube_SCAN_CAD.txt"]
deviations_dict = {file: read_deviation_from_file(file) for file in files}

# Předpokládáme, že máte již nahrány odchylky do dictionary `deviations_dict`
file_names = [
    "Propeller_CAD_IPW.txt", 
    "Propeller_SCAN_IPW.txt", 
    "Propeller_SCAN_CAD.txt", 
    "Tube_CAD_IPW.txt", 
    "Tube_SCAN_IPW.txt", 
    "Tube_SCAN_CAD.txt"
]

# Definujte nové názvy pro křivky
curve_names = {
    "Propeller_CAD_IPW.txt": "Propeller: CAD vs. IPW",
    "Propeller_SCAN_IPW.txt": "Propeller: Scan vs. IPW",
    "Propeller_SCAN_CAD.txt": "Propeller: Scan vs. CAD",
    "Tube_CAD_IPW.txt": "Tube: CAD vs. IPW",
    "Tube_SCAN_IPW.txt": "Tube: Scan vs. IPW",
    "Tube_SCAN_CAD.txt": "Tube: Scan vs. CAD"
}

# Definice tolerance a výpočet procent
tolerance_ranges = np.arange(0.0, 3.03, 0.03)
results = {}

for file in file_names:
    deviations = np.array(deviations_dict[file])
    percentages = []
    for tol in tolerance_ranges:
        count_within_tol = np.sum((deviations >= -tol) & (deviations <= tol))
        percentage = count_within_tol / len(deviations) * 100
        percentages.append(percentage)
    results[curve_names[file]] = percentages  # Použití nového názvu pro klíč v results

# Plot the results
fig = go.Figure()
for curve_label, percentages in results.items():
    fig.add_trace(go.Scatter(x=tolerance_ranges, y=percentages, mode='lines+markers', name=curve_label))

fig.update_layout(
    font_size=25,
    xaxis_title='Tolerance (mm)',
    yaxis_title='Percentage of Points (%)',
    legend_title='From Deviation Analysis of:'
)

plot(fig, filename='Deviation Analysis.html', auto_open=True)