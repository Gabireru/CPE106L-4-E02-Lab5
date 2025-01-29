import sqlite3
import os

DATABASE_FILE = os.path.join(os.path.dirname(__file__), "ColonialAdventure.db")

DROP_TABLES_SQL = os.path.join(os.path.dirname(__file__), "OracleDropColonial.sql")
CREATE_TABLES_SQL = os.path.join(os.path.dirname(__file__), "OracleColonial.sql")

def execute_sql_file(filename, connection):
    try:
        with open(filename, "r") as file:
            sql_script = file.read()
        print(f"Executing SQL from {filename}:")  # Debugging: Shows which file is being executed

        """
        print(sql_script)  # Debugging: Print SQL script to verify content
        """

        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()
    except Exception as e:
        print(f"Error executing {filename}: {e}")

def execute_query(connection, query, description):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        print(f"\n{description}:")
        if results:
            for row in results:
                print(row)
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error executing query ({description}): {e}")

# Queries
queries = {
    "a": {
        "description": "Participant details",
        "query": """
        SELECT CUSTOMER_NUM, LAST_NAME, FIRST_NAME, ADDRESS, CITY, STATE, POSTAL_CODE, PHONE
        FROM CUSTOMER;
        """
    },
    "b": {
        "description": "Adventure class details",
        "query": """
        SELECT TRIP_ID, TRIP_NAME, START_LOCATION, STATE, DISTANCE, MAX_GRP_SIZE, TYPE, SEASON
        FROM TRIP;
        """
    },
    "c": {
        "description": "Participant enrollments",
        "query": """
        SELECT c.CUSTOMER_NUM, c.LAST_NAME, c.FIRST_NAME, t.TRIP_ID, t.TRIP_NAME, r.TRIP_DATE
        FROM RESERVATION r
        JOIN CUSTOMER c ON r.CUSTOMER_NUM = c.CUSTOMER_NUM
        JOIN TRIP t ON r.TRIP_ID = t.TRIP_ID;
        """
    },
    "d": {
        "description": "Class participants",
        "query": """
        SELECT r.TRIP_DATE, t.TRIP_ID, t.TRIP_NAME, c.CUSTOMER_NUM, c.LAST_NAME, c.FIRST_NAME
        FROM RESERVATION r
        JOIN CUSTOMER c ON r.CUSTOMER_NUM = c.CUSTOMER_NUM
        JOIN TRIP t ON r.TRIP_ID = t.TRIP_ID;
        """
    }
}

# Driver code
def main():
    connection = sqlite3.connect(DATABASE_FILE)

    try:
        print("Dropping tables...")
        execute_sql_file(DROP_TABLES_SQL, connection)

        # Create and populate tables
        print("Creating tables...")
        execute_sql_file(CREATE_TABLES_SQL, connection)

        # Execute and display queries
        print("Executing queries...")
        for key in queries:
            execute_query(connection, queries[key]["query"], queries[key]["description"])

    except Exception as e:
        print("Error:", e)

    finally:
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
