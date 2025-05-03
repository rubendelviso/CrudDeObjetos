import re
from datetime import datetime


class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            # validar formato de fecha dd/mm/aaaa con expresiones regulres
            if not self.es_fecha_valida(fecha_str):
                raise ValueError(
                    'Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)  

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"


class Menu:
    def __init__(self):
        self.opciones_menu = ['1. Crear nuevo alumno', '2. Modificar alumno', '3. Eliminar alumno',
                              '4. Ver alumnos', '5. Buscar alumno por Codigo de Alumno', '6. Salir del programa']

    def mostrar_menu(self) -> None:
        for opcion in self.opciones_menu:
            print(opcion)

    def pedir_opcion_de_menu_valida(self) -> int:
        opcion_seleccionada = ''
        while not opcion_seleccionada.isnumeric() or \
                int(opcion_seleccionada) not in range(1, len(self.opciones_menu)+1):
            opcion_seleccionada = input('Seleccione una opción del menú: ') 
            if not opcion_seleccionada.isnumeric() or \
                    int(opcion_seleccionada) not in range(1, len(self.opciones_menu)+1):
                print(
                    f'Opción no válida. Debe ser un número entre 1 y {len(self.opciones_menu)}')
        return int(opcion_seleccionada)


class Alumno:
    def __init__(self, cod_alumno: int, apellido_nombre: str, telefono: str, fecha_nacimiento: Fecha):
        self.cod_alumno = cod_alumno
        self.apellido_nombre = apellido_nombre
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"ALUMNO {self.cod_alumno}: {self.apellido_nombre} - Tel: {self.telefono} - Fecha nac: {self.fecha_nacimiento}"


class GestorDeAlumnos:
    def __init__(self):
        self.alumnos: list[Alumno] = []

    def _es_fecha_nacimiento_valida(self, fecha_str: str) -> bool:
        try:
            Fecha(fecha_str)
            return True
        except ValueError:
            return False

    def _pedir_fecha_nacimiento_valida(self) -> Fecha:
        fecha_nacimiento = 'NO_VALIDA'
        while not self._es_fecha_nacimiento_valida(fecha_nacimiento):
            fecha_nacimiento = input(
                'Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa): ')
            if not self._es_fecha_nacimiento_valida(fecha_nacimiento):
                print('Formato de fecha no válido. Debe ser dd/mm/aaaa')
        return Fecha(fecha_nacimiento)

    def agregar_alumno(self):
        apellido_nombre = input('Ingrese Apellido y Nombre del alumno: ')
        telefono = input('Ingrese el teléfono del alumno: ')
        fecha_nacimiento = self._pedir_fecha_nacimiento_valida()
        nuevo_alumno = Alumno(len(self.alumnos) + 1,
                              apellido_nombre, telefono, fecha_nacimiento)
        self.alumnos.append(nuevo_alumno)

    def buscar_alumno_por_codigo(self, cod_alumno: int) -> Alumno:
        for alumno in self.alumnos:
            if alumno.cod_alumno == cod_alumno:
                return alumno
        return None

    def modificar_alumno(self):
        # La función de modificar solo permitirá modificar el telefono.
        cod_alumno = int(
            input('Ingrese el código del alumno a modificar: '))
        alumno_a_modificar = self.buscar_alumno_por_codigo(cod_alumno)
        if alumno_a_modificar:
            print(f"Se va a modificar el alumno: {alumno_a_modificar}")
            nuevo_telefono = input(
                f'Ingrese el nuevo teléfono para {alumno_a_modificar.apellido_nombre}: ')
            alumno_a_modificar.telefono = nuevo_telefono
            print(f"Alumno modificado correctamente: {alumno_a_modificar}")
        else:
            print('No se encontró el alumno con el código ingresado')

    def eliminar_alumno(self):
        cod_alumno = int(
            input('Ingrese el código del alumno a eliminar: '))
        alumno_a_eliminar = self.buscar_alumno_por_codigo(cod_alumno)
        if alumno_a_eliminar:
            print(f"Se va a eliminar el alumno: {alumno_a_eliminar}")
            confirmacion = input(
                "¿Está seguro que desea eliminar el alumno? (S/N)")
            if confirmacion.lower() in ('s', 'si', 'sí'):
                self.alumnos.remove(alumno_a_eliminar)
                print("Alumno eliminado correctamente")
            else:
                print("Eliminación cancelada.")
        else:
            print('No se encontró el alumno con el código ingresado')

    def ver_alumnos(self):
        print('Listado de alumnos:')
        for alumno in self.alumnos:
            print(alumno)


def main():
    menu = Menu()
    gestor_alumnos = GestorDeAlumnos()
    while True:
        menu.mostrar_menu()
        opcion_seleccionada = menu.pedir_opcion_de_menu_valida()
        if opcion_seleccionada == 1:
            gestor_alumnos.agregar_alumno()
        elif opcion_seleccionada == 2:
            gestor_alumnos.modificar_alumno()
        elif opcion_seleccionada == 3:
            gestor_alumnos.eliminar_alumno()
        elif opcion_seleccionada == 4:
            gestor_alumnos.ver_alumnos()
        elif opcion_seleccionada == 5:
            cod_alumno = int(input('Ingrese el código del alumno a buscar: '))
            alumno_buscado = gestor_alumnos.buscar_alumno_por_codigo(
                cod_alumno)
            if alumno_buscado:
                print(f"Alumno encontrado: {alumno_buscado}")
            else:
                print('No se encontró el alumno con el código ingresado')
        elif opcion_seleccionada == 6:
            print('Saliendo del programa...')
            break
        else:
            print("Opción inválida")
        print()


main()