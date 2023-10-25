from src.lib.geo_db_cities import geoDbData
import json
import logging

logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

logging.debug('Start Program')

for item in geoDbData['data']:
    print(item["name"])

while True:
    name_to_find = input("\nEnter a city name from the list above: ")

    logging.info(f"User Input: {name_to_find}")

    filtered_objects = list(filter(lambda x: x["name"] == name_to_find, geoDbData["data"]))

    if (not filtered_objects):
        logging.info('User did not enter a valid name')
        print("Not a valid city, try again.")
    else:
        break

print(json.dumps(filtered_objects, indent=4))


logging.debug('End Program')