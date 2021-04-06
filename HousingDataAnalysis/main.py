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
            
    return ret

def linearRegression(data, numOfPoints):
    sumx = 0
    sumxy = 0
    xAverage = numOfPoints/2
    yAverage = 0
    for i in range(0, numOfPoints):
        yAverage += data[i]
    yAverage = yAverage/numOfPoints
    for i in range(0, numOfPoints):
        sumx = sumx + (i - xAverage)*(i - xAverage)
        sumxy = sumxy + (i - xAverage)*(data[i] - yAverage)
    slope = (sumxy/sumx)
    c = yAverage - slope*xAverage
    return [c,(yAverage - data[0])/xAverage]

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

for i in range (0, len(Montreal_Singles)):
    Montreal_Singles[i] = int(Montreal_Singles[i].replace(',', ''))
    Toronto_Singles[i] = int(Toronto_Singles[i].replace(',', ''))
    Ottawa_Singles[i] = int(Ottawa_Singles[i].replace(',', ''))

    Montreal_Semis[i] = int(Montreal_Semis[i].replace(',', ''))
    Toronto_Semis[i] = int(Toronto_Semis[i].replace(',', ''))
    Ottawa_Semis[i] = int(Ottawa_Semis[i].replace(',', ''))

    Montreal_Rows[i] = int(Montreal_Rows[i].replace(',', ''))
    Toronto_Rows[i] = int(Toronto_Rows[i].replace(',', ''))
    Ottawa_Rows[i] = int(Ottawa_Rows[i].replace(',', ''))

    Montreal_Apts[i] = int(Montreal_Apts[i].replace(',', ''))
    Toronto_Apts[i] = int(Toronto_Apts[i].replace(',', ''))
    Ottawa_Apts[i] = int(Ottawa_Apts[i].replace(',', ''))

for i in range(0, len(Montreal_Singles)):
    MontrealAVG = Montreal_Singles[i] + Montreal_Semis[i] + Montreal_Rows[i] + Montreal_Apts[i]
    OttawaAVG = Ottawa_Singles[i] + Ottawa_Semis[i] + Ottawa_Rows[i] + Ottawa_Apts[i] 
    TorontoAVG = Toronto_Singles[i] + Toronto_Semis[i] + Toronto_Rows[i] + Toronto_Apts[i]

years = np.arange(2006, 2020, 1)
    
#================Singles Regression================#    
y_int, slope = linearRegression(Montreal_Singles, len(Montreal_Singles))
plt.plot(years, (y_int + (years-2006)*slope), 'r--')
y_int, slope = linearRegression(Toronto_Singles, len(Toronto_Singles))

plt.plot(years, (y_int + (years-2006)*slope), 'b--')
y_int, slope = linearRegression(Ottawa_Singles, len(Ottawa_Singles))

plt.plot(years, (y_int + (years-2006)*slope), 'g--')
#================Singles Regression================#
plt.plot(years, Montreal_Singles, 'r-', label='Montreal')
plt.plot(years, Toronto_Singles, 'b-', label='Toronto')
plt.plot(years, Ottawa_Singles, 'g-', label='Ottawa')
plt.ylabel("Number of Dwellings")
plt.xlabel("Year")
plt.title("Number of Dwellings(Single Detatched Homes)")
plt.legend(loc='best')
plt.show()
#================Semis Regression================#
y_int, slope = linearRegression(Montreal_Semis, len(Montreal_Semis))

plt.plot(years, (y_int + (years-2006)*slope), 'r--')
y_int, slope = linearRegression(Toronto_Semis, len(Toronto_Semis))

plt.plot(years, (y_int + (years-2006)*slope), 'b--')
y_int, slope = linearRegression(Ottawa_Semis, len(Ottawa_Semis))

