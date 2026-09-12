import tkinter as tk
from typing import Callable

from servicios.restaurante_servicio import RestauranteServicio


class MainView(tk.Frame):
    def __init__(self, contenedor: tk.Widget, servicio: RestauranteServicio,
                 al_cerrar_sesion: Callable[[], None]) -> None:
        super().__init__(contenedor)
        self.servicio: RestauranteServicio = servicio
        self.al_cerrar_sesion: Callable[[], None] = al_cerrar_sesion

        tk.Label(self, text="Panel principal - JoelFood", font=("Arial", 16, "bold")).pack(pady=10)

        barra_opciones = tk.Frame(self)
        barra_opciones.pack(pady=5)

        tk.Button(barra_opciones, text="Productos", command=self.mostrar_productos).pack(side="left", padx=5)
        tk.Button(barra_opciones, text="Usuarios", command=self.mostrar_usuarios).pack(side="left", padx=5)
        tk.Button(
            barra_opciones, text="Ventas (pendiente)", command=self.mostrar_ventas_pendiente
        ).pack(side="left", padx=5)

        self.lista_informacion = tk.Listbox(self, width=70, height=15)
        self.lista_informacion.pack(pady=10, fill="both", expand=True, padx=10)

        tk.Button(self, text="Cerrar sesión", command=self.al_cerrar_sesion).pack(pady=10)

    def actualizar_listas(self) -> None:
        self.mostrar_productos()

    def mostrar_productos(self) -> None:
        self.lista_informacion.delete(0, tk.END)
        productos = self.servicio.listar_productos()

        if not productos:
            self.lista_informacion.insert(tk.END, "No hay productos registrados.")
            return

        for informacion in productos:
            self.lista_informacion.insert(tk.END, informacion)

    def mostrar_usuarios(self) -> None:
        self.lista_informacion.delete(0, tk.END)
        usuarios = self.servicio.listar_usuarios()

        if not usuarios:
            self.lista_informacion.insert(tk.END, "No hay usuarios registrados.")
            return

        for informacion in usuarios:
            self.lista_informacion.insert(tk.END, informacion)

    def mostrar_ventas_pendiente(self) -> None:
        self.lista_informacion.delete(0, tk.END)
        self.lista_informacion.insert(tk.END, "Funcionalidad de ventas pendiente de implementación gráfica.")
