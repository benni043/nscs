import csv

def csv_to_ldif(csv_file, ldif_file):
    """
    Convert CSV data to LDIF format.

    CSV Format: string (Klasse), string (Familienname), string (Vorname), char (m/w), string (Email)
    """
    with open(csv_file, 'r', encoding='latin-1') as csvfile, open(ldif_file, 'w', encoding='latin-1') as ldiffile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Skip header row if present

        for row in reader:
            klasse, familienname, vorname, geschlecht, email = row

            # Write LDIF entry
            ldiffile.write(f"""
dn: cn={vorname} {familienname}, ou=users, o=if, dc=huff,dc=lan
objectclass: top
objectclass: person
objectclass: organizationalPerson
objectclass: inetOrgPerson
objectclass: posixAccount
cn: {vorname} {familienname}
displayName: {vorname} {familienname}
sn: {familienname}
givenName: {vorname}
initials: {vorname[0]}{familienname[0]}
title: Dr
uid: {vorname}
mail: {email}
roomNumber: N326
uidNumber: 5000
gidNumber: 5000
homeDirectory: /home/{vorname}
userPassword: {vorname}
""".strip() + "\n\n")

if __name__ == "__main__":
    # Example usage
    csv_file = '5AHIF_2425.CSV'  # Input CSV file
    ldif_file = 'users.ldif'  # Output LDIF file

    csv_to_ldif(csv_file, ldif_file)
    print(f"LDIF file '{ldif_file}' has been created.")
