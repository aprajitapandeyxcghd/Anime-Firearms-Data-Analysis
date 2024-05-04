import requests
import mysql.connector
from bs4 import BeautifulSoup
import pandas as pd

# Connect to MySQL
cnx = mysql.connector.connect(user='root', password='JOSH@69sit', host='localhost', database='firearms_data')
cursor = cnx.cursor()

# Retrieve data from link
url = 'https://erich-springer.livejournal.com/22885.html'
response = requests.get(url)
content = response.content.decode('utf-8')

# Parse data using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Extract firearms data
firearms_data = []
for tr in soup.find_all('tr')[1:]:
  tds = tr.find_all('td')
  anime_character = tds[0].text.strip()
  firearm_name = tds[1].text.strip()
  firearm_type = tds[2].text.strip()
  firearm_manufacturer = tds[3].text.strip()
  firearm_caliber = tds[4].text.strip()
  firearm_capacity = int(tds[5].text.strip())
  firearm_length = float(tds[6].text.strip().replace('in', '').replace('"', ''))
  firearm_weight = float(tds[7].text.strip().replace('oz', '').replace('lb', ''))
  firearm_features = tds[8].text.strip()
  firearms_data.append((anime_character, firearm_name, firearm_type, firearm_manufacturer, firearm_caliber, firearm_capacity, firearm_length, firearm_weight, firearm_features))

# Insert data into MySQL
insert_query = '''
INSERT INTO firearms (anime_character, firearm_name, firearm_type, firearm_manufacturer, firearm_caliber, firearm_capacity, firearm_length, firearm_weight, firearm_features)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
cursor.executemany(insert_query, firearms_data)
cnx.commit()

# Query firearms data from MySQL
query = '''
SELECT anime_character, firearm_name, firearm_type, firearm_manufacturer, firearm_caliber, firearm_capacity, firearm_length, firearm_weight, firearm_features FROM firearms
'''
cursor.execute(query)

# Fetch data as a list of tuples
data = cursor.fetchall()

# Convert the list of tuples to a Pandas DataFrame
df = pd.DataFrame(data, columns=['anime_character', 'firearm_name', 'firearm_type', 'firearm_manufacturer', 'firearm_caliber', 'firearm_capacity', 'firearm_length', 'firearm_weight', 'firearm_features'])

# Perform data analysis using Pandas
# ...

# Close MySQL connection
cursor.close()
cnx.close()