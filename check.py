import pandas as pd
import json
import os.path



def main() -> None:
    # Quarterfall object containing the data
    qf = {}

    # read the data from QF json file if it exists
    if os.path.exists('qf.json'):
        json_file = open('qf.json')
        qf = json.load(json_file)
        json_file.close()

    
    # read the Excel file
    df = pd.read_excel("answer.xlsx")
    print(df)

    # verify that the computed value in the cell is correct
    computed_value = df["Test"][3]
    qf["sumCorrectlyComputed"] = bool(computed_value == 6)

    # write the qf data to the json file
    outfile = open('qf.json', 'w')
    json.dump(qf, outfile)
    outfile.close()

if __name__ == "__main__":
    main()