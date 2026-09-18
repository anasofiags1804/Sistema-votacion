# Sistema de Votación

Sistema de votación simple en Python con registro de votos, visualización 
de resultados y guardado de historial — proyecto desarrollado en equipo 
usando Git con ramas y control de versiones.

## Funciones implementadas

### 1. Registro de votos (`rama1-registro`)
Permite registrar el voto de una persona por un candidato. Si la persona 
ya votó anteriormente, el sistema lo detecta y no permite votar de nuevo.
- **Desarrollado por:** Ana sofia

### 2. Ver resultados (`rama-resultados`)
Muestra el conteo de votos por candidato, el porcentaje que representa 
cada uno sobre el total, y el ganador de la votación.
- **Desarrollado por:** Jairo chiran

### 3. Historial de votaciones (`rama-resultados`)
Guarda un registro con fecha y hora de cada votación en un archivo 
`historial_votacion.json`, permitiendo reiniciar la votación sin perder 
los datos anteriores.
- **Desarrollado por:** Jairo Chiran 

## Candidatos

Los candidatos disponibles para votar en este sistema son:
- Abelardo de la espriella
- Mafe Carrascal
- Gustavo Petro
- Alvaro uribe

## Mejora adicional
Se agregó la funcionalidad de mostrar el **ganador de la votación** 
junto con el conteo final de resultados y las opciones del presidente para la votacion de los que estan postulados.

## Cómo ejecutar el proyecto

1. Clona el repositorio:
```bash
   git clone https://github.com/anasofiags1804/Sistema-votacion.git
   cd Sistema-votacion
```

2. Ejecuta el programa:
```bash
   python sistema.py
```

3. Opciones disponibles al ejecutar:
   - Escribe el **nombre de una persona** para registrar su voto y el candidatos por el que va a votgar 
   - Escribe `resultados` para ver el conteo y el ganador
   - Escribe `reiniciar` para guardar el historial y reiniciar la votación
   - Escribe `salir` para terminar el programa

## Integrantes del equipo
- Ana sofia Gomez — Registro de votos
- Jairo chiran — Resultados e historial

## Tecnologías
- Python 3
- Módulos: `json`, `datetime`