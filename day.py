import re
import matplotlib.pyplot as plt

fname = "mbox.txt"
fhand = open(fname)
day = []
count = 0

for line in fhand:
    words = line.split()
    for i in words:
        if re.search('From$', i):
            count = 1
        if re.search('Mon$|Tue$|Wed$|Thu$|Fri$|Sat$|Sun$',i) and count == 1:
            day.append(i)
            count += 1

data = day
plt.hist(data, bins='auto', color='skyblue', edgecolor='black')
plt.xlabel('Days of the week')
plt.xticks(rotation=90)
plt.title('Emails by day of the week')
plt.savefig('Day_emails.png')
plt.show()
