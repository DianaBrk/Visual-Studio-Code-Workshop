import tkinter as tk


def setup_window():
    root = tk.Tk()
    root.title("Malanwendung")

    canvas = tk.Canvas(root, bg="white", width=800, height=600)
    canvas.pack()

    color_frame = tk.Frame(root)
    color_frame.pack()

    return root, canvas, color_frame


def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=0.01)


def change_color(new_color):
    global current_color
    current_color = new_color


def clear_canvas():
    canvas.delete("all")


def main():
    global current_color, canvas
    current_color = "black"

    root, canvas, color_frame = setup_window()

    canvas.bind("<B1-Motion>", paint)

    colors = ["black", "red", "yellow", "purple", "orange", "brown"]
    for color in colors:
        btn = tk.Button(
            color_frame, bg=color, width=2, height=1, command=lambda c=color: change_color(c)
            )
        btn.pack(side=tk.LEFT)

    clear_button = tk.Button(root, text="Clear", command=clear_canvas)
    clear_button.pack()

    root.mainloop()


if __name__ == "__main__":
   main()
