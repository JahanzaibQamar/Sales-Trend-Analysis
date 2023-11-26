#!/usr/bin/env python
# coding: utf-8

# # Sales Analysis

# #### Install and import necessory libraries

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install os')
get_ipython().system('pip install matplotlib')



# In[5]:


import pandas as pd
import os
import matplotlib.pyplot as plt


# #### Importing and Merging all files

# In[11]:


folder_path = r"D:\data analyst Course data\Case study\Sales python project\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data"
all_data = pd.DataFrame()


for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        all_data = pd.concat([all_data, df], ignore_index=True)

print(all_data)

        
        
        


# #### Save the file

# In[12]:


all_data.to_csv("all_data.csv", index=False)


# In[13]:


all_data = pd.read_csv("all_data.csv")
all_data.head()


# #### Clean up the Data

# In[14]:


# when we merge all the files the headers of all the files are also duplicated
temp_df = all_data[all_data['Order ID'].str[0:5] == 'Order']
temp_df.head()


# In[15]:


# We have to drop all the duplicated rows
all_data = all_data[all_data['Order ID'].str[0:5] != 'Order']


# In[16]:


# check for null values
na_df = all_data[all_data.isna().any(axis=1)]
na_df.head()


# In[18]:


# Drop nulls
all_data = all_data.dropna(how='all')


# #### Create new 'month' column

# In[21]:


all_data['Month'] = all_data['Order Date'].str[0:2]
all_data ['Month'] = all_data['Month'].astype('int')
all_data.head()


# #### Make a Sales column

# In[24]:


all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'], errors='coerce')

all_data['Price Each'] = pd.to_numeric(all_data['Price Each'], errors='coerce')
all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
print(all_data.head())


# #### Create a City column

# In[50]:


all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{x.split(', ')[1]}, {x.split(', ')[2].split(' ')[0]}")

all_data.head()


# #### What are the monthly Sales 

# In[27]:


monthly_sales = all_data.groupby('Month').agg({
    'Quantity Ordered': 'sum',
    'Price Each': 'sum',
    'Sales': 'sum'
}).reset_index()
monthly_sales = monthly_sales.sort_values(by='Sales', ascending=False)

print(monthly_sales)


# In[33]:


plt.bar(monthly_sales['Month'], monthly_sales['Sales'])
plt.xticks(monthly_sales['Month'])
plt.xlabel('Months')
plt.ylabel('Total Sales')
plt.show()


# #### December month have most sales and January has the slowest sales recorded

# #### Sales according to cities

# In[52]:


city_sales = all_data.groupby('City').agg({
    'Quantity Ordered': 'sum',
    'Price Each': 'sum',
    'Sales': 'sum'
}).reset_index()
city_sales = city_sales.sort_values(by='Sales', ascending=False)

print(city_sales)


# In[54]:


plt.bar(city_sales['City'], city_sales['Sales'])
plt.xticks(city_sales['City'], rotation= 'vertical', size= 8)
plt.xlabel('Cities Names')
plt.ylabel('Total Sales')
plt.show()


# #### San Francisco, CA has the highest sales recorded and Portland, ME has the least sales record.

# #### What time customers buy the most

# In[59]:


# First we have to convert Order Date column into datetime data type
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'], format='%m/%d/%y %H:%M')


# In[74]:


# Convert 'Order Date' column to datetime type
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

# Extract hour from 'Order Date' and create a new column 'Hour'
all_data['Hour'] = all_data['Order Date'].dt.hour

# Group data by 'Hour' and sum the 'Sales' for each hour
hourly_sales = all_data.groupby('Hour')['Sales'].sum()

# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(hourly_sales.index, hourly_sales.values, marker='o', linestyle='-', color='b')
plt.title('Total Sales Over Time (Hourly)')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(range(24))  

# Show the plot
plt.show()



    


# #### 11 AM to 7 PM is the peak time

# #### What products are most sold?

# In[77]:


product_sales = all_data.groupby('Product')['Quantity Ordered'].sum()


product_sales = product_sales.sort_values(ascending=False)
product_sales.head()


# In[78]:


# Create a bar chart
plt.figure(figsize=(12, 6))


product_sales.plot(kind='bar', color='skyblue')


plt.title('Total Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=90)


plt.show()


# #### AAA Batteries are the most sold product and LG Dryer is the least sold product

# #### Products sold in respect to their prices

# In[86]:


product_data = all_data.groupby('Product').agg({'Quantity Ordered': 'sum', 'Price Each': 'mean'})

product_data = product_data.sort_values(by='Quantity Ordered', ascending=False)

product_data.head(20)



# In[89]:


fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(product_data.index, product_data['Quantity Ordered'], color='skyblue', label='Quantity Sold')
ax1.set_xlabel('Product')
ax1.set_ylabel('Quantity Sold', color='skyblue')
ax1.tick_params('y', colors='skyblue')

ax1.set_xticks(range(len(product_data.index)))
ax1.set_xticklabels(product_data.index, rotation=90, ha='center')

ax2 = ax1.twinx()
ax2.plot(product_data.index, product_data['Price Each'], color='orange', label='Price')
ax2.set_ylabel('Price', color='orange')
ax2.tick_params('y', colors='orange')

plt.title('Product Sales and Prices')
fig.tight_layout()
plt.show()


# #### Lowest the price, higher the selling. LG Dryer has a high price and low selling.
