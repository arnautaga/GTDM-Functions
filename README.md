# GTDM-Functions

## Funciones del módulo de matemáticas
Para usar las funciones del módulo de matemáticas hay que importar: `GTDM-Functions.matematicas.funciones_matematicas`

### Funciones de Cálculo de Ángulos

#### `grad2gradminsec(grados)`
Convierte grados decimales a grados, minutos y segundos.

#### `calc_grad_angle_np(u, v)`
Calcula el ángulo entre dos vectores `u` y `v` utilizando NumPy.

#### `calc_rad_angle_np(u, v)`
Calcula el ángulo en radianes entre dos vectores `u` y `v` utilizando NumPy.

#### `calc_base_ortonormal_np(A, v)`
Calcula la proyección de un vector `v` sobre el espacio nulo de la matriz `A` utilizando NumPy.

#### `calc_grad_angle_sp(u, v)`
Calcula el ángulo entre dos vectores `u` y `v` utilizando SymPy.

#### `calc_rad_angle_sp(u, v)`
Calcula el ángulo en radianes entre dos vectores `u` y `v` utilizando SymPy.

#### `calc_base_ortonormal_sp(A, v)`
Calcula la proyección de un vector `v` sobre el espacio nulo de la matriz `A` utilizando SymPy.

### Funciones de Proyección y Gráficos

#### `proyeccion_caballera(puntos)`
Realiza una proyección caballera de un conjunto de puntos.

#### `caballera(c, color='k')`
Grafica una proyección caballera de un objeto tridimensional.

### Funciones de Transformaciones Geométricas

#### `TH(v)`
Genera una matriz de transformación homogénea para traslación, dado un vector `v`.

#### `traslacion(v, puntos)`
Realiza una traslación de un conjunto de puntos utilizando una matriz de transformación homogénea.

#### `EH(v)`
Genera una matriz diagonal para una transformación de escala, dado un vector `v`.

#### `escala(s, puntos)`
Realiza una escala de un conjunto de puntos utilizando una matriz diagonal.

#### `rot2(angulo)`
Genera una matriz de rotación en 2D dado un ángulo.

#### `rotacion(angulo, eje)`
Genera una matriz de rotación en 3D dado un ángulo y un eje de rotación.

---

**Nota:** Asegúrate de tener las bibliotecas necesarias instaladas antes de ejecutar el script.
