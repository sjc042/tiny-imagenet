import os
import shutil

current = os.path.join('../data', 'tiny-imagenet-200')

# Training data
train_dir = os.path.join(current, 'train')
for DIR in os.listdir(train_dir):
    dir_path = os.path.join(train_dir, DIR)
    os.chdir(dir_path)
    for file_name in os.listdir(os.path.join(dir_path, 'images')):
        shutil.move(os.path.join(dir_path, 'images', file_name), dir_path)
    shutil.rmtree(os.path.join(dir_path, 'images'))
    os.chdir(current)

# Validation data
val_dir = os.path.join(current, 'val')
annotate_file = os.path.join(val_dir, 'val_annotations.txt')

with open(annotate_file, 'r') as file:
    lines = file.readlines()

for line in lines:
    file_name, directory = line.split()[:2]
    directory_path = os.path.join(val_dir, directory)
    os.makedirs(directory_path, exist_ok=True)
    shutil.move(os.path.join(val_dir, 'images', file_name), directory_path)

shutil.rmtree(os.path.join(val_dir, 'images'))
print("done")