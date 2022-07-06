import mysql.connector # For connecting to dataset

from api_keys import config, createDBconfig, DB_name

##################### Start database connection and cursor #####################
def database_startup():
    try:
        db = mysql.connector.connect(**config) # Connect to a database with the config set in the parameters
        print ("Successfully connected to database:", DB_name, "\n")
        cursor = db.cursor() # Instantiate a cursor to work with the specified database
    except: #If there is no database yet, run the script twice. First will create the database then error out. the secondtime will run the actual program.
        print ("Couldnt create default cursor, trying to create the database instead")
        db2 = mysql.connector.connect(**createDBconfig) # Connect to a database with the config set in the parameters
        cursor2 = db2.cursor() # Instantiate a cursor to work with the specified database
        print ("Setup cursor for database creation.")

        def create_database():
            cursor2.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8mb4' COLLATE utf8mb4_0900_ai_ci".format(DB_name)) #https://dba.stackexchange.com/questions/76788/create-a-mysql-database-with-charset-utf-8
            print ("Database created:", DB_name)

        create_database()     # NOTE: When creating a database, need to remove the database parameter in the "config" dictionary.
        sys.exit("Database created, now exiting.") #exiting here so you run the script twice in case there is no database first.
    return db, cursor

if __name__ == "__main__":
    db, cursor = database_startup()
else:
    db, cursor = database_startup()