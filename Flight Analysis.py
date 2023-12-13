#!/usr/bin/env python
# coding: utf-8

# # project number 2.1

# ## data analysis with pandas

# ###### Flight Analysis - Bureau of Transportation

# ###### Name: Daniel Rodan 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ###### Ex 1

# In[2]:


airlines = pd.read_csv(r"C:\python files\airelines.csv")
airports = pd.read_csv(r"C:\python files\airports.csv")
flights = pd.read_csv(r"C:\python files\flights.csv")


# In[3]:


airlines.head(3)


# In[4]:


airports.head(3)


# In[5]:


flights.head(3)


# ###### Ex 2

# In[6]:


# 2.1

len(airlines)


# In[7]:


# 2.2

df = airports.groupby('state')
df['airport'].count().to_frame().sort_values('airport', ascending = False).head(1).rename(columns = {'airport':'total_airports'})


# In[8]:


# 2.3
my_df = df['airport'].count().to_frame().sort_values('airport', ascending = False).rename(columns = {'airport':'total_airports'})

x_axix = my_df.index
y_axix = my_df['total_airports']

plt.figure(figsize = (20,6))
plt.xticks(rotation = 90)

plt.bar(x_axix, y_axix, color = 'darkred', width = 0.65, edgecolor ='black')

plt.grid(b = True, color ='darkred', 
        linestyle ='-.', linewidth = 0.4, 
        alpha = 0.5) 

plt.xlabel('<---State Name--->', fontweight = 'bold', color = 'darkred')
plt.ylabel('<---Airports--->', fontweight = 'bold', color = 'darkred')
plt.title('Airports by State', loc = 'left', fontweight = 'bold', color = 'darkred')

plt.show()


# ###### Ex 3

# In[9]:


# 3.1

df = flights.groupby('cancel_reason')
df['cancelled'].count().to_frame().sort_values('cancelled', ascending = False).rename(columns = {'cancelled':'num_of_cancellations'}).head(1)


# In[10]:


# 3.2
v_df = flights.groupby('cancel_reason')['cancelled'].count().to_frame().sort_values('cancelled', ascending=False).rename(columns = {'cancelled': 'total_cancellations'})

x_axis = v_df.index
y_axis = v_df['total_cancellations']

plt.bar(x_axis, y_axis, color = 'darkred', width = 0.5, edgecolor ='black')

plt.grid(b = True, color ='darkred', 
        linestyle ='-.', linewidth = 0.4, 
        alpha = 0.5) 

plt.xlabel('Cancellation Reason', fontweight = 'bold', color = 'darkred')
plt.ylabel('Number of Cancellations', fontweight = 'bold', color = 'darkred')
plt.title('Flight Cancellations', loc = 'left', fontweight = 'bold', color = 'darkred')

plt.show()


# ###### Ex 5

# In[11]:


# 5.1

flights.groupby('airline')['flight_id'].count().to_frame().rename(columns = {'flight_id':'number_of_flights'})


# In[12]:


# 5.2

data = flights.groupby('airline')['flight_id'].count().to_frame().rename(columns = {'flight_id':'number_of_flights'})

x_axix = data.index
y_axix = data['number_of_flights']

plt.figure(figsize = (10,3))
plt.xticks(rotation = 0)
plt.yticks(rotation = 0)

plt.bar(x_axix,y_axix, color = 'darkred', width = 0.5, edgecolor ='black')

plt.grid(b = True, color ='darkred', 
        linestyle ='-.', linewidth = 0.4, 
        alpha = 0.5) 

plt.xlabel('<---Airline Type--->', fontweight = 'bold', color = 'darkred')
plt.ylabel('<---Total Flights--->', fontweight = 'bold', color = 'darkred')
plt.title('Flights by Airlines', loc= 'left', fontweight = 'bold', color = 'darkred')

plt.show()


# ###### Ex 6

# In[13]:


# 6.1 

s1 = flights.merge(airlines, how="inner", left_on="airline", right_on="iata_code").rename(columns={"airline_y":"airline_name"})

s1.groupby("airline_name")["delay_in_minutes"].sum().to_frame().sort_values('delay_in_minutes', ascending=False).head(1)


# In[14]:


# 6.2

