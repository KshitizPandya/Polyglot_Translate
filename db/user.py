import mysql.connector
from ImageOCR_trans import lang, image_path, ocr, trans


        # Connect to the database
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="image_db"
        )

        # Create a cursor object to execute SQL statements
mycursor = mydb.cursor()

        # Execute SQL statement to insert data into the database
sql = "INSERT INTO translations (language, photos, original_text, translated_text) VALUES (%s,%s,%s,%s)"



val = (lang,image_path, ocr, trans)
mycursor.execute(sql, val)

        # Commit the changes to the database
mydb.commit()

        # Print a message to indicate that the data has been inserted successfully
print(mycursor.rowcount, "record inserted.")

