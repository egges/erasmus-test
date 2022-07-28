import pandas as pd

def main() -> None:
    df = pd.read_excel("answer.xlsx")
    print(df)

if __name__ == "__main__":
    main()