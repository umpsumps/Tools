#!/usr/bin/python2.7

import os
import re
import csv

def parse_email(filename):
    
    regex   = r"\b([a-zA-Z0-9-_.<.*?>]+)@(\w+[.][a-zA-Z.]+)"
    pattern = re.compile(regex)
    with open('listemails.csv', 'wb') as f:
        writer = csv.writer(f)
        with open(filename) as input_file:
                for line in input_file:
                        matches = pattern.finditer(line)  # Gives an iterator of matches.
                        for match in matches:
                                group = match.groups()
                                email = group[0].split("<br>") + "@" + group[1].strip("\n.")  # Repair.
                                email = [email]
                                writer.writerows([email])
       
