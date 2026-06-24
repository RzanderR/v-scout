import csv
from pathlib import Path

def save_detections(output_file, detections):
    output_path = Path(output_file)

    with open(output_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "frame_id",
                "class_name",
                "confidence",
                "x_min",
                "y_min",
                "x_max",
                "y_max",
            ],
        )

        writer.writeheader()

        for detection in detections:
            writer.writerow(detection)

    print(f"Saved {len(detections)} detection(s) to {output_path}")

fake_detections = [
    {
        "frame_id": 1,
        "class_name": "drone",
        "confidence": 0.92,
        "x_min": 120,
        "y_min": 80,
        "x_max": 200,
        "y_max": 160,
    },
    {
        "frame_id": 2,
        "class_name": "truck",
        "confidence": 0.87,
        "x_min": 300,
        "y_min": 220,
        "x_max": 420,
        "y_max": 330,
    },
]

save_detections("data/detections.csv", fake_detections)