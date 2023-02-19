import os
import time
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
            get_books = str(input((f"\nWould you like to get a list of books in the {matching_genres[0]} genre? [y/n]\n")))[0].lower()
            if get_books == 'y':
                selected_genre = matching_genres[0]
                print(f"\nSelected genre: {selected_genre}")
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
                        repeat_search = str(input(("\nWould you like to search for other genres? [y/n]\n")))[0].lower()
                        if repeat_search == 'y':
                            selected_genre = ""
                            continue
                        else:
                            messages.print_goodbye()
                            break


                else:
                    with open(str(selected_genre)+'.txt', 'w') as file:
                        print('\nCreating file!')
                # checking for pages-range
                set_pages = str(input('\nWould you like to set min-max pages filter? If no, all books will be listed. [y/n]\n'))[0].lower()
                set_pages_min = False
                set_pages_max = False
                min_pages = 0
                max_pages = 10**9
                if set_pages == 'y':
                    min_pages = input('\nWhat should the minimum page count? Please, enter an integer.\n')
                    max_pages =  input('\nWhat should the maximum page count? Please, enter an integer.\n')
                    # sleep in case user makes a mistake so the msg is readable
                    sleep_time = 2
                    try:
                        min_pages = int(min_pages)
                        set_pages_min = True
                    except:
                        print(f'\n"{min_pages}" is not an integer! Skipping min page filter!')
                        time.sleep(sleep_time)
                    try:
                        max_pages = int(max_pages)
                        set_pages_max = True
                    except:
                        print(f'\n"{max_pages}" is not an integer! Skipping max page filter!')
                        time.sleep(sleep_time)
                # checking for minimum rating
                set_rating = str(input('\nWould you like to set a min rating filter? If no, all books will be listed. [y/n]\n'))[0].lower()
                min_rating = 0.00
                set_min_rating = False
                if set_rating == 'y':
                    min_rating =  input('\nWhat should the minimum rating be? Please, enter float in range 0.00-5.00.\n')
                    try:
                        min_rating = float(min_rating)
                        set_min_rating = True
                    except:
                        print(f'\n"{min_rating}" is not a float! Skipping min rating filter!')
                        time.sleep(sleep_time)
                # checking for minimum liked percentage
                set_percentage = str(input('\nWould you like to set a min liked by % of readers filter? If no, all books will be listed. [y/n]\n'))[0].lower()
                min_percentage = 0
                set_min_percentage = False
                if set_percentage == 'y':
                    min_percentage =  input('\nWhat should the minimum liked by % be? Please, enter an integer in range 0-100.\n')
                    try:
                        min_percentage = int(min_percentage)
                        set_min_percentage = True
                    except:
                        print(f'\n"{min_percentage}" is not an integer! Skipping min liked by % filter!')
                        time.sleep(sleep_time)

                with open(str(selected_genre)+'.txt', 'w', encoding="utf-8") as file:
                    print('\nSearching!')
                    current_book = books_ll.get_head_node()
                    while current_book.get_next_node() is not None:
                        current_book_data = current_book.get_value()
                        if selected_genre in current_book_data[5]:
                            # skipping missing data
                            if None not in current_book_data:
                                if set_pages_min and int(current_book_data[6]) < min_pages:
                                    current_book = current_book.get_next_node()
                                    continue
                                if set_pages_max and int(current_book_data[6]) > max_pages:
                                    current_book = current_book.get_next_node()
                                    continue
                                if set_min_rating and float(current_book_data[3]) < min_rating:
                                    current_book = current_book.get_next_node()
                                    continue
                                if set_min_percentage and int(current_book_data[7]) < min_percentage:
                                    current_book = current_book.get_next_node()
                                    continue
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
            else:
                continue

            # asking if the user wants to repeat search
            repeat_search = str(input(("\nWould you like to repeat and search for other genres? [y/n]\n")))[0].lower()
            if repeat_search == 'y':
                selected_genre = ""
            else:
                selected_genre = "end"
                messages.print_goodbye()

if __name__ == "__main__":
    main()
