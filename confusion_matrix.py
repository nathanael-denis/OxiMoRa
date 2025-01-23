import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Confusion matrix data
confusion_matrix = np.array([[161, 17, 0],
                              [14, 123, 41],
                              [0, 11, 167]])

# Labels for the confusion matrix axes
labels = ['PIPE_RUSTY_SCREWS', 'PIPE_EMPTY', 'PIPE_RUSTLESS_SCREWS']

# Plotting the confusion matrix with increased width
plt.figure(figsize=(10, 4))  # Wider figure for horizontal emphasis
ax = sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="YlOrBr", 
                 xticklabels=labels, yticklabels=labels, cbar=False)

# Adjusting the aspect ratio for horizontal stretching
ax.set_aspect(0.5)  # Aspect ratio less than 1 stretches it horizontally

# Axis labels and title
plt.xlabel('Predicted Labels', fontsize=12)
plt.ylabel('True Labels', fontsize=12)
plt.title('Confusion Matrix', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()
