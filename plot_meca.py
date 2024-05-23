import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from obspy.imaging.beachball import beach

'''
Aplicación de visualización de mecanismos focales.

Desarrollado por Francisca Guiñez Rivas.

2024
'''


class FocalMechanismApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Focal Mechanism App")

        # Inicializar valores de strike, dip y rake
        self.strike = 0
        self.dip = 45
        self.rake = 90

        # Crear lienzo para la figura de mecanismo focal
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=24)

        # Crear sliders para ajustar strike, dip y rake
        self.create_sliders()

        # Graficar el mecanismo focal inicial
        self.plot_focal_mechanism()

        # Configurar el evento de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_sliders(self):
        # Slider para el ángulo de strike
        self.strike_label = tk.Label(self.root, text="Strike:")
        self.strike_label.grid(row=7, column=1, padx=1, pady=1, sticky="e")
        self.strike_slider = tk.Scale(self.root, from_=0, to=360, orient=tk.HORIZONTAL, command=self.update_strike)
        self.strike_slider.grid(row=7, column=2, padx=1, pady=1, sticky="ew")
        self.strike_slider.set(self.strike)

        # Casilla de entrada para el ángulo de strike
        self.strike_entry = tk.Entry(self.root)
        self.strike_entry.grid(row=8, column=2, padx=0, pady=0, sticky="ew")
        self.strike_entry.insert(0, str(self.strike))
        self.strike_entry.bind("<Return>", self.update_strike_entry)

        # Slider para el ángulo de dip
        self.dip_label = tk.Label(self.root, text="Dip:")
        self.dip_label.grid(row=11, column=1, padx=5, pady=5, sticky="e")
        self.dip_slider = tk.Scale(self.root, from_=0, to=90, orient=tk.HORIZONTAL, command=self.update_dip)
        self.dip_slider.grid(row=11, column=2, padx=5, pady=5, sticky="ew")
        self.dip_slider.set(self.dip)

        # Casilla de entrada para el ángulo de dip
        self.dip_entry = tk.Entry(self.root)
        self.dip_entry.grid(row=12, column=2, padx=5, pady=5, sticky="ew")
        self.dip_entry.insert(0, str(self.dip))
        self.dip_entry.bind("<Return>", self.update_dip_entry)

        # Slider para el ángulo de rake
        self.rake_label = tk.Label(self.root, text="Rake:")
        self.rake_label.grid(row=14, column=1, padx=5, pady=5, sticky="e")
        self.rake_slider = tk.Scale(self.root, from_=-180, to=180, orient=tk.HORIZONTAL, command=self.update_rake)
        self.rake_slider.grid(row=14, column=2, padx=5, pady=5, sticky="ew")
        self.rake_slider.set(self.rake)

        # Casilla de entrada para el ángulo de rake
        self.rake_entry = tk.Entry(self.root)
        self.rake_entry.grid(row=15, column=2, padx=5, pady=5, sticky="ew")
        self.rake_entry.insert(0, str(self.rake))
        self.rake_entry.bind("<Return>", self.update_rake_entry)

    def update_strike(self, value):
        self.strike = int(value)
        self.strike_entry.delete(0, tk.END)
        self.strike_entry.insert(0, str(self.strike))
        self.plot_focal_mechanism()

    def update_strike_entry(self, event):
        try:
            self.strike = int(self.strike_entry.get())
            self.strike_slider.set(self.strike)
            self.plot_focal_mechanism()
        except ValueError:
            pass

    def update_dip(self, value):
        self.dip = int(value)
        self.dip_entry.delete(0, tk.END)
        self.dip_entry.insert(0, str(self.dip))
        self.plot_focal_mechanism()

    def update_dip_entry(self, event):
        try:
            self.dip = int(self.dip_entry.get())
            self.dip_slider.set(self.dip)
            self.plot_focal_mechanism()
        except ValueError:
            pass

    def update_rake(self, value):
        self.rake = int(value)
        self.rake_entry.delete(0, tk.END)
        self.rake_entry.insert(0, str(self.rake))
        self.plot_focal_mechanism()

    def update_rake_entry(self, event):
        try:
            self.rake = int(self.rake_entry.get())
            self.rake_slider.set(self.rake)
            self.plot_focal_mechanism()
        except ValueError:
            pass

    def plot_focal_mechanism(self):
        self.ax.clear()
        b = beach([self.strike, self.dip, self.rake], xy=(0.5, 0.5), width=0.95, linewidth=1.5, facecolor='gray', edgecolor='k')
        self.ax.add_collection(b)
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.axis('off')
        self.canvas.draw()

    def on_close(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FocalMechanismApp(root)
    root.mainloop()

