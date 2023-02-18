import pandas as pd
import re
"""
All possible dictionary entries are:

bookId, title, series, author, rating, description, language, isbn, genres, characters, 
bookFormat, edition, pages, publisher, publishDate, firstPublishDate, 
awards, numRatings, ratingsByStars, likedPercent, setting, coverImg, bbeScore, bbeVotes, price
"""

"""
All currently used entries are:

title, series,  author,  rating,  language,  
genres,  pages,  likedPercent
"""

def get_data(data_file):
    df = pd.read_csv(data_file, usecols = ['title','series', 'author', 'rating', 'language', 
                            'genres', 'pages', 'likedPercent'])
    df_lst = df.loc[:, :].values.tolist()
    genres_set = set()
    # fixing genres to a list of strings instead of concurrent string
    i = 0
    for row in df_lst:
        genres = re.sub("[']","",row[5][1:-1]).split(', ')
        df_lst[i][5] = genres
        i += 1
        for genre in genres:
            genres_set.add(genre)

    return df_lst, genres_set

