def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)): # Start from i+1 to avoid i==j
            ratio = values[i] / (values[j] - values[i])
            results.append((i, j, ratio))
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))