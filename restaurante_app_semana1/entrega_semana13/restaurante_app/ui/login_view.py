import tkinter as tk
from typing import Callable

from servicios.restaurante_servicio import RestauranteServicio


class LoginView(tk.Frame):
    def __init__(self, contenedor: tk.Widget, servicio: RestauranteServicio,
                 al_iniciar_sesion: Callable[[], None]) -> None:
        super().__init__(contenedor)
        self.servicio: RestauranteServicio = servicio
        self.al_iniciar_sesion: Callable[[], None] = al_iniciar_sesion

        tk.Label(self, text="Restaurante JoelFood", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Label(self, text="Usuario:").pack()
        self.entrada_usuario = tk.Entry(self)
        self.entrada_usuario.pack()

        tk.Label(self, text="Contraseña:").pack()
        self.entrada_contrasena = tk.Entry(self, show="*")
        self.entrada_contrasena.pack()

        tk.Button(self, text="Ingresar", command=self.procesar_ingreso).pack(pady=15)

        self.etiqueta_mensaje = tk.Label(self, text="", fg="red")
        self.etiqueta_mensaje.pack()

    def procesar_ingreso(self) -> None:
        nombre_usuario: str = self.entrada_usuario.get().strip()
        contrasena: str = self.entrada_contrasena.get().strip()

        if not nombre_usuario or not contrasena:
            self.etiqueta_mensaje.config(text="Ingrese usuario y contraseña.", fg="red")
            return

        usuario_valido = self.servicio.validar_acceso(nombre_usuario, contrasena)

        if usuario_valido is None:
            self.etiqueta_mensaje.config(text="Credenciales incorrectas.", fg="red")
            return

        self.etiqueta_mensaje.config(text="")
        self.al_iniciar_sesion()

    def limpiar_campos(self) -> None:
        self.entrada_usuario.delete(0, tk.END)
        self.entrada_contrasena.delete(0, tk.END)
        self.etiqueta_mensaje.config(text="")
