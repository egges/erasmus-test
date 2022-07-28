from typing import Any
import pandas as pd
import json
import os.path

QF_JSON = "qf.json"

def read_json_data() -> dict[str, Any]:
    if not os.path.exists(QF_JSON):
        return {}

    with open(QF_JSON) as json_file:
        return json.load(json_file)

def write_json_data(data: dict[str, Any]):
    with open('qf.json', 'w') as outfile:
        json.dump(data, outfile)

def main() -> None:
    # read the QF object data
    qf = read_json_data()
    
    # read the Excel file and print it to the console
    df = pd.read_excel("answer.xlsx")
    print(df)

    # verify that the computed value in cell A5 is correct
    qf["sumCorrectlyComputed"] = bool(df["Test"][3] == 6)

    # write the QF object data
    write_json_data(qf)
    

if __name__ == "__main__":
    main()