import os

folders = [
    "train/images",
    "valid/images",
    "test/images"
]

for folder in folders:
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = [] #keeping only valid lines
        for line in lines:
            parts = line.strip().split()
            if int(parts[0]) > 1:
                continue
            new_lines.append(line) 

        with open(file_path, "w") as f:
            f.writelines(new_lines)
print("All labels fixed successfully!") 