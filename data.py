import pandas as pd
# "bookId","title","series","author","rating","description","language","isbn","genres","characters",
# "bookFormat","edition","pages","publisher","publishDate","firstPublishDate",
# "awards","numRatings","ratingsByStars","likedPercent","setting","coverImg","bbeScore","bbeVotes","price"

df = pd.read_csv("books_data.csv", usecols = ['title','series', 'author', 'rating', 'language', 
                                              'genres', 'characters','publisher', 'pages', 'likedPercent','price'])
print(df)