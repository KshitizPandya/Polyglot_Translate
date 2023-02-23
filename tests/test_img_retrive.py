import mysql.connector
import os
from ImageOCR_trans import lang, image_path, ocr, trans

def main():
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


        
    # Use a SELECT statement to retrieve the image data from the database
    sql = "SELECT photos FROM translations WHERE id = %s"
    val = (25,) # replace 1 with the ID of the image you want to retrieve
    mycursor.execute(sql, val)

    # Fetch the result of the SELECT statement
    result = mycursor.fetchone()

    # Determine the file extension based on the first few bytes of the binary data
    file_type = ""
    if result[0][0:4] == b"\x89PNG":
        file_type = ".png"
    elif result[0][0:2] == b"\xff\xd8":
        file_type = ".jpg"
    else:
        raise ValueError("Unsupported file format.")

    # Open a file with the appropriate extension in binary write mode in the photos folder
    file_path = os.path.join("C:/xampp66/htdocs/python/photos/", f"image{file_type}")
    with open(file_path, "wb") as image_file:
        # Write the binary data to the file
        image_file.write(result[0])

   

if __name__ == "__main__":
    main()
