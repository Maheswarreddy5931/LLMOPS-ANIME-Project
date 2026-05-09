import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv
    
    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8', error_bad_lines=False).dropna()
        required_columns = {'Name','Genre','synopsis'}

        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError("missing required columns in the CSV")
        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " +df["sypnopsis"] + "Genres : " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv , index=False,encoding='utf-8')

        return self.processed_csv