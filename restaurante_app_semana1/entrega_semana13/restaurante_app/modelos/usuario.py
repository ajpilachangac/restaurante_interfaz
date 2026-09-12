class Usuario:
    def __init__(self, identificacion: str, nombre: str, nombre_usuario: str, contrasena: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.nombre_usuario: str = nombre_usuario
        self.contrasena: str = contrasena

    def mostrar_informacion(self) -> str:
        return f"{self.identificacion} | {self.nombre} | Usuario: {self.nombre_usuario}"

    @classmethod
    def crear_desde_diccionario(cls, datos: dict) -> "Usuario":
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            nombre_usuario=datos["nombre_usuario"],
            contrasena=datos["contrasena"],
        )
