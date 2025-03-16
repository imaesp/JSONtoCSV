import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        rows = []

        for item in data:
            picture_urls = [picture['originalUrl'] for picture in item.get('pictures', [])]

            if picture_urls:
                item['pictures'] = picture_urls

            rows.append(item)

        headers = rows[0].keys()

        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(rows)

        print(f"Data successfully written to {csv_file_path}")
    else:
        print("Error: Unexpected format.")


json_to_csv('', '')

