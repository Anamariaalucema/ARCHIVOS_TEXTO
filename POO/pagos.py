from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperatura_total = 0
        humedad_total = 0
        presion_total = 0
        velocidad_viento_total = 0
        direccion_viento_total = 0
        cantidad_registros = 0
        direccion_viento_grados = {
            'N': 0,
            'NNE': 22.5,
            'NE': 45,
            'ENE': 67.5,
            'E': 90,
            'ESE': 112.5,
            'SE': 135,
            'SSE': 157.5,
            'S': 180,
            'SSW': 202.5,
            'SW': 225,
            'WSW': 247.5,
            'W': 270,
            'WNW': 292.5,
            'NW': 315,
            'NNW': 337.5
        }
        direccion_viento_abreviaciones = {
            0: 'N',
            22.5: 'NNE',
            45: 'NE',
            67.5: 'ENE',
            90: 'E',
            112.5: 'ESE',
            135: 'SE',
            157.5: 'SSE',
            180: 'S',
            202.5: 'SSW',
            225: 'SW',
            247.5: 'WSW',
            270: 'W',
            292.5: 'WNW',
            315: 'NW',
            337.5: 'NNW'
        }

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.startswith('Temperatura:'):
                    temperatura = float(linea.split(':')[1].strip())
                    temperatura_total += temperatura
                elif linea.startswith('Humedad:'):
                    humedad = float(linea.split(':')[1].strip())
                    humedad_total += humedad
                elif linea.startswith('Presión:'):
                    presion = float(linea.split(':')[1].strip())
                    presion_total += presion
                elif linea.startswith('Viento:'):
                    viento = linea.split(':')[1].strip().split(',')
                    velocidad_viento = float(viento[0].strip())
                    direccion_viento = viento[1].strip()
                    velocidad_viento_total += velocidad_viento
                    direccion_viento_total += direccion_viento_grados[direccion_viento]

                cantidad_registros += 1

        temperatura_promedio = temperatura_total / cantidad_registros
        humedad_promedio = humedad_total / cantidad_registros
        presion_promedio = presion_total / cantidad_registros
        velocidad_viento_promedio = velocidad_viento_total / cantidad_registros
        direccion_viento_promedio = direccion_viento_total / cantidad_registros
        direccion_viento_predominante = direccion_viento_abreviaciones[min(direccion_viento_abreviaciones, key=lambda x: abs(x - direccion_viento_promedio))]

        return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_viento_predominante

datos = DatosMeteorologicos('datos_meteorologicos.sty')
temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_viento_predominante = datos.procesar_datos()

print(f'Temperatura promedio: {temperatura_promedio}')
print(f'Humedad promedio: {humedad_promedio}')
print(f'Presión promedio: {presion_promedio}')
print(f'Velocidad promedio del viento: {velocidad_viento_promedio}')
print(f'Dirección predominante del viento: {direccion_viento_predominante}')
