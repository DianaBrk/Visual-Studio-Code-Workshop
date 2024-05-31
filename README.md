# Liebe Kommilitoninnen und Kommilitonen,

am kommenden Donnerstag, den 06.06., findet unser Workshop zu "Visual Studio Code" statt.
Wir bitten euch folgende Schritte vor dem Workshop zu erledigen:

1. Visual Studio Code heruntergeladen (https://code.visualstudio.com/download)
2. URL für Pull: https://github.com/DianaBrk/Visual-Studio-Code-Workshop.git (Ihr müsst noch nichts pullen, einfach die URL abspeichern!)
3. Python installiert (https://www.python.org/downloads/) + PATH (Wichtig bei der Installation: Aktiviere das Kontrollkästchen „Add Python to PATH“ am unteren Rand des Installationsfensters)

Anleitung für Python Installation: https://code.visualstudio.com/docs/python/python-tutorial

Falls Python schon installiert ist, aber PATH nicht hinzugefügt worden ist folgende Schritte beachten:
Windows:

1. In Windows das Programm "Systemumgebungsvariablen bearbeiten" öffnen
2. Auf "Umgebungsvariablen..." klicken
3. In der unteren Box "Systemvariablen" auf die "Path"-Box klicken und auf "Bearbeiten..." klicken
4. Auf "Neu" klicken
5. Python PATH hinzufügen: C:\Users\<dein_username>\AppData\Local\Programs\Python\Python312

MAC:

1. Öffne das Terminal.
2. Bearbeite die .bash_profile, .zshrc oder .profile Datei im Home-Verzeichnis, je nachdem, welche Shell du verwendest.
   Beispiel: nano ~/.bash_profile
3. Füge die folgenden Zeilen am Ende der Datei hinzu:
   export PATH="/usr/local/bin/python3:$PATH"
4. Speichere die Datei (Ctrl + O und Enter) und schließe den Editor (Ctrl + X).
5. Lade die Änderungen neu: source ~/.bash_profile

Mit freundlichen Grüßen
Diana Brkic und Luca Rupp
