''' template for counting how many times Esther appears in each chapter'''
import re
import urllib.request
import matplotlib.pyplot as plt

hand = urllib.request.urlopen('https://www.gutenberg.org/cache/epub/1023/pg1023.txt')

chapter = 0
chapter_list = [0]
counts_esther = [0] 

chapterG = 0
chapter_listG = [0]
counts_Guppy = [0]

for line in hand:
    line = line.decode().strip()
    new_chapter = re.search('CHAPTER', line)
    if new_chapter: 
        chapter += 1 
        chapter_list.append(chapter)
        counts_esther.append(0)
         
    num_counts_e = len(re.findall('Esther',line))
    counts_esther[chapter] += num_counts_e

    new_chapterG = re.search('CHAPTER', line)
    if new_chapterG: 
        chapterG += 1 
        chapter_listG.append(chapterG)
        counts_Guppy.append(0)
        
    num_counts_G = len(re.findall('Guppy',line))
    counts_Guppy[chapterG] += num_counts_G

#print(counts_esther)
#print(counts_Guppy)


# your code here - display a plot with chapter on the x axis, counts_esther on the y axis
x = chapter_list
y = counts_esther
z = counts_Guppy
plt.plot(x,y, color='red')
plt.plot(x,z, color='blue')
plt.xlabel('Chapter')
plt.ylabel('Esther and Guppy count')
plt.legend(['Esther', 'Guppy'])
plt.title('Name count per chapter')
plt.show()
plt.savefig('Esther_Guppy.png')
