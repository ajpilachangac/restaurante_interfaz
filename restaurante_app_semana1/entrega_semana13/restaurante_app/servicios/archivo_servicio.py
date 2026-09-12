import json
from pathlib import Path
from typing import List

from modelos.producto import Producto
from modelos.usuario import Usuario

CARPETA_DATOS: Path = Path(__file__).resolve().parent.parent / "datos"
RUTA_PRODUCTOS: Path = CARPETA_DATOS / "productos.json"
RUTA_USUARIOS: Path = CARPETA_DATOS / "usuarios.json"


class ArchivoServicio:
    def cargar_productos(self) -> List[Producto]:
        registros = self.__leer_json(RUTA_PRODUCTOS)
        productos: List[Producto] = []
        for registro in registros:
            try:
                productos.append(Producto.crear_desde_diccionario(registro))
            except KeyError as error:
                print(f"Registro de producto incompleto, se omite: falta la clave {error}")
        return productos

    def cargar_usuarios(self) -> List[Usuario]:
        registros = self.__leer_json(RUTA_USUARIOS)
        usuarios: List[Usuario] = []
        for registro in registros:
            try:
                usuarios.append(Usuario.crear_desde_diccionario(registro))
            except KeyError as error:
                print(f"Registro de usuario incompleto, se omite: falta la clave {error}")
        return usuarios

    def __leer_json(self, ruta: Path) -> list:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print(f"No se encontró el archivo {ruta.name}. Se usará una lista vacía.")
            return []
        except json.JSONDecodeError:
            print(f"El archivo {ruta.name} contiene datos inválidos. Se usará una lista vacía.")
            return []
        except PermissionError:
            print(f"No se tienen permisos para leer {ruta.name}. Se usará una lista vacía.")
            return []
