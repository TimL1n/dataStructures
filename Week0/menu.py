#! /usr/bin/env python3
import csv
import sys

FILENAME = "movies.csv"


def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        print("Could not find " + FILENAME + " file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()


def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    except Exception as e:
        print(type(e), e)
        exit_program()


def exit_program():
    print("Terminating program.")
    sys.exit()


def display_menu():
    print("The Movie List Program")
    print()
    print("Command Menu")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()


def main():
    display_menu()
    movies = [["Deadpool", 2016],
                  ["Shawshank Redemption", 1994],
                  ["Goodfellas", 1990]]

    def list_movies(movies):
        if len(movies) == 0:
            print("There are no movies in this list.\n")
            return
        else:
            i = 1
            for row in movies:
                print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")")
                i += 1
            print()

    def add(movies):
        name = input("Movie: ")
        while True:
            try:
                year = int(input("Year: "))
                movie = (name, year)
                movies.append(movie)
                print(movie[0] + " was added. \n")
                break
            except ValueError:
                print("invalid entry for year, please try again.")

    def delete(movies):
        while True:
            try:
                number = int(input("Number: "))
                if number < 1 or number > len(movies):
                    print("Invalid movie number \n")
                else:
                    movie = movies.pop(number - 1)
                    print(movie[0] + " was deleted.\n")
                    break
            except ValueError:
                print("Invalid movie number. Please try again.")
                continue

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add(movies)
        elif command.lower() == "del":
            delete(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again. \n")
    print("Bye!")


if __name__ == "__main__":
    main()
