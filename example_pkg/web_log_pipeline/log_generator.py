import os
import sys
import random
import subprocess
from faker import Faker
from datetime import datetime


LINE = """\
{remote_addr} - - [{time_local} +0000] "{request_type} {request_path} HTTP/1.1" {status} {body_bytes_sent} "{http_referer}" "{http_user_agent}"\
"""


def generate_log_line():
    """ Generate fake (but somewhat realistic) log record """
    fake = Faker()
    now = datetime.now()
    remote_addr = fake.ipv4()
    time_local = now.strftime('%d/%b/%Y:%H:%M:%S')
    request_type = random.choice(["GET", "POST", "PUT"])
    request_path = "/" + fake.uri_path()

    status = random.choice([200, 401, 403, 404, 500])
    body_bytes_sent = random.choice(range(5, 1000, 1))
    http_referer = fake.uri()
    http_user_agent = fake.user_agent()

    log_line = LINE.format(
        remote_addr=remote_addr,
        time_local=time_local,
        request_type=request_type,
        request_path=request_path,
        status=status,
        body_bytes_sent=body_bytes_sent,
        http_referer=http_referer,
        http_user_agent=http_user_agent
    )
    return log_line


def write_log_line(log_file, line):
    """ Write each single log entry into log file """
    with open(log_file, "a") as f:
        f.write(line)
        f.write("\n")
        
        
def generate_log_file(log_file:str, log_max:int):
    """ 
    Generate a web-log file with defined size.
    :param log_file: Output text file to be generated
    :param log_max: Maximal number of log entries
    """
    current_log_file = log_file
    lines_written = 0
    
    while lines_written != log_max:
        line = generate_log_line()
        write_log_line(current_log_file, line)
        lines_written += 1
    print("{}{}{}".format("Log file with length ", log_max, " successfully generated"))      