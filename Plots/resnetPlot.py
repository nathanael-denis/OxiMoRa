import matplotlib.pyplot as plt
import numpy as np

# F1-scores per round for each ResNet variant
f1_scores = {
    "ResNet-18": [0.8914, 0.8679, 0.9073, 0.9079, 0.8841, 0.8985, 0.8938, 0.9128, 0.8953, 0.8953],
    "ResNet-34": [0.899, 0.9208, 0.9208, 0.906, 0.906, 0.9108, 0.9108, 0.9127, 0.8307, 0.9224],
    "ResNet-50": [0.9099, 0.9099, 0.9097, 0.8860, 0.9077, 0.8934, 0.9210, 0.9210, 0.9210, 0.9066],
    "ResNet-101": [0.9083, 0.8872, 0.9083, 0.9083, 0.9068, 0.9068, 0.9068, 0.9068, 0.905, 0.8998],
}

# Compute min, average, and max for each ResNet
resnets = list(f1_scores.keys())
min_scores = [min(scores) for scores in f1_scores.values()]
avg_scores = [np.mean(scores) for scores in f1_scores.values()]
max_scores = [max(scores) for scores in f1_scores.values()]

# Rust-themed contrasting colors
min_color = '#d17a52'    # Light, orange rust
avg_color = '#a3402a'    # Strong, warm rust
max_color = '#5b1e0e'    # Deep, dark rust

# Plotting
x = np.arange(len(resnets))
width = 0.2

fig, ax = plt.subplots()
ax.bar(x - width, min_scores, width, label='Min F1-score', color=min_color)
ax.bar(x, avg_scores, width, label='Avg F1-score', color=avg_color)
ax.bar(x + width, max_scores, width, label='Max F1-score', color=max_color)

# Labels and formatting
ax.set_xlabel('ResNet Variant')
ax.set_ylabel('F1-score')
ax.set_title('Min, Average, and Max F1-score per ResNet')
ax.set_xticks(x)
ax.set_xticklabels(resnets)
ax.set_ylim(0.8, 1.0)
ax.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
