# MySQL Database Schema and Data Exporter

This Python script allows you to export the schema and data of all tables from a MySQL database into a text file. It creates a text file containing the creation and insertion commands for each table, facilitating the replication of the database schema and data in another environment.

## How it Works

The script first establishes a connection to the MySQL database based on user input for the host, user, port, and password. Additional configurations can also be provided. It then retrieves the list of tables in the database and generates the SQL commands for creating the tables and inserting their data. The output is stored in a text file named `insertion_commands.txt`.

## Setup and Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:
    ```
    pip install mysql-connector
    ```
3. Run the script `export_mysql_data.py`.
4. Follow the prompts to provide the necessary database connection details and additional configurations.
5. The script will generate the `insertion_commands.txt` file containing the SQL commands.

## Requirements

- Python 3.x
- mysql-connector

## Note

- Make sure to have proper access rights to the MySQL database from which you are trying to export the data.
- Ensure that the `insertion_commands.txt` file is not overwritten unintentionally, as it contains crucial SQL commands for recreating the database schema and data.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
