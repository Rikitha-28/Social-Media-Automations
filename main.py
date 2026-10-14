import csv

filename = "scheduled_posts (2).csv"

with open(filename, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
