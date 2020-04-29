import bcrypt
import sqlite3

conn = sqlite3.connect('users.db')
print("Opened Database connection")

data = conn.execute("SELECT id, username, password, age FROM EMPLOYEES")

for row in data:
  print("ID = ", row[0] )
  print("USERNAME = ", row[1] )
  print("PASSWORD = ", row[2] )
  print("AGE = ", row[3], "\n" )

  password_hash = row[2]
  print(password_hash)

  user_password = input("Please Verify your Password: ")

  valid_password = bcrypt.hashpw(user_password.encode(), password_hash) == password_hash

  if valid_password:
    print("Password is valid!")
  else:
    print("Invalid Credentials")

print("Data returns successfully")

conn.close()
print("Connection Closed")