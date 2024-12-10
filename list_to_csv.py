import pandas as pd
import numpy as np
import math
import re
import csv
import matplotlib.pyplot as plt

def get_num(x):
    ret = re.findall(r'\d+', x)
    if ret == []:
        return x[:-3]
    else:
        return int(ret[0])

def list_to_csv(input_file):
    output_file = input_file.replace(".list", ".csv")

    pattern = r"^\s*(\S+)\s+([\d.]+)\s+([\d.]+)\s+([\d]+)\s+([\d]+)"

    rows = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                assignment, w1, w2, data_height, sn = match.groups()
                rows.append([assignment[:-3], float(w1), float(w2), int(data_height), int(sn),assignment])

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "w1", "w2", "Data Height", "S/N", "Assignment"])
        writer.writerows(rows)
