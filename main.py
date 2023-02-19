import os
from linkedlist import LinkedList
from messages import Messages
from data import get_data

def get_data_lists(data_file):
    books_data, all_genres = get_data(data_file)
    return all_genres, books_data

def create_genres_ll(genres):
    genres_ll = LinkedList()
    for genre in genres:
        genres_ll.insert_beginning(genre)
    return genres_ll

def create_books_ll(books):
    books_ll = LinkedList()
    for book in books:
        books_ll.insert_beginning(book)
    return books_ll


def main():
    # setting initial variables and linked lists
    data_filename = 'books_data.csv'
    messages = Messages()
    genres, books = get_data_lists(data_filename)
    genres_ll = create_genres_ll(genres)
    books_ll = create_books_ll(books)

    selected_genre = ""
    messages.print_book()
    messages.print_hello()
    print('\n')

    while len(selected_genre) == 0:
        usr_input = str(input(
            "\nWhat book genre would you like to read today? \nType the beggining of that genre and press enter to see if it's here!\n")).lower()
        matching_genres = []
        current_genre = genres_ll.get_head_node()
        while current_genre is not None:
            if str(current_genre.value).lower().startswith(usr_input):
                matching_genres.append(current_genre.value)
            current_genre = current_genre.get_next_node()

        if len(matching_genres) > 1:
            print('\nWith those beggining letters, the matching genres are: \n')
            for genre in matching_genres:
                print('* ' + str(genre) + '\n')
        elif len(matching_genres) == 0:
            print("\nWe are sorry, we have not found any genre in our database that would match this input!")
        else:
            print(f'\nThe only matching genre is {matching_genres[0]}.')
            get_books = str(input((f"\nWould you like to get a list of books in the {selected_genre} genre? Type 'y' for yes or 'n' to start searching again.\n")))[0].lower()
            if get_books == 'y':
                selected_genre = matching_genres[0]
                print(f"\nSelected genre: {selected_genre}")
                current_book = books_ll.get_head_node()
                # starting counter to stop printing when it exceeds 10
                counter = 0
                # check if txt file exists, then ask if the user wants to overwrite it
                if os.path.exists(str(selected_genre)+'.txt'):
                    overwrite = str(input('\nYou already have a file with this genre, would you like to overwrite? [y/n]\n'))[0].lower()
                    if overwrite == 'y':
                        with open(str(selected_genre)+'.txt', 'w') as file:
                            print('\nOverwriting!')
                    else:
                        print('\nSkipping...')
                        repeat_search = str(input(("\nWould you like to search for other genres? Type 'y' for yes or 'n' to start searching again.\n")))[0].lower()
                        if repeat_search == 'y':
                            selected_genre = ""
                        continue
                else:
                    with open(str(selected_genre)+'.txt', 'w') as file:
                        print('\nCreating file!')

                with open(str(selected_genre)+'.txt', 'w', encoding="utf-8") as file:
                    print('\nSearching!')
                    while current_book.get_next_node() is not None:
                        current_book_data = current_book.get_value()
                        if selected_genre in current_book_data[5]:
                            # skipping missing data
                            if None not in current_book_data:
                                if counter < 10:
                                    print('\n======================================')
                                    print(f'Title: {current_book_data[0]}')
                                    print(f'Series: {current_book_data[1]}')
                                    print(f'Authors: {current_book_data[2]}')
                                    print(f'Rating: {current_book_data[3]}')
                                    print(f'Language: {current_book_data[4]}')
                                    print(f'All genres: {", ".join(current_book_data[5])}')
                                    print(f'Total pages: {current_book_data[6]}')
                                    print(f'Liked percentage: {current_book_data[7]}%')

                                file.write('======================================\n')
                                file.write(f'Title: {current_book_data[0]}\n')
                                file.write(f'Series: {current_book_data[1]}\n')
                                file.write(f'Authors: {current_book_data[2]}\n')
                                file.write(f'Rating: {current_book_data[3]}\n')
                                file.write(f'Language: {current_book_data[4]}\n')
                                file.write(f'All genres: {", ".join(current_book_data[5])}\n')
                                file.write(f'Total pages: {current_book_data[6]}\n')
                                file.write(f'Liked percentage: {current_book_data[7]}%\n')
                                file.write('\n')
                                counter += 1
                                if counter == 10:
                                    print('\nThe number of found books exceeded 10! No more entries will be printed.')
                                    print(f'Instead, all entries can be found in the {selected_genre}.txt file!')
                        current_book = current_book.get_next_node()
                if counter == 0:
                    print(f'\nSorry! It appears our database has no complete data for any books in the {selected_genre} genre')
                    print(f'Pleae, create a GitHub issue or send an email directly to: radoslawizak@gmail.com!')
                    # deleting empty file
                    os.remove(str(selected_genre)+'.txt')

            # asking if the user wants to repeat search
            repeat_search = str(input(("\nWould you like to search for other genres? Type 'y' for yes or 'n' to start searching again.\n")))[0].lower()
            if repeat_search == 'y':
                selected_genre = ""
            else:
                print('\nThank you for using BestBooks!\n')
                messages.print_goodbye()

if __name__ == "__main__":
    main()
