import matplotlib.pyplot as plt
import numpy as np

# F1-score summary data per stack
stack_sizes = ["16", "32", "64", "128", "256"]

min_scores = [0.8315, 0.7872, 0.7113, 0.8307, 0.8274]
avg_scores = [0.83632, 0.85136, 0.87386, 0.90400, 0.88933]
max_scores = [0.8513, 0.8736, 0.8990, 0.9224, 0.9234]

# Rust-themed contrasting colors
min_color = '#d17a52'    # Light, orange rust
avg_color = '#a3402a'    # Strong, warm rust
max_color = '#5b1e0e'    # Deep, dark rust

# Plotting
x = np.arange(len(stack_sizes)) * 0.7  # Reduce horizontal spacing
width = 0.12  # Width of bars

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(x - width, min_scores, width, label='Min F1-score', color=min_color)
ax.bar(x, avg_scores, width, label='Avg F1-score', color=avg_color)
ax.bar(x + width, max_scores, width, label='Max F1-score', color=max_color)

# Font size scale (200% = doubled)
fontsize_base = 10
fontsize = int(fontsize_base * 1.6)  # 20 pt font size

ax.set_xlabel('Number of FFT Stacks', fontsize=fontsize)
ax.set_ylabel('F1-score', fontsize=fontsize)
ax.set_title('Min, Average, and Max F1-score per FFT Stack Size', fontsize=fontsize + 4)
ax.set_xticks(x)
ax.set_xticklabels(stack_sizes, fontsize=fontsize)
ax.set_ylim(0.7, 1.0)
ax.legend(fontsize=fontsize)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
