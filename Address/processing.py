

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

    addresses['Street_Suffix'] = addresses['Street_Name'].apply(
        lambda x: x.split()[-1] if isinstance(x, str) and x.split()[-1] in suffixes else None
    )

    addresses['Street_Name'] = addresses.apply(
        lambda row: ' '.join([word for word in str(row['Street_Name']).split()
                              if word not in directions and word not in suffixes]), axis=1
    )

    return addresses
