import os
import shutil
import random
import cv2
import numpy as np


def read_image(path):
    # Read image as BGR
    img = cv2.imread(path)
    return img


def resize_image(img, new_size=(224, 224)):
    # Nearest neighbor resizing
    h, w = img.shape[:2]
    new_h, new_w = new_size
    resized = np.zeros((new_h, new_w, 3), dtype=img.dtype)
    for i in range(new_h):
        for j in range(new_w):
            x = int(i * h / new_h)
            y = int(j * w / new_w)
            resized[i, j] = img[x, y]
    return resized


def to_grayscale(img):
    # grayscale conversion using luminosity method
    gray = np.zeros(img.shape[:2], dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            b, g, r = img[i, j]
            gray[i, j] = int(0.114 * b + 0.587 * g + 0.299 * r)
    return gray


def normalize(img):
    # Normalize to [0, 1]
    return img / 255.0


if __name__ == "__main__":
    folder = "data/Yes"
    images = [
        f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
    img_name = random.choice(images)
    img_path = os.path.join(folder, img_name)
    print(f"Selected image: {img_path}")

    img = read_image(img_path)
    print("Original shape:", img.shape)

    resized = resize_image(img, (224, 224))
    print("Resized shape:", resized.shape)

    gray = to_grayscale(resized)
    print("Grayscale shape:", gray.shape)

    norm = normalize(gray)
    print("Normalized min/max:", norm.min(), norm.max())

    # Save results
    cv2.imwrite("step_resized.jpg", resized)
    cv2.imwrite("step_gray.jpg", gray)
    cv2.imwrite("step_norm.jpg", (norm * 255).astype(np.uint8))
