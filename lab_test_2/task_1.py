import csv

# Read input from 'input.csv' file
with open('input.csv', 'r', newline='') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Sort rows: dept ascending, salary descending
rows_sorted = sorted(
    rows,
    key=lambda r: (r['dept'], -int(r['salary']))
)

# Print output in terminal (just a space after each comma, no extra text)
for row in rows_sorted:
    print(',: - task_1.py:16'.join(row[field] for field in reader.fieldnames))