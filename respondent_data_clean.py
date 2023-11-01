import pandas as pd
import sys

def clean_and_merge(contact_info_file, other_info_file, output_file):
    contact_df = pd.read_csv(contact_info_file)
    other_df = pd.read_csv(other_info_file)
    merged_df = pd.merge(contact_df, other_df, on='respondent_id')

    def convert_birthdate(date_str):
        date_str = str(date_str).zfill(8)
        return pd.to_datetime(date_str, format='%m%d%Y').strftime('%Y-%m-%d')
    
    merged_df['birthdate'] = merged_df['birthdate'].apply(convert_birthdate)

    merged_df.to_csv(output_file, index=False)


if __name__ == '__main__':
    contact_info_file, other_info_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    clean_and_merge(contact_info_file, other_info_file, output_file)