import matplotlib.pyplot as plt

# Use larger fonts for visibility in print
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12
})

# F1-score data for each scenario
# Scenario 1: Detection
scenario_1_f1 = [0.9804, 0.9804, 0.9888, 0.9916, 0.9916, 0.9776, 0.9608, 0.9721, 0.9804, 0.9888]
# Scenario 2: Number of screws
scenario_3_f1 = [0.8551, 0.8641, 0.8668, 0.8886, 0.8793, 0.8417, 0.8529, 0.8577, 0.8651, 0.8691]
# Scenario 3: Penetrability
scenario_2_f1 = [0.8997, 0.904, 0.8858, 0.8919, 0.8963, 0.894, 0.8932, 0.9178, 0.9113, 0.90118]

rounds = list(range(1, 11))

# Rust-inspired colors
colors = {
    'Scenario 1: Detection': 'peru',
    'Scenario 2: Number of Screws': 'sienna',
    'Scenario 3: Penetrability': 'darkred'
}

# Filenames for saving
filenames = {
    'Scenario 1: Detection': 'f1_detection.png',
    'Scenario 2: Number of Screws': 'f1_screws.png',
    'Scenario 3: Penetrability': 'f1_rust_levels.png'
}

# Plotting and saving function
def plot_f1(f1_scores, scenario_name):
    plt.figure(figsize=(6, 4))
    color = colors[scenario_name]
    plt.plot(rounds, f1_scores, marker='o', color=color, label='F1-score')
    plt.axhline(y=sum(f1_scores) / len(f1_scores), color='gray', linestyle='--', label='Mean')
    plt.xticks(rounds)
    plt.ylim(0.8, 1.0)
    plt.xlabel('Round')
    plt.ylabel('F1-score')
    plt.title(f'{scenario_name}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filenames[scenario_name], dpi=300)
    plt.close()

# Generate all three figures
plot_f1(scenario_1_f1, 'Scenario 1: Detection')
plot_f1(scenario_2_f1, 'Scenario 2: Number of Screws')
plot_f1(scenario_3_f1, 'Scenario 3: Penetrability')
