import re
import urllib.request
import matplotlib.pyplot as plt
from urllib.request import Request, urlopen

req = Request('https://en.wikipedia.org/wiki/Nikola_Tesla', headers = {'User-Agent': 'Mozilla/5.0'})

hand = urlopen(req)
dates = []
for line in hand:
    line = line.decode().strip()
    date_result = re.findall('1[8-9][0-9]{2}', line)
    if date_result != []:
        for date in date_result:
            dates.append(date)
print(dates)

data = dates
plt.hist(data, bins='auto', color='skyblue', edgecolor='black')
plt.xlabel('Dates Mentioned')
plt.xticks(rotation=90)
plt.title('Dates mentioned on Nikola Tesla Wikipedia')
plt.show()
plt.savefig('tesla_dates.png')
