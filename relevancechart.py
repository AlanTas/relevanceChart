import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter

# So pandas prints the whole dataframe
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

nomes = ["Chart Title", "Chart type", "Y axis unity", "Bar values", "Y and X axis labels", "Bars/Groups labels",
         "Chart legend", "Min/Max values", "Increment value", "Tendency", "Mean", "Std dev", "Colors"]
data = pd.read_csv('form.csv', usecols=[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], names=nomes, header=0)
totalAnswers = len(data)
print(data.head())
print(totalAnswers)

percentages = []
for i in range(len(nomes)):
    low = len(data[(data[nomes[i]] == 1) | (data[nomes[i]] == 2)])
    medium = len(data[data[nomes[i]] == 3])
    high = len(data[(data[nomes[i]] == 4) | (data[nomes[i]] == 5)])

    low = (low * 100) / totalAnswers
    medium = (medium * 100) / totalAnswers
    high = (high * 100) / totalAnswers

    percentages.append([low, medium, high, nomes[i]])

print(percentages)
lowP = []
mediumP = []
highP = []
nome = []

percentages = sorted(percentages, key=lambda x: x[2], reverse=True)

for i in range(len(percentages)):
    lowP.append(percentages[i][0])
    mediumP.append(percentages[i][1])
    highP.append(percentages[i][2])
    nome.append(percentages[i][3])

plt.style.use("ggplot")
plt.figure(figsize=(7, 6))
p1 = plt.bar(nome, lowP, color='#F44336', label="Low relevance (1, 2)")
p2 = plt.bar(nome, mediumP, bottom=np.array(lowP), color='#FFEB3B', label="Medium relevance (3)")
p3 = plt.bar(nome, highP, bottom=np.array(mediumP) + np.array(lowP), color='#4CAF50', label="High relevance (4, 5)")
plt.legend(bbox_to_anchor=(0., 1.0, 1, .106), loc='center',
           ncol=3, borderaxespad=0)
plt.xticks(nome, rotation=-45, horizontalalignment='left')
plt.axhline(y=50, c='black', linestyle='--')
plt.text(-2, 49, "50%")
plt.title('Relevance Percentages', y=1.12)
locs, labels = plt.yticks()
for i in range(len(labels)):
    labels[i] = str(locs[i]) + "%"
plt.yticks(locs[:-1], labels[:-1])
plt.show()