plt.plot(years, (y_int + (years-2006)*slope), 'g--')
#================Semis Data================#
plt.plot(years, Montreal_Semis, 'r-', label='Montreal')
plt.plot(years, Toronto_Semis, 'b-', label='Toronto')
plt.plot(years, Ottawa_Semis, 'g-', label='Ottawa')
plt.ylabel("Number of Dwellings")
plt.xlabel("Year")
plt.title("Number of Dwellings(Semi Detatched Homes)")
plt.legend(loc='best')
plt.show()
#================Rows Regression================#
y_int, slope = linearRegression(Montreal_Rows, len(Montreal_Rows))

plt.plot(years, (y_int + (years-2006)*slope), 'r--')
y_int, slope = linearRegression(Toronto_Rows, len(Toronto_Rows))

plt.plot(years, (y_int + (years-2006)*slope), 'b--')
y_int, slope = linearRegression(Ottawa_Rows, len(Ottawa_Rows))

plt.plot(years, (y_int + (years-2006)*slope), 'g--')
#================Rows Data================#
plt.plot(years, Montreal_Rows, 'r-', label='Montreal')
plt.plot(years, Toronto_Rows, 'b-', label='Toronto')
plt.plot(years, Ottawa_Rows, 'g-', label='Ottawa')
plt.ylabel("Number of Dwellings")
plt.xlabel("Year")
plt.title("Number of Dwellings(Row Houses)")
plt.legend(loc='best')
plt.show()
#================Apts Regression================#
y_int, slope = linearRegression(Montreal_Apts, len(Montreal_Apts))

plt.plot(years, (y_int + (years-2006)*slope), 'r--')
y_int, slope = linearRegression(Toronto_Apts, len(Toronto_Apts))

plt.plot(years, (y_int + (years-2006)*slope), 'b--')
y_int, slope = linearRegression(Ottawa_Apts, len(Ottawa_Apts))

plt.plot(years, (y_int + (years-2006)*slope), 'g--')
#================Apts Data================#
plt.plot(years, Montreal_Apts, 'r-', label='Montreal')
plt.plot(years, Toronto_Apts, 'b-', label='Toronto')
plt.plot(years, Ottawa_Apts, 'g-', label='Ottawa')
plt.ylabel("Number of Dwellings")
plt.xlabel("Year")
plt.title("Number of Dwellings(Apartments/Other)")
plt.legend(loc='best')
plt.show()


for i in range(0, len(Montreal_Singles)):
    MontrealAVG = Montreal_Singles[i] + Montreal_Semis[i] + Montreal_Rows[i] + Montreal_Apts[i]
    OttawaAVG = Ottawa_Singles[i] + Ottawa_Semis[i] + Ottawa_Rows[i] + Ottawa_Apts[i] 
    TorontoAVG = Toronto_Singles[i] + Toronto_Semis[i] + Toronto_Rows[i] + Toronto_Apts[i]
    
    Montreal_Singles[i] = Montreal_Singles[i]/MontrealAVG
    Montreal_Semis[i] = Montreal_Semis[i]/MontrealAVG
    Montreal_Rows[i] = Montreal_Rows[i]/MontrealAVG
    Montreal_Apts[i] = Montreal_Apts[i]/MontrealAVG
    
    Ottawa_Singles[i] = Ottawa_Singles[i]/OttawaAVG
    Ottawa_Semis[i] = Ottawa_Semis[i]/OttawaAVG
    Ottawa_Rows[i] = Ottawa_Rows[i]/OttawaAVG
    Ottawa_Apts[i] = Ottawa_Apts[i]/OttawaAVG

    Toronto_Singles[i] = Toronto_Singles[i]/TorontoAVG
    Toronto_Semis[i] = Toronto_Semis[i]/TorontoAVG
    Toronto_Rows[i] = Toronto_Rows[i]/TorontoAVG
    Toronto_Apts[i] = Toronto_Apts[i]/TorontoAVG


