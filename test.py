import requests
import json
import csv
import os

testbool = os.path.isfile('movies.csv')
if not os.path.isfile('movies.csv'):
    with open('movies.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Year', 'Director', 'Writer', 'Actors', 'Genre', 'Runtime', 'Imdb Rating', 'My Rating'])

# Prompt the user for the movie title and rating
title = input('Enter the movie title: ')
rating = int(input('Enter your rating (1-100): '))

# Check if the movie is already in the CSV file
movie_exists = False
with open('movies.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
    for row in rows:
        if row[0] == title:
            movie_exists = True
            update_rating = input('Movie already exists. Do you want to update your rating? (y/n) ')
            if update_rating == 'y':
                row[7] = rating
                with open('movies.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rows)
                break

# # If the movie is not in the CSV file, add it
# if not movie_exists and omdb_data:
#     with open('movies.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([title, director, genre, rating])



# Query the IMDb API for the movie details
response = requests.get(f'http://www.omdbapi.com/?t={title}&apikey=47830a54')
data = json.loads(response.text)

# Check if the movie was found on IMDb
if data['Response'] == 'False':
    print('Movie not found on IMDb.')

if not movie_exists:
    # Extract the director and genre from the API response
    year = data["Year"]
    director = data['Director']
    author = data["Writer"]
    actors = data["Actors"]
    genre = data['Genre']
    runtime = data["Runtime"]
    imdbRating = data["imdbRating"]
    #rating

    # Add the movie to the CSV file
    with open('movies.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title, year, director, author, actors, genre, runtime, imdbRating, rating])
