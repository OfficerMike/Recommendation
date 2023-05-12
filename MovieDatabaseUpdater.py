import requests
import json
import csv
import os


def Omdb_Request(title):
    # Query the IMDb API for the movie details
    response = requests.get(f'http://www.omdbapi.com/?t={title}&apikey=47830a54')
    data = json.loads(response.text)

    # Check if the movie was found on IMDb
    if data['Response'] == 'False':
        print('Movie not found on IMDb.')
        return

    return data


def create_row(data):
    # Extract the director and genre from the API response
    year = data["Year"]
    director = data['Director']
    author = data["Writer"]
    actors = data["Actors"]
    genre = data['Genre']
    runtime = data["Runtime"]
    imdbRating = data["imdbRating"]
    #rating
    return [title, year, director, author, actors, genre, runtime, imdbRating, rating]

def write_row(data):
# Add the movie to the CSV file
    with open('movies.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

#If new file --> write header
if not os.path.isfile('movies.csv'):
    with open('movies.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Year', 'Director', 'Writer', 'Actors', 'Genre', 'Runtime', 'Imdb Rating', 'My Rating'])

# Prompt the user for the movie title and rating
title = input('Enter the movie title: ')

#Start data request
data = Omdb_Request(title)
if data:
    rating = int(input('Enter your rating (1-100): '))


#def check_csv_for_string(search):
# Check if the movie is already in the CSV file
movie_exists = False
with open('movies.csv', newline = '') as csvfile:
    print("DoubleCheck")
    reader = csv.DictReader(csvfile)
#        reader = csv.reader(csvfile)
    rows = list(reader)
    for row in rows:
        print(row['Title'])
        if row['Title'] == title:
            movie_exists = True
            update_rating = input('Movie already exists. Do you want to update your rating? (y/n) ')
            if update_rating == 'y':
                row['My Rating'] = rating
                with open('movies.csv', 'w', newline='') as csvfile:
                    fieldnames = ['Title', 'Year', 'Director', 'Writer', 'Actors', 'Genre', 'Runtime', 'Imdb Rating', 'My Rating']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                break

#check_csv_for_string(title)



if not movie_exists:
    write_row(create_row(data))