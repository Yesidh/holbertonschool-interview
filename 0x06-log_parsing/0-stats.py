#!/usr/bin/python3
"""
===========================
interview preparation
===========================
"""

import sys
import re

pattern_error = re.compile(r'\s(\d{3})\s')
pattern_size = re.compile(r'\s(\d{3})$')
text_to_search = sys.stdin.readline()
files_size = 0
ten_times = 0
errors_code = [200, 301, 400, 401, 403, 404, 405, 500]
errors_code_count = [0, 0, 0, 0, 0, 0, 0, 0]

while (text_to_search):
    match_pattern_error = pattern_error.finditer(text_to_search)
    match_pattern_size = pattern_size.finditer(text_to_search)
    for match in match_pattern_error:
        if int(match.group(1)) in errors_code:
            index_error = errors_code.index(int(match.group(1)))
            errors_code_count[index_error] += 1
    for match in match_pattern_size:
        files_size += int(match.group(1))
    text_to_search = sys.stdin.readline()

    if (ten_times == 9):
        print("File size: ", files_size)
        for ecode, cerror in zip(errors_code, errors_code_count):
            if cerror > 0:
                print("{}: {}".format(ecode, cerror))
        ten_times = -1
    ten_times += 1
