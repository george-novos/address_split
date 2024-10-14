

def split_street_direction_suffix(addresses):
    # List of street directions (like "N", "North")
    directions = ['N', 'S', 'E', 'W', 'North', 'South', 'East', 'West']
    # List of street suffixes (like "Street", "Avenue", "Boulevard")
    suffixes = ['St', 'Ave', 'Blvd', 'Rd', 'Road', 'Street', 'Avenue', 'Drive', 'Dr', 'Lane', 'Ln', 'Court', 'Ct',
                'Way', 'Cir', 'Ter', 'Trl', 'Plc', 'Pl', 'Trail', 'Pt', 'Pkwy']

    addresses['Street_Name'] = addresses['Street_Name'].str.lower()
    addresses['Street_Name'] = addresses['Street_Name'].str.title()

    addresses['Street_Direction'] = addresses['Street_Name'].apply(
        lambda x: x.split()[0] if isinstance(x, str) and x.split()[0] in directions else
        (x.split()[-1] if isinstance(x, str) and x.split()[-1] in directions else None)
    )

    addresses['Street_Type'] = addresses['Street_Name'].apply(
        lambda x: x.split()[-1] if isinstance(x, str) and x.split()[-1] in suffixes else None
    )

    addresses['Street_Name'] = addresses.apply(
        lambda row: ' '.join([word for word in str(row['Street_Name']).split()
                              if word not in directions and word not in suffixes]), axis=1
    )

    addresses['Prime_ID'] = ""
    addresses['COS_ID'] = ""
    addresses['BSL_ID'] = ""
    addresses["Status"] = ""
    addresses["Usage"] = ""
    addresses["Sub_Unit_Type"] = ""
    addresses["Sub_Unit_Number"] = ""
    addresses["Street_Suffix"] = ""
    addresses["Country"] = ""
    addresses["Splitter_Port"] = ""

    addresses.rename(columns={
        'Ready for Service Date': 'RFS_Date',
        'Zip_Code': 'Postal_Code'
    }, inplace=True)

    addresses = addresses.loc[:, ~addresses.columns.duplicated()]
    desired_order = ['Prime_ID', 'COS_ID', 'BSL_ID', 'Status', 'Usage', 'RFS_Date',
                     'Street_Number', 'Street_Direction', 'Street_Name', 'Street_Type',
                     'Street_Suffix', 'City', 'State', 'Postal_Code', 'Country', 'Sub_Unit_Type',
                     "Sub_Unit_Number", "Latitude", "Longitude", "Splitter_Port", "Address",
                     "Construction Complete Date", "Uploaded to Sales Rabbit",
                     "FDAName", "FDHName", "CF Address ID"]

    remaining_columns = [col for col in addresses.columns if col not in desired_order]
    addresses = addresses[desired_order + remaining_columns]

    return addresses
