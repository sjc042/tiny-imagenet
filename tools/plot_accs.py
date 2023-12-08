import sys
import json
import matplotlib.pyplot as plt

def plot_accuracies(json_file):
    # Read JSON data from file
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    # Extracting data
    epochs = range(1, json_data["Num-Epochs"] + 1)
    train_accs = json_data["train_accs"]
    val_accs = json_data["val_accs"]

    # Plotting
    plt.plot(epochs, train_accs, label='Train Accuracy')
    plt.plot(epochs, val_accs, label='Validation Accuracy')
    plt.title('Training and Validation Accuracies')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    # Set y-axis limit to 1
    plt.ylim(0, 1)
    # Force x-axis ticks to be integers
    plt.yticks([i/20 for i in range(21)])
    plt.xticks(list(epochs))
    
    # Save the plot to a JPG file with the same name as the JSON file
    jpg_file = json_file.replace('.json', '.jpg')
    plt.savefig(jpg_file)

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py json_file")
        sys.exit(1)

    json_file = sys.argv[1]
    plot_accuracies(json_file)