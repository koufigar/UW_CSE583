import pandas as pd
data = pd.read_csv('bicycle_data.csv')
data.info() #it looks like the date is a character string (str) and the other three columns are floating point number (float64). It seems like the last three columns could be integers since they are pathway count fields and we can only have whole number of counts! but i dont think we gain a lot by converting the floats to integers! I think what we definitely need to change is the date dtype, which is listed as str! 
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y %I:%M:%S %p') #to convert the format (I looked this one up in Claude!)
data.columns = ['Date & Time','Total','West','East'] # renaming the columns cause why not!
data['Total (again for hw)'] = data['West'] + data['East']
data['Hour'] = data['Date & Time'].dt.hour
data_2016 = data[data['Year']== 2016]
data_2016.isnull().sum() #it looks like one 