s1 = flights.merge(airlines, how="inner", left_on="airline", right_on="iata_code").rename(columns={"airline_y":"airline_name"})

data = s1.groupby("airline_name")["delay_in_minutes"].sum().to_frame().sort_values('delay_in_minutes', ascending=False)
# Figure Size 
fig, ax = plt.subplots(figsize =(16, 9)) 
  
# Horizontal Bar Plot 
ax.barh(data.index, data['delay_in_minutes'], color = 'darkred') 
  
# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='darkred', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 
  
# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+0.2, i.get_y()+0.5,  
             str(round((i.get_width()), 2)), 
             fontsize = 10, fontweight ='bold', 
             color ='black') 
  
# Add Plot Titles
ax.set_xlabel('<--- Total Delays (in minutes) --->', color = 'darkred',fontweight = 'bold')
ax.set_ylabel('<--- Airline --->', color = 'darkred',fontweight = 'bold')
ax.set_title('Delayes by Airlines', loc = 'left', color = 'darkred',fontweight = 'bold') 

  
# Add Text watermark 
fig.text(0.9, 0.15, 'a', fontsize = 12, 
         color ='grey', ha ='right', va ='bottom', 
         alpha = 0.7) 
  
# Show Plot 
plt.show()


# ###### Ex 7

# In[15]:


# 7.1 
s1 = flights.merge(airlines, how="inner", left_on="airline", right_on="iata_code").rename(columns={"airline_y":"airline_name"})

x = s1['origin_airport'] == 'LAX'
y = s1['destination_airport'] == 'SFO'

s1[x & y].groupby("airline_name")["delay_in_minutes"].sum().to_frame().sort_values('delay_in_minutes', ascending=True).head(1)


# In[16]:


# 7.2 

s1 = flights.merge(airlines, how="inner", left_on="airline", right_on="iata_code").rename(columns={"airline_y":"airline_name"})

x = s1['origin_airport'] == 'LAX'
y = s1['destination_airport'] == 'SFO'

data = s1[x & y].groupby("airline_name")["delay_in_minutes"].sum().to_frame().sort_values('delay_in_minutes', ascending=True)
x_axix = data.index
y_axix = data['delay_in_minutes']

plt.figure(figsize = (10,5))
plt.xticks(rotation = 0)
plt.yticks(rotation = 0)

plt.bar(x_axix,y_axix, color = 'darkred', width = 0.5, edgecolor ='black')

plt.grid(b = True, color ='darkred', 
        linestyle ='-.', linewidth = 0.4, 
        alpha = 0.5) 

plt.xlabel('<--- Airline --->', color = 'darkred', fontweight= 'bold')
plt.ylabel('<--- Total Delays --->', color = 'darkred', fontweight= 'bold')
plt.title('Delays by Airlines', loc = 'left', color = 'darkred', fontweight= 'bold')

plt.show()


# ###### Ex 8

# In[17]:


x = flights['cancelled'] == 1
len(flights[x]) / len(flights) * 100


# ###### Ex 9

# In[18]:


# 9.1
s1 = flights.merge(airlines, 
                   how = 'inner',
                   left_on = 'airline',
                   right_on = 'iata_code')\
.rename(columns = {'airline_y':'airline_name'})

total_flights = s1.groupby('airline_name')

total_cancellations = total_flights[['flight_id','cancel_reason']].count().rename(columns = {'flight_id': 'num_of_flights','cancel_reason': 'cancellations'})

total_cancellations['ratio'] = total_cancellations['cancellations'] / total_cancellations['num_of_flights'] * 100

total_cancellations.sort_values('ratio', ascending = False).head(1)


# In[19]:


s1 = flights.merge(airlines, 
                   how = 'inner',
                   left_on = 'airline',
                   right_on = 'iata_code')\
.rename(columns = {'airline_y':'airline_name'})

total_flights = s1.groupby('airline_name')

total_cancellations = total_flights[['flight_id','cancel_reason']].count().rename(columns = {'flight_id': 'num_of_flights','cancel_reason': 'cancellations'})

total_cancellations['ratio'] = total_cancellations['cancellations'] / total_cancellations['num_of_flights'] * 100

data = total_cancellations
x_axis = data.index
y_axis = data['ratio']

