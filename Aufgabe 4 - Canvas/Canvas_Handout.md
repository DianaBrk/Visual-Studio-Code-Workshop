Grundlegende Elemente in Tkinter:

Tk: Hauptfenster der Anwendung.
Label: Zeigt Text oder Bilder an.
Button: Führt eine Aktion aus, wenn er geklickt wird.
Entry: Ermöglicht die Eingabe von Text.
Frame: Container für andere Widgets.
Canvas: Ermöglicht das Zeichnen von Formen, Linien oder das Anzeigen von Bildern.

Erstellen eines Hauptfensters:


    import tkinter as tk

    root = tk.Tk()
    root.title("Meine Tkinter-Anwendung")
    root.geometry("800x600")  # Breite x Höhe
    root.mainloop()
    tk.Tk(): Erstellt das Hauptfenster.
    title(): Setzt den Titel des Fensters.
    geometry(): Setzt die Größe des Fensters.
    mainloop(): Startet die Ereignisschleife.


Einführung in das Canvas-Widget
Das Canvas-Widget ist ein vielseitiges Werkzeug zum Zeichnen von Formen, Linien und Bildern.

Canvas erstellen und anzeigen:

    canvas = tk.Canvas(root, bg="white", width=800, height=600)
    canvas.pack()


tk.Canvas(): Erstellt ein Canvas-Widget.
bg: Hintergrundfarbe des Canvas.
width und height: Setzen die Größe des Canvas.
pack(): Platziert das Canvas im Hauptfenster.


Zeichnen auf dem Canvas

Kreise und Ovale:

    canvas.create_oval(x1, y1, x2, y2, fill="red", outline="")

create_oval(): Zeichnet einen Kreis oder eine Ellipse.
x1, y1, x2, y2: Koordinaten des Begrenzungsrechtecks.
fill: Füllfarbe der Form.
outline: Farbe der Umrandung (leerlassen für keine Umrandung).


Rechtecke:

    canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="")

create_rectangle(): Zeichnet ein Rechteck.
x1, y1, x2, y2: Koordinaten der gegenüberliegenden Ecken.
fill: Füllfarbe des Rechtecks.
outline: Farbe der Umrandung (leerlassen für keine Umrandung).


    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=2)

    canvas.bind("<B1-Motion>", paint)


bind(): Bindet eine Funktion an ein Ereignis.

"<B1-Motion>": Ereignis, das auftritt, wenn die linke Maustaste gedrückt wird und die Maus bewegt wird.

paint: Die Funktion, die ausgeführt wird.

Farbwechsel:

    def change_color(new_color):
        global current_color
        current_color = new_color


global: Schlüsselwort, um eine Variable außerhalb der Funktion zu ändern.




