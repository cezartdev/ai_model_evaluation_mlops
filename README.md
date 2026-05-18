# 🤖 AI Model Evaluation & MLOps Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/Package%20Manager-uv-blueviolet.svg?style=for-the-badge&logo=python&logoColor=white" alt="UV Package Manager" />
  <img src="https://img.shields.io/badge/Code%20Style-Ruff-black.svg?style=for-the-badge&logo=python&logoColor=white" alt="Ruff Linter" />
  <img src="https://img.shields.io/badge/ML/DL-AutoGluon-orange.svg?style=for-the-badge&logo=autogluon&logoColor=white" alt="AutoGluon" />
  <img src="https://img.shields.io/badge/Visualization-Plotly-blue.svg?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
</p>

<p align="center">
  <b>A production-grade benchmark and MLOps pipeline designed to evaluate and compare advanced Machine Learning & Deep Learning models across multiple real-world scenarios.</b>
</p>

<p align="center">
  <a href="https://github.com/cezartdev">
    <img src="https://img.shields.io/badge/Developer-cezartdev-181717.svg?style=for-the-badge&logo=github&logoColor=white" alt="Developer: cezartdev" />
  </a>
</p>

<p align="center">
  <a href="#english">English Version</a> • 
  <a href="#español">Versión en Español</a>
</p>

---

<a id="english" name="english"></a>
## English Version

### 📌 Project Overview
This repository is a production-ready **AI Model Evaluation & MLOps Pipeline** designed to benchmark, compare, and deploy a variety of Machine Learning (ML) and Deep Learning (DL) models. The project analyzes and predicts outcomes across three distinct, real-world domains:

1.  **Walmart Sales Forecasting**: High-dimensional, multi-series time-series forecasting.
2.  **Retail Store Inventory**: Tabular inventory optimization and stock predictions.
3.  **S&P 500 Index**: Financial market trend and asset price predictions.

Beyond the comparative modeling, this project serves as a showcase for modern **MLOps** practices, featuring robust environments, automated quality workflows, containerization readiness, and structured execution pipelines for an enterprise-level workflow.

---

### 🚀 Key Features

