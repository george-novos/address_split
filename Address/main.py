import pandas as pd
from Address.processing import split_street_direction_suffix

if __name__ == "__main__":
    print("Starting..")
    address_df = pd.read_excel('master_address_list.xlsx')
    processed_addresses_df = split_street_direction_suffix(address_df)
    processed_addresses_df.to_csv('processed_addresses.csv', index=False)
    print("Done")
