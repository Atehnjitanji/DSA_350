import re
import matplotlib.pyplot as plt

fname = "mbox.txt"
fhand = open(fname)
month = []
count = 0

for line in fhand:
    words = line.split()
    for i in words:
        if re.search('From$', i):
            count = 1
        if re.search('Jan$|Feb$|March$|Mar$|Apr$|May$|June$|Jul$|July$|Aug$|Sep$|Oct$|Nov$|Dec$',i) and count == 1:
            month.append(i)
            count += 1


data = month
plt.hist(data, bins='auto', color='skyblue', edgecolor='black')
plt.xlabel('Months')
plt.xticks(rotation=90)
plt.title('Emails by month')
plt.savefig('Months.png')
plt.show()
