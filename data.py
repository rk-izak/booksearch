import pandas as pd

"""
All possible dictionary entries are:

bookId, title, series, author, rating, description, language, isbn, genres, characters, 
bookFormat, edition, pages, publisher, publishDate, firstPublishDate, 
awards, numRatings, ratingsByStars, likedPercent, setting, coverImg, bbeScore, bbeVotes, price
"""

"""
All currently used entries are:

title, series,  author,  rating,  language,  
genres,  characters, publisher,  pages,  likedPercent, price
"""

def get_data(data_file):
    df = pd.read_csv(data_file, usecols = ['title','series', 'author', 'rating', 'language', 
                            'genres', 'characters','publisher', 'pages', 'likedPercent','price'])
    # print(df[['characters']])
    return df
    

get_data("books_data.csv")