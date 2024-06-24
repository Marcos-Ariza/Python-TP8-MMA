
# Trabajo Práctico No 8 - Fixture Copa América 2024 CSV

## Objetivo
El objetivo de este trabajo práctico es desarrollar una aplicación en Python que permita gestionar el fixture de la Copa América 2024 utilizando archivos. La aplicación debe ser capaz de:
- Cargar los datos de los equipos y los partidos desde un archivo CSV.
- Actualizar los resultados de los partidos.
- Actualizar las posiciones de los equipos en cada grupo.

## Requerimientos

### 1. Lectura de Archivos:
- La aplicación debe leer un archivo CSV llamado `copa-america-2024-UTC.csv` con el fixture de la Copa América 2024. 
- El archivo CSV contendrá la siguiente información:
  ```
  Match Number,Round Number,Date,Location,Home Team,Away Team,Group,Result
  ```
  Ejemplo:
  ```
  1,1,21/06/2024 00:00,Mercedes-Benz Stadium,Argentina,CONCACAF 5,Group A,
  ```

### 2. Estructura de Datos:
- Crear una estructura de datos adecuada para almacenar la información de los equipos, los partidos y los resultados.
- La estructura debe permitir la actualización eficiente de los resultados y el cálculo de las posiciones.

### 3. Actualización de Resultados:
- Implementar una funcionalidad que permita actualizar los resultados de los partidos desde un archivo CSV con el siguiente formato:
  ```
  Match Number,Home Team Goals,Away Team Goals
  ```
  Ejemplo:
  ```
  1,2,1
  ```
- La actualización de los resultados debe reflejarse inmediatamente en las posiciones de los equipos en cada grupo.

### 4. Cálculo de Posiciones:
- Implementar un método para calcular las posiciones de los equipos en cada grupo basándose en los resultados actualizados.
- Las posiciones se determinarán por los siguientes criterios:
  1. Puntos (3 por victoria, 1 por empate, 0 por derrota)
  2. Diferencia de goles
  3. Goles a favor
  4. Resultado entre equipos empatados (en caso de igualdad de puntos, diferencia de goles y goles a favor)

### 5. Salida de Datos:
- Generar un informe final que muestre la tabla de posiciones de cada grupo en formato CSV. El formato del archivo de salida será:
  ```
  Grupo,Equipo,Puntos,PartidosJugados,Victorias,Empates,Derrotas,GolesAFavor,GolesEnContra,DiferenciaDeGoles
  ```

## Consideraciones Adicionales
- Validar que los datos de los archivos CSV sean correctos y manejar posibles errores (como formato incorrecto, datos faltantes, etc.).
- La aplicación debe ser modular, con funciones claramente definidas para cada tarea (lectura de archivos, actualización de resultados, cálculo de posiciones, etc.).
- El código debe seguir buenas prácticas de programación, incluyendo comentarios y documentación adecuada.

## Entrega
- Código fuente de la aplicación en Python en su repositorio y el enlace del repositorio enviado via classroom.
- Archivos CSV de entrada utilizados para las pruebas.
- Archivo CSV con las posiciones finales de los equipos.
- Informe breve explicando el funcionamiento de la aplicación y cómo se implementaron las diferentes funcionalidades.
