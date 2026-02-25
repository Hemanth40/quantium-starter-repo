import csv
import os

# Define paths
data_folder = "./data"
output_file = "./formatted_data.csv"

with open(output_file, "w", newline="") as out:
    writer = csv.writer(out)

    # Write header
    writer.writerow(["sales", "date", "region"])

    # Loop through each file in data folder
    for file in os.listdir(data_folder):
        with open(f"{data_folder}/{file}", "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row

            for row in reader:
                product = row[0]
                price = float(row[1].replace("$", ""))
                quantity = int(row[2])
                date = row[3]
                region = row[4]

                # Only process pink morsels
                if product == "pink morsel":
                    sales = price * quantity
                    writer.writerow([sales, date, region])

print("Done! formatted_data.csv created successfully.")