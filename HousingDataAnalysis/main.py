import numpy as np
import matplotlib.pyplot as plt
import os
import csv
def parseData(path, city):
    data = list(csv.reader(open('./data/' + path, 'rt'), delimiter='\t'))
    ret = []
    for i in range(len(data)):
        #print(data[i][1], " ", data[i][2])
        if (data[i][1] == city and data[i][2] == "Total"):
            ret.append(data[i][3])
            ret.append(data[i][4])
            ret.append(data[i][5])
            ret.append(data[i][6])
            #print(city, " Singles: ", data[i][3])
            #print(city, " Semis: ", data[i][4])
            #print(city, " Row: ", data[i][5])
            #print(city, " Apartment/Other: ", data[i][6])
    print(ret)
    return ret
Montreal_Singles = []
Montreal_Semis = []
Montreal_Rows = []
Montreal_Apts = []
Ottawa_Singles = []
Ottawa_Semis = []
Ottawa_Rows = []
Ottawa_Apts = []
Toronto_Singles = []
Toronto_Semis = []
Toronto_Rows = []
Toronto_Apts = []
for file in os.listdir("./Data/"):
    Montreal_Single, Montreal_Semi, Montreal_Row, Montreal_Apt = parseData(file, "MontrÃ©al")
    Montreal_Singles.append(Montreal_Single)
    Montreal_Semis.append(Montreal_Semi)
    Montreal_Rows.append(Montreal_Row)
    Montreal_Apts.append(Montreal_Apt)
    Ottawa_Single, Ottawa_Semi, Ottawa_Row, Ottawa_Apt = parseData(file, "Ottawa")
    Ottawa_Singles.append(Ottawa_Single)
    Ottawa_Semis.append(Ottawa_Semi)
    Ottawa_Rows.append(Ottawa_Row)
    Ottawa_Apts.append(Ottawa_Apt)
    Toronto_Single, Toronto_Semi, Toronto_Row, Toronto_Apt = parseData(file, "Toronto")
    Toronto_Singles.append(Toronto_Single)
    Toronto_Semis.append(Toronto_Semi)
    Toronto_Rows.append(Toronto_Row)
    Toronto_Apts.append(Toronto_Apt)

#fig, axs = plt.subplots(1, 2)
#axs[0].hist(x, 20)
#axs[1].hist(y, 20)
#print(fig)
#plt.show()
