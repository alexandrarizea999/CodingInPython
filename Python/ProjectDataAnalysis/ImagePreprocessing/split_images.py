import os
import shutil
import random

# Folder that contains 'Yes' and 'No'
DATASET_DIR = "data"
OUTPUT_DIR = "split_data"
TRAIN_RATIO = 0.8  # 80% train, 20% test

os.makedirs(os.path.join(OUTPUT_DIR, "train", "Yes"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "train", "No"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "test", "Yes"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "test", "No"), exist_ok=True)

for label in ["Yes", "No"]:
    img_dir = os.path.join(DATASET_DIR, label)
    images = os.listdir(img_dir)
    random.shuffle(images)
    split_idx = int(len(images) * TRAIN_RATIO)
    train_imgs = images[:split_idx]
    test_imgs = images[split_idx:]

    for img in train_imgs:
        src = os.path.join(img_dir, img)
        dst = os.path.join(OUTPUT_DIR, "train", label, img)
        shutil.copy2(src, dst)

    for img in test_imgs:
        src = os.path.join(img_dir, img)
        dst = os.path.join(OUTPUT_DIR, "test", label, img)
        shutil.copy2(src, dst)

print("Dataset split into train and test sets.")

train_yes = len(os.listdir(os.path.join(OUTPUT_DIR, "train", "Yes")))
train_no = len(os.listdir(os.path.join(OUTPUT_DIR, "train", "No")))
test_yes = len(os.listdir(os.path.join(OUTPUT_DIR, "test", "Yes")))
test_no = len(os.listdir(os.path.join(OUTPUT_DIR, "test", "No")))

print(f"Train set: Yes = {train_yes}, No = {train_no}")
print(f"Test set: Yes = {test_yes}, No = {test_no}")
