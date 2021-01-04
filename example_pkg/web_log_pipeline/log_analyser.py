import csv
import sqlite3
import pandas as pd
from datetime import datetime


def parse_time(time_str):
    """Parse a string to timestamp format"""
    try:
        time_obj = datetime.strptime(time_str, '[%d/%b/%Y:%H:%M:%S %z]')
    except Exception as e:
        print(e)
        time_obj = ""
    return time_obj


def get_lines_browser(time_obj, db_name):
    """
    Query the browser information from a specified date or time
    :param time_obj: Datetime from which we collect the browser information
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT time_local,http_user_agent FROM logs WHERE created > ?", [time_obj])
    resp = cur.fetchall()
    return resp


def parse_user_agent(user_agent):
    """
    Parsing the user agent to retrieve the name of the browser
    :param user_agent: User agent information to be mapped with enumerated browsers
    """
    browsers = ["Firefox", "Chrome", "Opera", "Safari", "MSIE"]
    for browser in browsers:
        if browser in user_agent:
            return browser
    return "Other"


def get_time_and_ip_browser(lines):
    """Extract the ip and time from each row we queried."""
    browsers = []
    times = []
    for line in lines:
        times.append(parse_time(line[0]))
        browsers.append(parse_user_agent(line[1]))
    return browsers, times


def count_browser(year:int, month:int, day:int, db_name, output_csv):
    """
    Counter distinct browsers per day;
    Also define the constaint date to start the query.
    :param db_name: SQLite database name
    :param output_csv: Output csv file to write the query result
    """
    browser_counts = {}
    start_time = datetime(year=year, month=month, day=day)
    lines = get_lines_browser(time_obj=start_time, db_name=db_name)
    browsers, times = get_time_and_ip_browser(lines)
    if len(times) > 0:
        start_time = times[-1] 
    for browser, time_obj in zip(browsers, times):
        if browser not in browser_counts:
            browser_counts[browser] = 0
        browser_counts[browser] += 1
    count_list = sorted(browser_counts.items(), key=lambda x: x[0])
    with open(output_csv,'w') as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\r\n")
        writer.writerow(["browser", "count"])
        writer.writerows(count_list)

