import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.cbtnuggets.com/common-ports'

response = requests.get(url)

ports = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html5lib')
    table = soup.find('table')
    
    if table:
        header = [item.get_text(strip=True) for item in table.find_all('th')]
        
        rows = table.find_all('tr')[1:]
        for row in rows:
            cols = row.find_all('td')
            if cols:
                row_data = [col.get_text(strip=True) for col in cols]
                port_dict = dict(zip(header, row_data))
                ports.append(port_dict)

# Write to CSV
with open('Data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for port in ports:
        writer.writerow([port[col] for col in header])
