# wohnungen

Neue Wohnungsangebote aus beliebigen Immobilienportalen werden automatisch auf deiner E-Mail geschickt. 

## How-to-use

### Vorbereitung
1. Python 2.7 installieren
2. wohn.py öffnen und die kompletten Links aus immobilienscout24, ebay, immonet in die jeweiligen Methoden kopieren.
3. Eine Dummy E-Mail Account machen und die in die send-mail Methode hinzufügen. (Hinweis: "Recipient" ist deine richtige E-Mail Adresse, wo die Angebote weitergeleitet werden.)

### Das Programm starten
4. pip install -r requirements.txt ausführen
5. python wohn.py ausführen

### Anmerkungen

Man kann nach freier Wahl noch mehrere Portalen hinzufügen. Einfach das Logik kopieren.
Die Links werden noch zusätzlich in einer .txt-Datei gespeichert ('test.txt)
Am sinnvollsten ein Cronjob einrichten um den Skript automatisch ausführen (je nach Interval.)

