import tkinter as tk
from tkinter import ttk
from obspy.taup import TauPyModel

'''
Aplicación de visualización de rayos sísmicos.

Desarrollado por Francisca Guiñez Rivas.

2024
'''

class WavePathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wave Path App")

        # Inicializar valores de profundidad y distancia epicentral
        self.depth_km = tk.DoubleVar(value=10)
        self.distance_deg = tk.DoubleVar(value=90)
        self.phase_list = tk.StringVar(value="PP")
        self.projection_type = tk.StringVar(value="Spherical")

        # Inicializar el modelo de velocidades de ObsPy
        self.model = TauPyModel(model="iasp91")

        # Crear input para la profundidad
        self.depth_label = ttk.Label(root, text="Depth (km):")
        self.depth_label.grid(row=0, column=0, padx=10, pady=5)
        self.depth_entry = ttk.Entry(root, textvariable=self.depth_km)
        self.depth_entry.grid(row=0, column=1, padx=10, pady=5)

        # Crear input para la distancia epicentral
        self.distance_label = ttk.Label(root, text="Epicentral distance (deg):")
        self.distance_label.grid(row=1, column=0, padx=10, pady=5)
        self.distance_entry = ttk.Entry(root, textvariable=self.distance_deg)
        self.distance_entry.grid(row=1, column=1, padx=10, pady=5)

        # Crear input para la lista de fases
        self.phase_label = ttk.Label(root, text="Phase List (comma separated):")
        self.phase_label.grid(row=2, column=0, padx=10, pady=5)
        self.phase_entry = ttk.Entry(root, textvariable=self.phase_list)
        self.phase_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botones para seleccionar tipo de proyección
        self.projection_label = ttk.Label(root, text="Projection Type:")
        self.projection_label.grid(row=3, column=0, padx=10, pady=5)
        self.cartesian_button = ttk.Radiobutton(root, text="Cartesian", variable=self.projection_type, value="cartesian")
        self.cartesian_button.grid(row=3, column=1, padx=10, pady=5)
        self.spherical_button = ttk.Radiobutton(root, text="Spherical", variable=self.projection_type, value="spherical")
        self.spherical_button.grid(row=3, column=2, padx=10, pady=5)

        # Botón para actualizar el gráfico
        self.update_button = ttk.Button(root, text="Update Plot", command=self.plot_p_wave_path)
        self.update_button.grid(row=4, column=1, padx=10, pady=5)

        # Configurar el evento de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def plot_p_wave_path(self):
        depth = self.depth_km.get()
        distance = self.distance_deg.get()
        phase_list = self.phase_list.get().split(',')
        projection = self.projection_type.get()

        # Graficar la trayectoria de ondas
        arrivals = self.model.get_ray_paths(source_depth_in_km=depth, distance_in_degree=distance, phase_list=phase_list)
        arrivals.plot_rays(plot_type=projection, legend=True, phase_list=phase_list)

    def on_close(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = WavePathApp(root)
    root.mainloop()
