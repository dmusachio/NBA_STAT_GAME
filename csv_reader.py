import csv

# Specify the path to your CSV file


# Open the CSV file
def read_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data