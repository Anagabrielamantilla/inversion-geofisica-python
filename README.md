<div align="center">

# Curso teórico práctico sobre inversión geofísica en Python

### Del dato observado al modelo del subsuelo

**Gravimetría · Magnetometría · MT 1D · FWI · SimPEG · Aprendizaje profundo guiado por física**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![SimPEG](https://img.shields.io/badge/SimPEG-Geophysics-23395B)](https://simpeg.xyz/)
[![Course](https://img.shields.io/badge/curso-teórico--práctico-19A7CE)](#ruta-científica)
[![YouTube](https://img.shields.io/badge/ver-clases_en_YouTube-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=gAqL1yqmJJw&list=PLBrkSquHNyNM)

</div>

<p align="center"><em>Un laboratorio reproducible para explorar la relación</em></p>

$$
\mathbf{d} = \mathcal{F}(\mathbf{m}) + \boldsymbol{\varepsilon}
$$

<p align="center"><em>y reconstruir modelos físicos con ajuste de datos, regularización y aprendizaje profundo.</em></p>

![Mapa visual del curso](docs/assets/course-map.png)

## Qué encontrarás

Este repositorio reúne los materiales del **Curso teórico práctico sobre inversión geofísica en Python**, dirigido a la comunidad científica. Integra fundamentos del problema inverso con ejercicios guiados, casos sintéticos y datos reales.

El curso fue dirigido por **Ana Mantilla, Javier Torres y León Suárez**, con **PhD Henry Arguello Fuentes** como investigador principal. Fue organizado por los grupos de investigación **HDSP, GIGBA y CPS** en el marco del **Contrato No. 045-2025** financiado por el Ministerio de Ciencia, Tecnología e Innovación (MINCIENCIAS) y la **Agencia Nacional de Hidrocarburos (ANH)**.

## Ruta científica

| Sesión | Eje | Del dato al modelo | Material |
|:--:|---|---|---|
| 01 | Fundamentos | No unicidad, sensibilidad, incertidumbre y regularización | [Abrir](materials/session-01/) |
| 02 | Gravimetría 3D | Anomalía residual → contraste de densidad | [Abrir](materials/session-02/) |
| 03 | Magnetometría 3D | Anomalía TMI → susceptibilidad magnética | [Abrir](materials/session-03/) |
| 04 | MT 1D guiada por física | Impedancia Z<sub>xy</sub> → resistividad por capas | [Abrir](materials/session-04/) |
| 05 | FWI: fundamentos | Registros sísmicos → modelo de velocidad | [Abrir](materials/session-05/) |
| 06 | FWI: entrenamiento | *Shots* y pesos preentrenados → velocidad de onda P | [Abrir](materials/session-06/) |
| 07 | Reto integrador MT 1D | Datos sintéticos → inversión profunda no supervisada | [Abrir](materials/session-07/) |

## Arquitectura conceptual

```mermaid
%%{init: {"theme":"base","themeVariables":{"fontFamily":"Arial, sans-serif","fontSize":"22px","lineColor":"#38d9ff","primaryTextColor":"#ffffff"},"flowchart":{"htmlLabels":true,"curve":"basis","nodeSpacing":50,"rankSpacing":65}}}%%
flowchart TB
    subgraph ENTRADAS["① OBSERVAR Y CONSTRUIR LA HIPÓTESIS"]
        direction LR
        D["📡 <b>DATOS OBSERVADOS</b><br/>geometría · unidades · ruido<br/>incertidumbre de medición"]
        M["🧩 <b>MODELO INICIAL</b><br/>malla o capas · propiedades físicas<br/>límites y conocimiento previo"]
    end

    subgraph FISICA["② TRADUCIR EL MODELO A UNA RESPUESTA FÍSICA"]
        direction LR
        F["⚙️ <b>OPERADOR DIRECTO F(m)</b><br/>ecuaciones físicas · discretización<br/>respuesta geofísica predicha"]
        S["🔬 <b>SENSIBILIDAD</b><br/>¿qué parámetros controla cada dato?<br/>Jacobiano o gradiente automático"]
        F --> S
    end

    subgraph NUCLEO["③ MEDIR LA DISCREPANCIA Y RESTRINGIR LA SOLUCIÓN"]
        direction LR
        MIS["🎯 <b>AJUSTE A LOS DATOS</b><br/>‖Wd [F(m) − dobs]‖²<br/>residuales ponderados"]
        REG["🧭 <b>REGULARIZACIÓN R(m)</b><br/>suavidad · estructura · referencia<br/>principios físicos y geológicos"]
        OBJ["✨ <b>FUNCIÓN OBJETIVO</b><br/>Φ(m) = misfit + β R(m)<br/>balance evidencia ↔ estabilidad"]
        MIS --> OBJ
        REG --> OBJ
    end

    subgraph SOLUCION["④ APRENDER, VALIDAR E INTERPRETAR"]
        direction LR
        OPT["🚀 <b>OPTIMIZACIÓN</b><br/>SimPEG · MLP · CNN<br/>actualización iterativa del modelo"]
        VAL{"✅ <b>¿CONVERGE Y<br/>EXPLICA LOS DATOS?</b>"}
        POST["🌍 <b>MODELO ESTIMADO m*</b><br/>resolución · incertidumbre<br/>coherencia e interpretación geológica"]
        OPT --> VAL
        VAL -- "sí" --> POST
    end

    D --> F
    M --> F
    F --> MIS
    S --> OPT
    OBJ --> OPT
    VAL -. "no: revisar β, modelo, datos o física" .-> M
    POST -. "nueva evidencia / nueva hipótesis" .-> D

    G["🟣 <b>GRAVIMETRÍA 3D</b><br/>densidad"]
    MAG["🔵 <b>MAGNETOMETRÍA 3D</b><br/>susceptibilidad"]
    MT["🟢 <b>MT 1D</b><br/>resistividad por capas"]
    W["🟠 <b>FWI + DEEP LEARNING</b><br/>velocidad de onda P"]
    POST --> G
    POST --> MAG
    POST --> MT
    POST --> W

    classDef data fill:#073b66,stroke:#38d9ff,stroke-width:4px,color:#fff;
    classDef model fill:#32186f,stroke:#b794ff,stroke-width:4px,color:#fff;
    classDef physics fill:#102a56,stroke:#56e0ff,stroke-width:4px,color:#fff;
    classDef objective fill:#142a86,stroke:#ffda57,stroke-width:5px,color:#fff;
    classDef action fill:#123f65,stroke:#38d9ff,stroke-width:4px,color:#fff;
    classDef decision fill:#5b245f,stroke:#ff8bd8,stroke-width:5px,color:#fff;
    classDef result fill:#805019,stroke:#ffd05b,stroke-width:4px,color:#fff;
    classDef method fill:#0b1747,stroke:#8fe9ff,stroke-width:3px,color:#fff;

    class D data;
    class M,REG model;
    class F,S,MIS physics;
    class OBJ objective;
    class OPT action;
    class VAL decision;
    class POST result;
    class G,MAG,MT,W method;
```

La inversión se plantea como un **ciclo iterativo y auditable**: los datos observados y la hipótesis física alimentan el operador directo; la discrepancia entre datos predichos y observados se combina con regularización y conocimiento previo; el modelo se actualiza hasta alcanzar convergencia, y finalmente se evalúan resolución, incertidumbre y coherencia geológica.

## Clases grabadas

<div align="center">

### ▶️ [Ver la lista de reproducción completa en YouTube](https://www.youtube.com/watch?v=gAqL1yqmJJw&list=PLBrkSquHNyNM)

[![Vista previa de las clases del curso](https://img.youtube.com/vi/zWDQ6DE8mWs/maxresdefault.jpg)](https://www.youtube.com/watch?v=zWDQ6DE8mWs&list=PLBrkSquHNyNM&index=4&t=112s)

**[▶ Reproducir este video desde el minuto 1:52](https://www.youtube.com/watch?v=zWDQ6DE8mWs&list=PLBrkSquHNyNM&index=4&t=112s)**

*Revisa las sesiones en orden y utiliza los notebooks de este repositorio como laboratorio práctico.*

</div>

## Inicio rápido

```bash
git clone https://github.com/Anagabrielamantilla/inversion-geofisica-python.git
cd inversion-geofisica-python
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Abre los notebooks desde su propia carpeta de sesión para conservar las rutas relativas a los datos. Varios cuadernos fueron diseñados para **Google Colab**; las celdas de montaje de Drive y las rutas `/content/...` deben ajustarse si se ejecutan localmente. Las tareas de FWI pueden requerir GPU y conjuntos externos indicados dentro de cada notebook.

## Estructura

```text
.
├── docs/
│   ├── brochure.pdf          # pieza publicitaria y programa original
│   └── assets/               # publicidad e infografía conceptual
├── materials/
│   ├── session-01/           # introducción y regresión lineal
│   ├── session-02/           # inversión gravimétrica
│   ├── session-03/           # inversión magnetométrica
│   ├── session-04/           # inversión MT 1D
│   ├── session-05/           # introducción a FWI
│   ├── session-06/           # FWI y modelos preentrenados
│   └── session-07/           # reto de inversión MT 1D
├── CITATION.cff
└── requirements.txt
```

## Programa anunciado

La pieza publicitaria presenta una intensidad total de **18 horas**:

- **Bloque 1 — Introducción al problema inverso (3 h):** datos, modelos, incertidumbre, problema directo, no unicidad, ruido, sensibilidad, ajuste y regularización.
- **Bloque 2 — Inversión gravimétrica con SimPEG (3 h):** malla 3D, celdas activas, modelos sintéticos, datos reales y visualización en ParaView.
- **Bloque 3 — Inversión magnetométrica con SimPEG (3 h):** TMI, campo inductor, susceptibilidad, casos sintéticos y reales.
- **Bloque 4 — Inversión profunda guiada por física para MT 1D (3 h):** operador directo diferenciable, MLP con *skip connections* y entrenamiento no supervisado.
- **Bloques 5 y 6 — Inversión de onda completa (6 h):** adquisición, ecuación de onda acústica, aprendizaje supervisado, hiperparámetros y pesos preentrenados.

Consulta el [folleto original](docs/brochure.pdf) para preservar la información institucional y el programa completo.

> **Nota histórica.** La publicidad anuncia el curso del **3 al 11 de agosto**, de **1:00 p. m. a 3:00 p. m.**, en el salón 404 del edificio E3T, con modalidad virtual complementaria. Los enlaces de asistencia e inscripción del evento se consideran históricos y no se reproducen como llamadas activas.

## Datos, reproducibilidad y alcance

- Los conjuntos `.npy`, `.txt` y `.edi` disponibles en la carpeta fuente se mantienen junto a su sesión.
- Algunos notebooks hacen referencia a recursos externos o a nombres de archivos que no forman parte del paquete original; revisa sus celdas de preparación antes de ejecutar.
- Los resultados numéricos pueden variar por versión de biblioteca, *hardware*, semilla y tolerancias del optimizador.
- `requirements.txt` documenta el conjunto común de bibliotecas; cada notebook sigue siendo la referencia para requisitos específicos.

## Crédito institucional

Material asociado al proyecto **“Nuevas tecnologías computacionales para el procesamiento e inversión conjunta de gravimetría, magnetometría y magnetotelúrica mediante aprendizaje profundo guiado por principios físicos para la caracterización multicriterio”**.

Organizan: **HDSP · GIGBA · CPS**, con participación institucional de la **Universidad Industrial de Santander**, la **Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones**, la **Facultad de Ciencias** y la **Agencia Nacional de Hidrocarburos**.

## Uso y atribución

Este repositorio conserva material docente y datos del curso. **No se declara una licencia abierta**: todos los derechos permanecen con sus titulares. Antes de reutilizar, modificar o redistribuir contenido, confirma los permisos aplicables y cita a las personas e instituciones responsables mediante [`CITATION.cff`](CITATION.cff).

---

<div align="center">

**Explora · modela · invierte · valida**

</div>
