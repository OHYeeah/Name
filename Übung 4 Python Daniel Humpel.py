deutsche_woerter = ["Apfel", "Birne", "Marille"]
englische_woerter = ["Apple", "Pear", "Apricot"]

deutsch = input("Gib ein deutsches Wort ein (Apfel, Birne oder Marille): ")

for i in range(len(deutsche_woerter)):
    if deutsch == deutsche_woerter[i]:
        print("Englische Übersetzung:", englische_woerter[i])
        break
else:
    print("Das eingegebene Wort wurde nicht gefunden.")
