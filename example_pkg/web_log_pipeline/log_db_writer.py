import os
import time
import sqlite3
from datetime import datetime


def create_table(db_name):
    """
    Create table logs in the SQLite database.
    The table schema is defined accroding to the log format.
    :param db_name: SQLite database name
    """
    conn = sqlite3.connect(db_name)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS logs (
      raw_log TEXT NOT NULL,
      remote_addr TEXT,
      time_local TEXT,
      request_type TEXT,
      request_path TEXT,
      status INTEGER,
      body_bytes_sent INTEGER,
      http_referer TEXT,
      http_user_agent TEXT,
      created DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    """)
    conn.close()
    

def parse_line(line):
    """
    Parse each log line by splitting it into structured fields.
    Extract all of the fields from the split representation. 
    :param line: A single web log record
    """
    split_line = line.split(" ")
    if len(split_line) < 12:
        return []
    remote_addr = split_line[0]
    time_local = split_line[3] + " " + split_line[4]
    request_type = split_line[5]
    request_path = split_line[6]
    status = split_line[8]
    body_bytes_sent = split_line[9]
    http_referer = split_line[10]
    http_user_agent = " ".join(split_line[11:])
    created = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    return [
        remote_addr,
        time_local,
        request_type,
        request_path,
        status,
        body_bytes_sent,
        http_referer,
        http_user_agent,
        created
    ]


def insert_record(db, line, parsed):
    """
    Insert a single parsed record into the logs table of the SQLite database.
    :param line: A single web log record
    :param parsed: A single web log record in parsed format
    """
    conn = sqlite3.connect(db, timeout=10)
    cur = conn.cursor()
    args = [line] + parsed # Parsed is a list of the values parsed earlier
    cur.execute('INSERT INTO logs VALUES (?,?,?,?,?,?,?,?,?,?)', args)
    conn.commit()
    conn.close()   
    
    
def insert_file_to_db(file_name, db_name):
    """
    Insert the whole parsed file into database.
    :param file_name: Web log file storing logs generated
    """
    if not os.path.isfile(db_name):
        create_table(db_name)
    try:
        f = open(file_name, "r")
        lines = f.readlines()
        for line in lines:
            parsed = parse_line(line.strip())
            time.sleep(1)
            insert_record(db_name, line, parsed)
        f.close()
    except KeyboardInterrupt: pass