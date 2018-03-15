import psycopg2 as psycopg2

# Connecting to the database.
db = psycopg2.connect(
    dbname="news",
    host='localhost',
    user="postgres",
    password="newPassword"
)

# Open a cursor to perform database operations
cur = db.cursor()

# Fetch the 3 most popular articles.
cur.execute("SELECT * FROM articles_popularity LIMIT 3")

# Loop over the data form the query and print it out.
print("Top 3 articles. \n")
for article in cur:
    print('"{}" - {} views'.format(article[0], article[1]))
print("\n")

# Fetch the authors and how many views they have.
cur.execute("SELECT * FROM author_popularity")

# Loop over the data form the query and print it out.
print("Author popularity. \n")
for author in cur:
    print('{} - {} views'.format(author[0], author[1]))
print("\n")

# Fetch the days where more than 1 percentage of request errors happened
cur.execute("SELECT * FROM errors_by_day WHERE error_percentage > 1;")

# Loop over the data form the query and print it out.
print("Days with more than 1% of errors. \n")
for day in cur:
    print('{} - {}% errors'.format(day[0], day[1]))
print("\n")
