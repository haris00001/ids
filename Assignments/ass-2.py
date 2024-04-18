#haris shoaib ~FA21-BSE-076~ 

#Q1
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have loaded the world population dataset into a DataFrame called 'world_population_df'

# Filter the data for the year 2020
top_10_countries_2020 = world_population_df[world_population_df['Year'] == 2020].nlargest(10, 'Population')

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(top_10_countries_2020['Country'], top_10_countries_2020['Population'], color='skyblue')
plt.xlabel('Population (Billions)')
plt.ylabel('Country')
plt.title('Top 10 Highest Populated Countries in 2020')
plt.gca().invert_yaxis()  # Invert y-axis to display highest population at the top
plt.tight_layout()
plt.show()

#Q2
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have loaded the world population dataset into a DataFrame called 'world_population_df'

# Filter the data for the year 2015
top_10_least_populous_2015 = world_population_df[world_population_df['Year'] == 2015].nsmallest(10, 'Population')

# Calculate population change for the specified countries
countries_of_interest = ['Pakistan', 'India', 'United States', 'United Kingdom']
population_change = world_population_df.pivot_table(index='Country', columns='Year', values='Population')
population_change = population_change.loc[countries_of_interest, [1970, 2010]].diff(axis=1).iloc[:, 1]

# Plotting
plt.figure(figsize=(10, 6))
population_change.plot(kind='bar', color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Country')
plt.ylabel('Population Change (Millions)')
plt.title('Population Change from 1970 to 2010')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Filter the data for Pakistan between 2010 and 2020
pakistan_population_growth = world_population_df[(world_population_df['Country'] == 'Pakistan') &
                                                 (world_population_df['Year'] >= 2010) &
                                                 (world_population_df['Year'] <= 2020)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(pakistan_population_growth['Year'], pakistan_population_growth['Population'], marker='o', color='green')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Pakistan Population Growth (2010-2020)')
plt.grid(True)
plt.tight_layout()
plt.show()

#Q3
import pandas as pd
import seaborn as sns

# Assuming you have loaded the diamonds dataset into a DataFrame called 'diamonds_df'

# Filter the data for diamonds with 'clarify' = 'SI2' and 'color' = 'E'
filtered_diamonds = diamonds_df[(diamonds_df['clarity'] == 'SI2') & (diamonds_df['color'] == 'E')]

# Plotting
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_diamonds, x='carat', y='price', hue='cut', palette='viridis')
plt.xlabel('Carat')
plt.ylabel('Price')
plt.title('Relationship Between Carat and Price of Diamonds (Cut as Colors)')
plt.tight_layout()
plt.show()

#Q4
import folium
from folium.plugins import MarkerCluster

# Assuming you have the nuclear waste dataset loaded into a DataFrame called 'nuclear_waste_df'

# Create a base map centered on the US
nuclear_waste_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Add markers for nuclear waste storage sites
marker_cluster = MarkerCluster().add_to(nuclear_waste_map)
for index, row in nuclear_waste_df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Site Name']).add_to(marker_cluster)

# Save the map as an HTML file
nuclear_waste_map.save("nuclear_waste_storage_sites_map.html")


#Q5
import folium

# Assuming you have the Pakistan heritage sites dataset loaded into a DataFrame called 'heritage_sites_df'

# Create a base map centered on Pakistan
heritage_sites_map = folium.Map(location=[30.3753, 69.3451], zoom_start=6)

# Add markers for heritage sites in Pakistan
for index, row in heritage_sites_df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Site Name']).add_to(heritage_sites_map)

# Save the map as an HTML file
heritage_sites_map.save("pakistan_heritage_sites_map.html")
