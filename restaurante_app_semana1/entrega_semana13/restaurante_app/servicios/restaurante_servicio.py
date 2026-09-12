from typing import List, Optional

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self) -> None:
        self.__archivo_servicio: ArchivoServicio = ArchivoServicio()
        self.__productos: List[Producto] = self.__archivo_servicio.cargar_productos()
        self.__usuarios: List[Usuario] = self.__archivo_servicio.cargar_usuarios()

    def validar_acceso(self, nombre_usuario: str, contrasena: str) -> Optional[Usuario]:
        for usuario in self.__usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
                return usuario
        return None

    def listar_usuarios(self) -> List[str]:
        return [usuario.mostrar_informacion() for usuario in self.__usuarios]

    def listar_productos(self) -> List[str]:
        return [producto.mostrar_informacion() for producto in self.__productos]

    def consultar_cantidad(self, codigo_producto: str) -> Optional[int]:
        for producto in self.__productos:
            if producto.codigo == codigo_producto:
                return producto.stock
        return None
