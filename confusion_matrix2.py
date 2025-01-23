import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# Define the confusion matrix
confusion_matrix = np.array([
    [113, 1, 0, 0],
    [0, 110, 4, 0],
    [0, 7, 89, 18],
    [0, 0, 7, 107]
])

# Define class labels
class_labels = ['1 Screw', '2 Screws', '3 Screws', '4 Screws']

# Create a confusion matrix display
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=class_labels)

# Plot the confusion matrix
fig, ax = plt.subplots(figsize=(8, 4))  # Wider figure, smaller height for horizontal emphasis
disp.plot(ax=ax, cmap="YlOrBr", colorbar=False)

# Adjust the aspect ratio to stretch the matrix horizontally
ax.set_aspect(0.5)  # Aspect ratio less than 1 makes it horizontally stretched

# Reset label font sizes to default
ax.set_xticklabels(class_labels, fontsize=10, rotation=45)  # Default font size, rotate x-ticks
ax.set_yticklabels(class_labels, fontsize=10)
plt.xlabel("Predicted Labels", fontsize=12)  # Default font size
plt.ylabel("True Labels", fontsize=12)

# Enhance plot aesthetics
plt.title("Confusion Matrix", fontsize=14)  # Normal title size
plt.tight_layout()

# Save the figure for use in LaTeX
plt.savefig("confusion_matrix_horizontal.pdf", bbox_inches="tight")  # Save in PDF format for LaTeX
plt.show()
