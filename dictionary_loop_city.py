"""
Dictionaries: hier werden Daten in Schlüssel-Wert-Paaren gespeichert.
Im Gegensatz zu Listen, die über Indizes auf Elemente zugreifen, verwenden Dictionaries Schlüssel, um auf die zugehörigen Werte zuzugreifen.

Diese Schlüssel müssen immutable (unveränderlich) sein!
Dementsprechend: können die Schlüssel Strings, Zahlen oder Tupel sein,  aber keine Listen oder andere Dictionaries!!!Ai

Data is stored in key-value pairs.
In contrast to lists, which access elements via indices, dictionaries use keys to access the associated values.

These keys must be immutable!
Accordingly: the keys can be strings, numbers or tuples, but not lists or other dictionaries!!!
"""



countryCities = {
    "Germany": "Berlin",
    "France": "Paris",
    "Norway": "Oslo"
}

found = False
askCity = input("City: ")

for eachCountry in countryCities:
    if askCity == countryCities[eachCountry]:
        print(f"Found. It's the capital of {eachCountry}")
        found = True  # Wichtig: found auf True setzen
        break  # Wichtig: Schleife beenden, sobald die Stadt gefunden wurde

if not found:  # Überprüfung NACH der Schleife
    print("Sorry, the city you entered wasn't found in my system.")