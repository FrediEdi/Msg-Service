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



class DBClient:

    def Create(title : str, msg : str):
        query = "INSERT INTO msg (Title, Message) VALUES (%s, %s)"
        cursor.execute(query, (title, msg))
        db.commit();
        print("create", title, msg);

    def Read(arg : str): # Done
        cursor.execute("select * from msg");
        return cursor.fetchall();

    def Update(id : str, title : str, msg : str):
        query = "UPDATE msg SET Title = %s, Message = %s WHERE ID = %s"
        cursor.execute(query, (title, msg, id))
        db.commit();
        print("updateing:", id);

    def Delete(id : str):
        query = "DELETE FROM msg WHERE ID = %s"
        cursor.execute(query, (id,))
        db.commit();
        print("deleting:", id);