import os

folders = [
    "dataset/train/labels",
    "dataset/valid/labels",
    "dataset/test/labels"
]

for folder in folders:
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:
            parts = line.strip().split()

            # class filter (only 0 and 1)
            if int(parts[0]) > 1:
                continue

            # bounding box values
            x, y, w, h = map(float, parts[1:])

            # ❌ remove too large boxes (bike cover kar raha hoga)
            if w > 0.6 or h > 0.6:
                continue

            new_lines.append(line)

        with open(file_path, "w") as f:
            f.writelines(new_lines)

print("Labels cleaned ")