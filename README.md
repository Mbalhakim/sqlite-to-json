# SQLite to JSON Exporter

This Python script exports the contents of a SQLite database to a JSON file. It features a simple GUI using Tkinter for selecting the SQLite database and specifying the output JSON file.

## Features

- **GUI File Selection:**  
  Use file dialogs to select the SQLite database and specify the output JSON file.

- **Complete Database Export:**  
  The script retrieves all tables from the database. For each table, it fetches column information and all rows, converting them into a list of dictionaries.

- **JSON Output:**  
  Exports the database as a JSON object where each key is a table name and its value is a list of row dictionaries.

- **Error Handling:**  
  Displays error messages if the file selection is canceled or if any error occurs during the export process.

## Requirements

- Python 3.x  
- Tkinter (usually included with Python installations)

## How It Works

1. **Select the Database:**  
   When you run the script, a file dialog will prompt you to select your SQLite database file (e.g., `database.sqlite` or `data.db`).

2. **Choose Output File:**  
   Another dialog lets you choose where to save the JSON file. By default, the script suggests a name based on the SQLite file name (e.g., `database.json`).

3. **Database Export:**  
   The script connects to the SQLite database using Python’s `sqlite3` module. It retrieves the list of tables, gets the schema and rows for each table, and then converts the rows to dictionaries.

4. **JSON Creation:**  
   All tables and their rows are stored in a dictionary which is then written to a JSON file using Python’s `json` module.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/sqlite-to-json-exporter.git
   cd sqlite-to-json-exporter
   
   pip install -r requirements.txt
   
    python export_sqlite_to_json.py
   ```

