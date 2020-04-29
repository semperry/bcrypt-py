import sqlite3

conn = sqlite3.connect('demo.db')
print("Opened Database Connection")
user_id = input("Enter an ID to delete \n")
conn.execute(f"DELETE FROM EMPLOYEES where ID = {user_id}")
conn.commit()

print("DATA Delete a Success")

conn.close()