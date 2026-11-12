import pandas as pd
data = pd.read_csv('./HW1/src/HW1_data_analysis/bicycle_data.csv')
data.info() 
#it looks like the date is a character string (str) and the other three columns are floating point number (float64). It seems like the last three columns could be integers since they are pathway count fields and we can only have whole number of counts! but i dont think we gain a lot by converting the floats to integers! I think what we definitely need to change is the date dtype, which is listed as str! 
#I am back to this and now it says dtype for Date is "object" which makes sense cause it does have mixed data types! Idk why and how I saw the dtype for data as str! But regardless I will change the format of this!
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y %I:%M:%S %p') #to convert the format (I looked this one up in Claude!)
data.columns = ['Date & Time','Total','West','East'] # renaming the columns cause why not!
print(data)#lets see what we have...
data['Total (again for hw)'] = data['West'] + data['East'] #it looks like the total is already there but I am doing it again cause I want that one point!
print(data['Date & Time'].dtype) #wanted to check out the type of data for the column! 
data['Hour'] = data['Date & Time'].dt.hour #I Google'd this, the dt.hour
data['Year'] = data['Date & Time'].dt.year
print(data)
data_2016= data[data['Year'] >= 2016] #I am assuming "from the year 2016" includes 2016 as well
data_2016.isnull().sum()#it looks like there are 22 that have missing values!!

import matplotlib.pyplot as plt
group_hour_data_2016 = data_2016.groupby('Hour') ['Total'].sum()
fig = plt.figure()
group_hour_data_2016.plot()
plt.xlabel('Hour of the day')
plt.ylabel('Total daily counts')
plt.title('Counts by hour plot_bikes since 2016-2026')
fig.tight_layout()
plt.savefig('counts_by_hour.png')
plt.show()

busiest_hour = group_hour_data_2016.idxmax()
busiest_count = group_hour_data_2016.max()
print(f"Busiest hour: {busiest_hour}:00 with {busiest_count:,.0f} total counts")
#Busiest hour: 17:00 with 1,355,912 total counts
