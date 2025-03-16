# JSONtoCSV
This script is designed for the **PAWfect Match** project to convert pet data from a **JSON** file into a **CSV** 
It reads the JSON data, extracts image URLs from the "pictures" field (if present), and replaces the original "pictures" field with a list of extracted URLs. 
The script then writes the processed data into a CSV file, ensuring the headers match the keys of the first dictionary. 
It includes basic error handling to check if the JSON structure is as expected.
