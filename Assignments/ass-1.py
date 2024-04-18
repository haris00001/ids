#haris shoaib ~FA21-BSE-076~ 

#Question 1: Web Scraper for IMDB Top 250 Movies


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = [title.text.strip() for title in soup.select(".titleColumn a")]
years = [int(year.text.strip("()")) for year in soup.select(".titleColumn span")]
durations = [int(duration.text.split()[0]) for duration in soup.select(".titleColumn .runtime")]
ratings = [float(rating.text) for rating in soup.select(".imdbRating strong")]

movies_df = pd.DataFrame({
    "Title": titles,
    "Year": years,
    "Duration (min)": durations,
    "IMDB Rating": ratings
})

print(movies_df.head())  # Print the first few rows of the DataFrame
movies_df.to_csv("imdb_top_250_movies.csv", index=False)



#Question 2: Web Scraper for Mars Planet Profile
import pandas as pd

url = "https://space-facts.com/mars/"
tables = pd.read_html(url)
mars_profile_df = tables[0]
mars_profile_df.columns = ["Description", "Value"]

print(mars_profile_df.head())  # Print the first few rows of the DataFrame
mars_profile_df.to_excel("mars_planet_profile.xlsx", index=False)
