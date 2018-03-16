#!/usr/bin/env python3
import psycopg2 as psycopg2
import sys


def connect():
    # Connecting to the database.
    try:
        db = psycopg2.connect(
            dbname="news",
            host='localhost',
            user="postgres",
            password="newPassword"
        )
        return db
    except psycopg2.Error as e:
        # If connection failed, close program.
        print("Unable to connect to database")
        sys.exit(1)


def run_query(query):
    # Connect to database
    db = connect()

    # Open a cursor to perform database operations
    cur = db.cursor()

    # Run query
    cur.execute(query)
    return cur


def print_top_articles():
    # Fetch the 3 most popular articles.
    result = run_query("SELECT * FROM articles_popularity LIMIT 3")

    # Loop over the data form the query and print it out.
    print("Top 3 articles. \n")
    for article in result:
        print('"{}" - {} views'.format(article[0], article[1]))
    print("\n")


def print_top_authors():
    # Fetch the authors and how many views they have.
    result = run_query("SELECT * FROM author_popularity")

    # Loop over the data form the query and print it out.
    print("Author popularity. \n")
    for author in result:
        print('{} - {} views'.format(author[0], author[1]))
    print("\n")


def print_errors_over_one():
    # Fetch the days where more than 1 percentage of request errors happened
    result = run_query("SELECT * FROM errors_by_day WHERE error_percentage > 1;")

    # Loop over the data form the query and print it out.
    print("Days with more than 1% of errors. \n")
    for day in result:
        print('{} - {}% errors'.format(day[0], day[1]))
    print("\n")


if __name__ == '__main__':
    # Fetch and print all the statistics
    print_top_articles()
    print_top_authors()
    print_errors_over_one()