*   **Comparative Modeling**:
    *   **State-of-the-Art AutoML**: Leveraging [AutoGluon](https://auto.gluon.ai/) to automatically train, tune, and evaluate deep ensembles of top-performing models (e.g., CatBoost, LightGBM, XGBoost, Deep Neural Networks, Weighted Ensembles).
    *   **Multi-Domain Analysis**: Evaluating models across three distinct business problems ranging from tabular regression to time-series forecasting.
*   **Robust MLOps Infrastructure**:
    *   Reproducible environments managed via ultra-fast **`uv`** dependency resolution.
    *   Structured dataset lifecycle split into raw, intermediate, and primary data states.
    *   Containerized environment configurations with Docker & Compose (`compose.yaml`).
*   **Automated Quality & CI/CD**:
    *   Continuous Integration workflow configuration ready for GitHub Actions.
    *   Ultra-fast linting and code formatting using **`ruff`**.
    *   Robust testing suite built with **`pytest`**.
    *   Unified command execution using a clean `Makefile`.

---

### 📂 Project Structure

```bash
.
├── .github/             # CI/CD Workflows (GitHub Actions)
│   └── workflows/
├── data/                # Data storage (raw, intermediate, primary datasets)
│   ├── 01_raw/          # Raw datasets (Walmart Sales, Retail Inventory, S&P 500)
│   ├── 02_intermediate/ # Processed intermediate datasets
│   └── 03_primary/      # Final features & evaluation ready datasets
├── notebooks/           # Jupyter Notebooks for EDA & rapid prototyping
│   ├── 01_walmart_sales.ipynb            # Walmart Sales analysis and modeling
│   ├── 02_retail_store_inventory.ipynb   # Retail store inventory prediction
│   └── 03_sp500.ipynb                    # S&P 500 Index forecasting
├── src/                 # Main source code
│   └── walmart_sales/   # Core packages & pipeline modules
│       ├── assets/      # Assets and artifact tracking
│       ├── resources/   # Resource configurations and schemas
│       └── utils/       # Utility helper functions
├── tests/               # Unit and integration test suite
├── Makefile             # Unified commands for linting, formatting, and testing
├── compose.yaml         # Docker services and pipeline runner definition
├── pyproject.toml       # Python package configuration and dependencies
└── uv.lock              # Reproducible lockfile for dependencies
```

---

### ⚙️ Getting Started

#### 1. Prerequisites
Ensure you have the following installed on your local machine:
*   Python `== 3.12.*`
*   [uv](https://github.com/astral-sh/uv) (Ultra-fast Python package installer and resolver)

#### 2. Environment Setup
Clone this repository and set up the virtual environment:

```bash
# Clone the repository
git clone <your-repository-url>
cd ai_model_evaluation_mlops

# Initialize virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
```

#### 3. Development Commands (`Makefile`)
Keep the codebase clean and tested easily using our defined `Makefile` targets:

*   **Format code**:
    ```bash
    make fmt
    ```
*   **Lint code**:
    ```bash
    make lint
    ```
*   **Run test suite**:
    ```bash
    make test
    ```

---

### 📊 MLOps & CI/CD Workflow
The repository enforces best MLOps practices:
1.  **Code Consistency**: `ruff` is run before committing to guarantee compliance with modern PEP 8 standards.
2.  **Continuous Testing**: Automated execution of all `pytest` suites inside the CI pipeline ensures new model changes do not introduce regression.
3.  **Reproducible Pipelines**: Seamless package locking and fast replication across staging, local, and production environments using `uv.lock`.

---

<br/>

---

<a id="español" name="español"></a>
## Versión en Español

### 📌 Descripción General del Proyecto
Este repositorio es un **Pipeline de MLOps y Evaluación de Modelos de IA** de nivel de producción, diseñado para realizar benchmarks, comparar y desplegar una variedad de modelos de Machine Learning (ML) y Deep Learning (DL). El proyecto analiza y predice resultados en tres dominios del mundo real:

1.  **Predicción de Ventas de Walmart**: Previsión de series temporales de alta dimensión y series múltiples.
2.  **Inventario de Tiendas Minoristas**: Optimización tabular de inventarios y predicciones de stock.
3.  **Índice S&P 500**: Predicciones financieras de tendencias y precios de activos del mercado.

Más allá del modelado comparativo, este proyecto sirve como vitrina para prácticas modernas de **MLOps**, incluyendo entornos totalmente reproducibles, preparación para la contenedorización, flujos de trabajo de calidad automatizados y pipelines estructurados para un flujo de trabajo de nivel empresarial.

---

### 🚀 Características Clave

*   **Modelado Comparativo**:
    *   **AutoML de Vanguardia**: Uso de [AutoGluon](https://auto.gluon.ai/) para entrenar, optimizar y evaluar automáticamente ensamblados profundos de modelos de alto rendimiento (p. ej., CatBoost, LightGBM, XGBoost, Redes Neuronales Profundas, Ensamblados Ponderados).
    *   **Análisis Multidominio**: Evaluación de modelos en tres problemas comerciales diferentes que abarcan desde regresión tabular hasta series temporales.
*   **Infraestructura de MLOps Robustez**:
    *   Gestión de entornos reproducibles mediante el resolutor ultra rápido de dependencias **`uv`**.
    *   Ciclo de vida de datos estructurado y dividido en estados: crudo (`01_raw`), intermedio (`02_intermediate`) y primario (`03_primary`).
    *   Configuraciones de entorno contenedorizadas con Docker y Compose (`compose.yaml`).
*   **CI/CD Automatizado y Calidad de Código**:
    *   Flujo de trabajo de Integración Continua listo para GitHub Actions.
    *   Linting y formateo de código ultra rápidos mediante **`ruff`**.
    *   Suite de pruebas robusta creada con **`pytest`**.
    *   Ejecución unificada de comandos mediante un `Makefile` limpio y legible.

---

### 📂 Estructura del Proyecto

```bash
.
├── .github/             # Flujos de trabajo de CI/CD (GitHub Actions)
│   └── workflows/
├── data/                # Almacenamiento de datos (crudos, procesados, calendarios)
│   ├── 01_raw/          # Datos crudos (Walmart Sales, Retail Inventory, S&P 500)
│   ├── 02_intermediate/ # Datos intermedios procesados
│   └── 03_primary/      # Datos finales listos para modelado y evaluación
├── notebooks/           # Notebooks de Jupyter para EDA y prototipado rápido
│   ├── 01_walmart_sales.ipynb            # Análisis y modelado de Ventas de Walmart
│   ├── 02_retail_store_inventory.ipynb   # Predicción de inventario minorista
│   └── 03_sp500.ipynb                    # Predicción del índice S&P 500
├── src/                 # Código fuente principal
│   └── walmart_sales/   # Paquetes base y módulos del pipeline
│       ├── assets/      # Activos y seguimiento de artefactos
│       ├── resources/   # Configuraciones de recursos y esquemas
│       └── utils/       # Funciones de utilidad y ayuda
├── tests/               # Suite de pruebas unitarias y de integración
├── Makefile             # Comandos unificados para linting, formateo y pruebas
├── compose.yaml         # Servicios de Docker y definición del runner del pipeline
├── pyproject.toml       # Configuración del paquete de Python y dependencias
└── uv.lock              # Archivo de bloqueo reproducible para dependencias
```

---

### ⚙️ Instrucciones de Inicio

#### 1. Requisitos Previos
Asegúrate de tener lo siguiente instalado en tu máquina local:
*   Python `== 3.12.*`
*   [uv](https://github.com/astral-sh/uv) (Instalador y resolutor ultra rápido de paquetes de Python)

#### 2. Configuración del Entorno
Clona este repositorio y configura el entorno virtual:

```bash
# Clonar el repositorio
git clone <url-de-tu-repositorio>
cd ai_model_evaluation_mlops

# Inicializar el entorno virtual e instalar las dependencias
uv venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
uv sync
```

#### 3. Comandos de Desarrollo (`Makefile`)
Mantén la base de código limpia y probada fácilmente utilizando los objetivos definidos en el `Makefile`:

*   **Formatear código**:
    ```bash
    make fmt
    ```
*   **Analizar código (Linting)**:
    ```bash
    make lint
    ```
*   **Ejecutar suite de pruebas**:
    ```bash
    make test
    ```

---

### 📊 Flujo de Trabajo de MLOps y CI/CD
El repositorio implementa las mejores prácticas de MLOps:
1.  **Consistencia del Código**: Se ejecuta `ruff` antes de confirmar cambios (commit) para garantizar el cumplimiento de los estándares modernos PEP 8.
2.  **Pruebas Continuas**: La ejecución automatizada de la suite de `pytest` dentro de la integración continua (CI) asegura que los nuevos cambios del modelo no introduzcan regresiones.
3.  **Pipelines Reproducibles**: Bloqueo y resolución rápida de paquetes a través de `uv.lock` para una replicación exacta en entornos locales, de staging y de producción.
