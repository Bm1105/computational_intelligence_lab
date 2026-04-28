import csv
import math

def distance_metric(a, b, r):
    total = sum(abs(x - y) ** r for x, y in zip(a, b))
    return total ** (1 / r)

def load_data(filename):
    data = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            feat_headers = header[4:8]
            for row in reader:
               features = list(map(float, row[4:8]))
               label = row[-1]
               data.append((features, label))
            data = data[:15]
        return data, feat_headers
    except FileNotFoundError:
        print("Error: data.csv not found.")
        return [], []

def normalize(data):
    feature_count = len(data[0][0])
    mins = [min(row[0][i] for row in data) for i in range(feature_count)]
    maxs = [max(row[0][i] for row in data) for i in range(feature_count)]
    normalized_list = []
    for features, label in data:
        norm_features = []
        for i in range(feature_count):
            if maxs[i] != mins[i]:
                norm_features.append((features[i] - mins[i]) / (maxs[i] - mins[i]))
            else:
                norm_features.append(0.0)
        normalized_list.append((features, norm_features, label))
    return normalized_list, mins, maxs

def main():
    raw_tuples, feat_headers = load_data("data.csv")
    if not raw_tuples: return

    data, mins, maxs = normalize(raw_tuples)

    print("\n--- Features and Ranges ---")
    for i in range(len(feat_headers)):
        print(f"{feat_headers[i]:<25}: {mins[i]} to {maxs[i]}")

    query = []
    print("\n--- Enter Test Point ---")
    for i in range(len(feat_headers)):
        val = float(input(f"Enter {feat_headers[i]}: "))
        query.append(val)

    norm_query = []
    for i in range(len(query)):
        if maxs[i] != mins[i]:
            norm_query.append((query[i] - mins[i]) / (maxs[i] - mins[i]))
        else:
            norm_query.append(0.0)

    print("\nDistance Metric: 1. Euclidean (r=2), 2. Manhattan (r=1)")
    r_val = 2 if input("Choice: ") == "1" else 1

    distances = []
    for original, normalized, label in data:
        d = distance_metric(normalized, norm_query, r_val)
        distances.append((original, normalized, d, label))
    distances.sort(key=lambda x: x[2])

    print(f"\n{'Rank':<5} | {'Original Point':<30} | {'Normalized Point':<40} | {'Dist':<8} | {'Class'}")
    print("-" * 110)
    for i, (orig, norm, d, label) in enumerate(distances, 1):
        o_str = str([round(x, 1) for x in orig])
        n_str = str([round(x, 2) for x in norm])
        print(f"{i:<5} | {o_str:<30} | {n_str:<40} | {d:<8.4f} | {label}")

    summary_history = []

    while True:
        k_val = int(input("\nEnter K value (-1 to exit): "))
        if k_val == -1: break
        if k_val > 15: k_val = 15

        neighbors = distances[:k_val]

        print(f"\n--- Top {k_val} Neighbors Details ---")
        print(f"{'Rank':<5} | {'Original Point':<30} | {'Dist':<8} | {'Class'}")
        print("-" * 65)

        counts = {}
        weighted_scores = {}
        for i, (orig, norm, d, label) in enumerate(neighbors, 1):
            o_str = str([round(x, 1) for x in orig])
            print(f"{i:<5} | {o_str:<30} | {d:<8.4f} | {label}")

            counts[label] = counts.get(label, 0) + 1
            weight = 1 / (d + 1e-9)
            weighted_scores[label] = weighted_scores.get(label, 0) + weight

        unweighted_pred = max(counts, key=counts.get)
        weighted_pred = max(weighted_scores, key=weighted_scores.get)
        summary_history.append((k_val, unweighted_pred, weighted_pred))

        rounded_weights = {k: round(v, 4) for k, v in weighted_scores.items()}
        print(f"\nUnweighted Counts: {counts} -> Prediction: {unweighted_pred}")
        print(f"Weighted Scores: {rounded_weights} -> Prediction: {weighted_pred}")

if __name__ == "__main__":
    main()
