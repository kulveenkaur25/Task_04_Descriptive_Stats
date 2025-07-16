import csv
import argparse
import math
from collections import defaultdict, Counter

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def compute_stats(values):
    numeric_values = [float(v) for v in values if is_float(v)]
    count = len(values)
    mean = sum(numeric_values) / len(numeric_values) if numeric_values else None
    minimum = min(numeric_values) if numeric_values else None
    maximum = max(numeric_values) if numeric_values else None
    stddev = (math.sqrt(sum((x - mean)**2 for x in numeric_values) / len(numeric_values))
              if numeric_values else None)
    unique = set(values)
    most_common = Counter(values).most_common(1)[0][0] if values else None

    return {
        "count": count,
        "mean": mean,
        "min": minimum,
        "max": maximum,
        "std": stddev,
        "unique": len(unique),
        "most_frequent": most_common
    }

def summarize_by_group(data, group_keys, headers):
    grouped = defaultdict(list)
    for row in data:
        key = tuple(row[k] for k in group_keys)
        grouped[key].append(row)

    for group_key, rows in grouped.items():
        print(f"\n--- Group: {group_key} ---")
        for col in headers:
            col_values = [r[col] for r in rows if r[col] != '']
            stats = compute_stats(col_values)
            print(f"\nColumn: {col}")
            print(stats)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to CSV file')
    parser.add_argument('--group_by', nargs='+', help='Group by column(s)')
    args = parser.parse_args()

    with open(args.input, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
        headers = reader.fieldnames

    summarize_by_group(data, args.group_by, headers)

if __name__ == "__main__":
    main()
