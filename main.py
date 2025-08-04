import json
from datetime import datetime


def convert_iso_to_ms(iso_str):
    """Convert ISO 8601 timestamp to milliseconds"""
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(dt.timestamp() * 1000)


def load_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def unify_data(data1, data2):
    unified = []

    # Convert data1 (ISO timestamps)
    for entry in data1:
        unified.append({
            "timestamp": convert_iso_to_ms(entry["timestamp"]),
            "value": entry["value"]
        })

    # Add data2 (already in ms)
    for entry in data2:
        unified.append(entry)

    # Sort by timestamp (optional but recommended)
    unified.sort(key=lambda x: x["timestamp"])
    return unified


def main():
    # Load input files
    data1 = load_json_file('data-1.json')
    data2 = load_json_file('data-2.json')

    # Process and unify
    result = unify_data(data1, data2)

    # Output result
    with open('output.json', 'w') as f:
        json.dump(result, f, indent=2)

    print("✅ Unification complete. Output saved to output.json")


if __name__ == "__main__":
    main()
