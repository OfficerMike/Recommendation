import requests
import json
import csv

# Prompt the user for the movie title and rating
title = input('Enter the movie title: ')
rating = int(input('Enter your rating (1-10): '))

# Query the IMDb API for the movie details
response = requests.get(f'http://www.omdbapi.com/?t={title}&apikey=47830a54')
data = json.loads(response.text)

# Extract the director and genre from the API response
director = data['Director']
genre = data['Genre']

# Add the movie to the CSV file
with open('movies.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([title, director, genre, rating])
