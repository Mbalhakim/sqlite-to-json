import sqlite3
import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def export_sqlite_to_json(db_path, json_path):
    try:
        # Connect to the SQLite database.
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get all tables in the database.
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        db_dict = {}

        for table in tables:
            table_name = table[0]

            # Get column names for the table.
            cursor.execute(f"PRAGMA table_info('{table_name}')")
            columns_info = cursor.fetchall()
            column_names = [col[1] for col in columns_info]

            # Retrieve all rows from the table.
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            # Convert rows to a list of dictionaries.
            rows_dicts = [dict(zip(column_names, row)) for row in rows]
            db_dict[table_name] = rows_dicts

        # Write the dictionary to a JSON file.
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(db_dict, json_file, indent=4, ensure_ascii=False)

        conn.close()
        return True, f"Exported {len(tables)} table(s) from '{os.path.basename(db_path)}' to '{os.path.basename(json_path)}'"
    except Exception as e:
        return False, str(e)

def select_files_and_export():
    root = tk.Tk()
    root.withdraw()  # Hide the main window.

    messagebox.showinfo("SQLite to JSON Exporter", "Please select the SQLite database file.")
    db_file = filedialog.askopenfilename(
        title="Select SQLite Database File",
        filetypes=[("SQLite Database", "*.sqlite;*.db"), ("All Files", "*.*")]
    )
    if not db_file:
        messagebox.showerror("Error", "No database file selected!")
        return

    # Suggest an output file name based on the database file name.
    default_json_name = os.path.splitext(os.path.basename(db_file))[0] + ".json"
    json_file = filedialog.asksaveasfilename(
        title="Save JSON Export As",
        initialfile=default_json_name,
        defaultextension=".json",
        filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
    )
    if not json_file:
        messagebox.showerror("Error", "No output file specified!")
        return

    success, message = export_sqlite_to_json(db_file, json_file)
    if success:
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Export Failed", message)

if __name__ == "__main__":
    select_files_and_export()
