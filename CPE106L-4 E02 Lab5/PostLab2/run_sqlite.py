import sqlite3
import os

# Database and SQL files
DATABASE_FILE = os.path.join(os.path.dirname(__file__), "SolmarisCondominium.db")
DROP_TABLES_SQL = os.path.join(os.path.dirname(__file__), "OracleDropSolmaris.sql")
CREATE_TABLES_SQL = os.path.join(os.path.dirname(__file__), "OracleSolmaris.sql")

# Execute an SQL script from a file
def execute_sql_file(filename, connection):
    try:
        with open(filename, "r") as file:
            sql_script = file.read()
        print(f"Executing SQL from {filename}...")

        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()
        print("Execution successful.")

    except Exception as e:
        print(f"Error executing {filename}: {e}")

# Execute a query and display results
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

# Queries for the tasks
queries = {
    "a": {
        "description": "Renter Details",
        "query": """
        SELECT RenterID, FirstName, MiddleInitial, LastName, Address, City, State, PostalCode, TelephoneNumber, EmailAddress
        FROM RENTERS;
        """
    },
    "b": {
        "description": "Property Details",
        "query": """
        SELECT CondoLocationNumber, CondoLocationName, Address, City, State, PostalCode, CondoUnitNumber, SquareFootage, 
               NumberOfBedrooms, NumberOfBathrooms, MaxPersons, BaseWeeklyRate
        FROM PROPERTIES;
        """
    },
    "c": {
        "description": "Rental Agreement Details",
        "query": """
        SELECT ra.RenterID, ra.FirstName, ra.MiddleInitial, ra.LastName, ra.Address, ra.City, ra.State, ra.PostalCode, 
               ra.TelephoneNumber, ra.StartDate, ra.EndDate, ra.WeeklyRentalAmount
        FROM RENTAL_AGREEMENTS ra;
        """
    }
}

# Driver code
def main():
    connection = sqlite3.connect(DATABASE_FILE)

    try:
        print("Dropping existing tables...")
        execute_sql_file(DROP_TABLES_SQL, connection)

        print("Creating tables and inserting data...")
        execute_sql_file(CREATE_TABLES_SQL, connection)

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
