import csv
import matplotlib.pyplot as plt

with open('Gapminder.csv', 'r') as myFile:            #For reading CSV file
    data = list(csv.reader(myFile, delimiter=','))

def dataTypeConversion(rawList, dataType):            #Conversion of Datatypes
    convertedList = []
    previousValue = 0
    for item in rawList:
        if item != '':
            convertedList.append(dataType(item))
            previousValue = dataType(item)
        else:
            convertedList.append(previousValue) # replacing missing value with previous value
    return convertedList

def fetchIndices(data, columnIndex, searchItem):      
    listRowIndices = []

    for i in range(len(data)):
        if data[i][columnIndex] == searchItem:
            listRowIndices.append(i)
    
    return listRowIndices

def fetchColumnData1(columnIndex, hasHeader, year):      #fetching column data
    listData = []

    for i in range(len(data)):
        if data[i][4]== year:
            listData.append(data[i][columnIndex])
    if hasHeader:
        return listData[0:]
    else:
        return listData

def fetchData(data, columnIndex, listRowIndices):
    listDataValues = []

    for i in range(len(listRowIndices)):
        listDataValues.append(data[listRowIndices[i]][columnIndex])
    return listDataValues

def fetchPak_data(columnIndex, hasHeader, year):       #fetching Pak data from columns
    list1=[]

    for i in range(len(data)):
        if data[i][0]== 'Pakistan' and data[i][4]==year:
            if data[i][columnIndex] == '':
                return [-1]
            else:
                list1.append(data[i][columnIndex])
                return list1

def attributes(attr,value):                         #attributes differentiation on positive and negative basis
    if attr=='AgriculturalLand':
        return 1
    elif attr=='BodyMassIndex_M':
        if value<18.5 or value>24.9:
            return 0
        else:
            return 1
    elif attr=='BodyMassIndex_F':
        if value<18.5 or value>24.9:
            return 0
        else:
            return 1
    elif attr=='Cellphones':
        return 1
    elif attr=='DemocracyScore':
        return 2
    elif attr=='Exports':
        return 1
    elif attr=='Femalesaged25to54labourforceparticipationrate':
        return 1
    elif attr=='Forestarea':
        return 1
    elif attr=='GDPpercapita':
        return 1
    elif attr=='Governmenthealthspendingperpersontotal':
        return 1
    elif attr=='Hightotechnologyexports':
        return 1
    elif attr=='Hourlycompensation':
        return 2
    elif attr=='IncomePerPerson':
        return 1
    elif attr=='Incomeshareofpoorest10pct':
        return 2
    elif attr=='Incomeshareofrichest10pct':
        return 2
    elif attr=='Internetusers':
        return 1
    elif attr=='LifeExpectancy':
        return 1
    elif attr=='Literacyrateadulttotal':
        return 1
    elif attr=='Literacyrateyouthtotal':
        return 1
    elif attr=='MedicalDoctors':
        return 1
    elif attr=='Ratioofgirlstoboysinprimaryandsecondaryeducation':
        return 2
    elif attr=='Renewablewater':
        return 1
    elif attr=='Residentialelectricityuseperperson':
        return 2
    elif attr=='TotalGDPUS':
        return 1
    elif attr=='TotalhealthspendingperpersonUS':
        return 2
    elif attr=='Tradebalance':
        return 1
    elif attr=='UrbanpopulationTotal':
        return 2
    elif attr=='Urbanpopulationgrowth':
        return 2
    else:
        return 0


#ranking pakistan w.r.t countries on average on the basis of input provided (year)
paksitanIndices = fetchIndices(data,0,'Pakistan')
years = fetchData(data,4,paksitanIndices)
print(years)
year=input("Enter year from list: ")

for i in range(6,50):  
    info = fetchColumnData1(i,True,year)
    info=dataTypeConversion(info,float)
    pak=fetchPak_data(i,True,year)
    pak=dataTypeConversion(pak,float)
    if pak[0]!=-1.0: 
        pak.append(sum(info)/len(info))
        indicator=data[0][i]     
        # plotting a bar chart 
        plt.figure()
        plt.bar([1,3], pak, tick_label = ['Pakistan','Countries on average'], 
                width = 0.5, color = ['green','red']) 
        plt.plot([0., 4.5], [0,0], "k--")
        
        plt.title(indicator+'   '+'Year:'+year) 


        
#For ranking pakistan w.r.t countries on average (1952-2012)
info_list=[]
pak_list=[]
for y in years:
    pak_val=10
    info_val=10
    for i in range(6,50):
        info = fetchColumnData1(i,True,y)
        info=dataTypeConversion(info,float)
        pak=fetchPak_data(i,True,y)
        pak=dataTypeConversion(pak,float) 
        indicator=data[0][i]  
        if pak[0]!=-1.0:
            info=sum(info)/len(info)
            pak=sum(pak)
            if pak>info:
                attr_val=attributes(indicator,pak)
                if attr_val==1:
                    pak_val+=1
                elif attr_val==0:
                    pak_val-=1
            if pak<info:
                attr_val=attributes(indicator,info)
                if attr_val==1:
                    info_val+=1
                elif attr_val==0:
                    info_val-=1
    info_list.append(info_val)
    pak_list.append(pak_val)
years = dataTypeConversion(fetchData(data,4,paksitanIndices),int)
plt.figure()
plt.plot(years,pak_list,'green',label="Pakistan")
plt.plot(years,info_list,'red',label="Countries on Average")
plt.title('Pakistan status (1952-2012)')
plt.legend(loc="best")
plt.show()




