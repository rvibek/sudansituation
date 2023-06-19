import requests
import csv
from datetime import datetime



# URL of the CSV file
url = "https://static.dwcdn.net/data/2D1Qs.csv"


# Download the CSV file
response = requests.get(url)
data = response.content.decode('utf-8')


def update_latest():
    # Path to the local CSV file
    filename = "sudansituation_data_latest.csv"
    # Write the downloaded data to the local CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        reader = csv.reader(data.splitlines())
        for row in reader:
            writer.writerow(row)

def update_historical():
    # Path to the local CSV file
    filename = "sudansituation_data_historical.csv"
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        reader = csv.reader(data.splitlines())
        for row in reader:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
            writer.writerow([timestamp] + row)  # Add the timestamp as the first column in each row

update_latest()
update_historical()

print("Data updated!!")