#================Singles Regression================#    
y_int, slope = linearRegression(Montreal_Singles, len(Montreal_Singles))
mSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'r--', label='Montreal ' + str(int(mSlope*10000)/100) + '% Average change per year')
y_int, slope = linearRegression(Toronto_Singles, len(Toronto_Singles))
tSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'b--', label='Toronto ' + str(int(tSlope*10000)/100) + '% Average change per year')
y_int, slope = linearRegression(Ottawa_Singles, len(Ottawa_Singles))
oSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'g--', label='Ottawa ' + str(int(oSlope*10000)/100) + '% Average change per year')
#================Singles Regression================#
plt.plot(years, Montreal_Singles, 'r-')
plt.plot(years, Toronto_Singles, 'b-')
plt.plot(years, Ottawa_Singles, 'g-')
plt.ylabel("Number of Dwellings")
plt.xlabel("Year")
plt.title("Number of Dwellings(Single Detatched Homes)")
plt.legend(loc='best')
plt.show()
#================Semis Regression================#
y_int, slope = linearRegression(Montreal_Semis, len(Montreal_Semis))
mSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'r--', label='Montreal ' + str(int(mSlope*10000)/100) + '% Average change per year')
y_int, slope = linearRegression(Toronto_Semis, len(Toronto_Semis))
tSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'b--', label='Toronto ' + str(int(tSlope*10000)/100) + '% Average change per year')
y_int, slope = linearRegression(Ottawa_Semis, len(Ottawa_Semis))
oSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'g--', label='Ottawa ' + str(int(oSlope*10000)/100) + '% Average change per year')
#================Semis Data================#
plt.plot(years, Montreal_Semis, 'r-')
plt.plot(years, Toronto_Semis, 'b-')
plt.plot(years, Ottawa_Semis, 'g-')
plt.ylabel("Number of Dwellings")
plt.xlabel("Year")
plt.title("Number of Dwellings(Semi Detatched Homes)")
plt.legend(loc='best')
plt.show()
#================Rows Regression================#
y_int, slope = linearRegression(Montreal_Rows, len(Montreal_Rows))
mSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'r--', label='Montreal ' + str(int(mSlope*10000)/100) + '% Average change per year')
y_int, slope = linearRegression(Toronto_Rows, len(Toronto_Rows))
tSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'b--', label='Toronto ' + str(int(tSlope*10000)/100) + '% Average change per year')
y_int, slope = linearRegression(Ottawa_Rows, len(Ottawa_Rows))
oSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'g--', label='Ottawa ' + str(int(oSlope*10000)/100) + '% Average change per year')
#================Rows Data================#
plt.plot(years, Montreal_Rows, 'r-')
plt.plot(years, Toronto_Rows, 'b-')
plt.plot(years, Ottawa_Rows, 'g-')
plt.ylabel("Number of Dwellings")
plt.xlabel("Year")
plt.title("Number of Dwellings(Row Houses)")
plt.legend(loc='best')
plt.show()
#================Apts Regression================#
y_int, slope = linearRegression(Montreal_Apts, len(Montreal_Apts))
mSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'r--', label='Montreal ' + str(int(mSlope*10000)/100) + '% Average change per year')
y_int, slope = linearRegression(Toronto_Apts, len(Toronto_Apts))
tSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'b--', label='Toronto ' + str(int(tSlope*10000)/100) + '% Average change per year')
y_int, slope = linearRegression(Ottawa_Apts, len(Ottawa_Apts))
oSlope = slope
plt.plot(years, (y_int + (years-2006)*slope), 'g--', label='Ottawa ' + str(int(oSlope*10000)/100) + '% Average change per year')
#================Apts Data================#
plt.plot(years, Montreal_Apts, 'r-')
plt.plot(years, Toronto_Apts, 'b-')
plt.plot(years, Ottawa_Apts, 'g-')
print('%', mSlope, '%', tSlope, '%', oSlope)
plt.ylabel("Number of Dwellings")
plt.xlabel("Year")
plt.title("Number of Dwellings(Apartments/Other)")
plt.legend(loc='best')
plt.show()    







    
