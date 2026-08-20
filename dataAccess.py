import mysql.connector

db = mysql.connector.connect(
    host = "fh24002.mitaspit.dk",
    user = "fh24002_fh24002",
    password = "K06!tjT#Z6vqK9",
    database = "fh24002_Python_DB",
    port = "3306"
)

if db.is_connected():
    print("live");

cursor = db.cursor();

cursor.execute("select * from msg");

rows = cursor.fetchall();
for row in rows:
    print(row);

