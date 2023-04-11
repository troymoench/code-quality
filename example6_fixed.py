# example 6: security
import os

print(1 + 2)

user_id = 12345
query = "SELECT * FROM users where user_id = %s"
# pass query and user_id to db driver (eg psycopg2) separately

password = os.getenv("MY_SECRET_PASSWORD")
