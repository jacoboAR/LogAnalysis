#! /usr/bin/env python

import psycopg2


def connect():
    """Connect to the database."""
    return psycopg2.connect("dbname=news")


def get_three_articles():
    """Get the most popular three articles in the database"""
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM articles_views LIMIT 3")
    articles = c.fetchall()
    db.close()
    print "\nWhat are the most popular three articles of all time?\n"
    for i in articles:
        print("\"{0}\" - {1} views".format(i[0], i[1]))


def most_popular_author():
    """Get the most popular article authors"""
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM most_pop_author LIMIT 3")
    authors = c.fetchall()
    db.close()
    print "\nWho are the most popular article authors of all time?\n"
    for i in authors:
        print("{0} - {1} views".format(i[0], i[1]))


def bad_request():
    """Get the days where error requests is more than 1%"""
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM log_status WHERE error_rate > 1.00")
    error_requests = c.fetchall()
    db.close()
    print "\nOn which days did more than 1% of requests lead to errors?\n"
    for i in error_requests:
        print("{0} - {1}%".format(i[0], i[1]))


get_three_articles()
most_popular_author()
bad_request()
