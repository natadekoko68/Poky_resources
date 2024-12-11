import re
import csv

def list_to_csv(input_file,remove_question=False):
    output_file = input_file.replace(".list", ".csv")

    pattern = r"^\s*(\S+)\s+([\d.]+)\s+([\d.]+)\s+([\d]+)\s+([\d]+)"

    rows = []
    if not remove_question:
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                match = re.match(pattern, line)
                if match:
                    assignment, w1, w2, data_height, sn = match.groups()
                    rows.append([assignment.split("-")[0], assignment.split("-")[-1], float(w1), float(w2), int(data_height), int(sn),assignment])
    else:
         with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                match = re.match(pattern, line)
                if match:
                    assignment, w1, w2, data_height, sn = match.groups()
                    rows.append([assignment.split("-")[0].replace("?",""), assignment.split("-")[-1].replace("?",""), float(w1), float(w2), int(data_height), int(sn),assignment])
       

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID1", "ID2", "w1", "w2", "Data Height", "S/N", "Assignment"])
        writer.writerows(rows)

if __name__ == "__main__":
    path = "path_to_list"
    list_to_csv(path)
    