plt.figure(figsize = (13,5))

plt.bar(x_axis, y_axis, color = 'darkred', width = 0.5, edgecolor ='black')

plt.grid(b = True, color ='darkred', 
        linestyle ='-.', linewidth = 0.4, 
        alpha = 0.5) 

plt.xticks(rotation = 90)

plt.xlabel('<--- Airline --->', color = 'darkred', fontweight= 'bold')
plt.ylabel('<--- Rates --->', color = 'darkred', fontweight= 'bold')
plt.title('Cancellation Rate', loc = 'left', color = 'darkred', fontweight= 'bold')
plt.show()


# ###### Ex 10

# In[20]:


# 10.1 
s1 = flights.merge(airports, 
                   how = 'inner',
                   left_on = 'origin_airport',
                   right_on = 'iata_code')

mask = s1['cancel_reason'] == 'Security'

s1[mask].groupby('airport')['flight_id'].count().to_frame().rename(columns = {'flight_id':'cancelled_flights'}).sort_values('cancelled_flights', ascending = False).head(1)


# In[21]:


#  10.2 
s1 = flights.merge(airports, 
                   how = 'inner',
                   left_on = 'origin_airport',
                   right_on = 'iata_code')

mask = s1['cancel_reason'] == 'Security'

can_issues = s1[mask].groupby('airport')['flight_id'].count().to_frame().rename(columns = {'flight_id':'cancelled_flights'}).sort_values('cancelled_flights', ascending = False).head(10)

x_axis = can_issues.index
y_axis = can_issues['cancelled_flights']

plt.figure(figsize = (13,5))

plt.bar(x_axis, y_axis, color = 'darkred', width = 0.5, edgecolor ='black')

plt.grid(b = True, color ='darkred', 
        linestyle ='-.', linewidth = 0.4, 
        alpha = 0.5) 

plt.xticks(rotation = 90)

plt.xlabel('<--- Airport --->', color = 'darkred', fontweight= 'bold')
plt.ylabel('<--- Number of Cancellations --->', color = 'darkred', fontweight= 'bold')
plt.title('Top 10 Security Cancellations', loc = 'left', color = 'darkred', fontweight= 'bold')
plt.show()


# ###### Ex 11

# In[26]:


# 11.1
flights['flight_date'] = pd.to_datetime(flights['flight_date'])
flights['flight_month'] = flights['flight_date'].dt.month

flights.groupby('flight_month')['flight_id'].count().to_frame().rename(columns = {'flight_id':'number_of_flights'})


# In[27]:


# 11.2
flights['flight_date'] = pd.to_datetime(flights['flight_date'])
flights['flight_month'] = flights['flight_date'].dt.month

df = flights.groupby('flight_month')['flight_id'].count().to_frame().rename(columns = {'flight_id':'number_of_flights'})

x_axis = df.index
y_axis = df['number_of_flights']

plt.figure(figsize = (13,5))

plt.bar(x_axis, y_axis, color = 'darkred', width = 0.5, edgecolor ='black')

plt.grid(b = True, color ='darkred', 
        linestyle ='-.', linewidth = 0.4, 
        alpha = 0.5) 

plt.xlabel('<--- Month --->', color = 'darkred', fontweight= 'bold')
plt.ylabel('<--- Flights Number --->', color = 'darkred', fontweight= 'bold')
plt.title('Flights number per month', loc = 'left', color = 'darkred', fontweight= 'bold')
plt.show()


# ###### Ex 12

# In[25]:


s1 = flights.merge(airlines, 
                   how = 'inner',
                   left_on = 'airline',
                   right_on = 'iata_code')

s2 = s1.merge(airports, 
              how = 'inner',
              left_on = 'origin_airport',
              right_on = 'iata_code')

s3 = s2.merge(airports,
              how = 'inner',
              left_on = 'destination_airport',
              right_on = 'iata_code')

m1 = s3['airline_y'] == 'American Airlines Inc.'
m2 = s3['airport_x'] == 'Los Angeles International Airport'
m3 = s3['airport_y'] == 'Miami International Airport'

s3[m1 & m2 & m3][['airport_x', 'airport_y']]

len(s3)


# In[ ]:




