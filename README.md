# 🏪 Walmart Sales Forecasting: ML/DL Benchmark & MLOps Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/Package%20Manager-uv-blueviolet.svg?style=for-the-badge&logo=python&logoColor=white" alt="UV Package Manager" />
  <img src="https://img.shields.io/badge/Code%20Style-Ruff-black.svg?style=for-the-badge&logo=python&logoColor=white" alt="Ruff Linter" />
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-orange.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/DL-GluonTS%20%7C%20PyTorch-red.svg?style=for-the-badge&logo=pytorch&logoColor=white" alt="GluonTS & PyTorch" />
</p>

<p align="center">
  <b>A comprehensive benchmark comparing Machine Learning and Deep Learning models for sales forecasting, packaged with a complete MLOps lifecycle and CI/CD pipelines.</b>
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

<a name="english"></a>
## English Version

### 📌 Project Overview
This repository is a production-ready **Walmart Sales Forecasting Benchmark** designed to evaluate, compare, and deploy a variety of **Machine Learning (ML)** and **Deep Learning (DL)** models on commercial sales datasets. 

Beyond the comparative modeling, this project serves as a showcase for modern **MLOps** practices, featuring robust **CI/CD pipelines**, fully reproducible environments, containerization, and structured pipelines for an enterprise-level workflow.

---

### 🚀 Key Features

*   **Comparative Modeling**:
    *   **Classical Machine Learning**: Utilizing [scikit-learn](https://scikit-learn.org/) to build baseline models (e.g., Random Forests, Gradient Boosting, Linear/Regularized models) to leverage tabular features.
    *   **State-of-the-Art Deep Learning**: Harnessing [GluonTS](https://ts.gluon.ai/) backed by [PyTorch](https://pytorch.org/) to build advanced time-series forecasting models (e.g., DeepAR, Temporal Fusion Transformers (TFT)) capable of capturing complex, multi-series patterns and seasonal sales cycles.
*   **Robust MLOps Infrastructure**:
    *   Reproducible environments managed via ultra-fast **`uv`** dependency resolution.
    *   Automated data preprocessing pipelines aligning raw sales data with commercial and fiscal calendars.
    *   Containerized environment configurations with Docker & Compose (`compose.yaml`).
*   **Automated CI/CD & Code Quality**:
    *   Continuous Integration workflow ready for GitHub Actions.
    *   Ultra-fast linting and code formatting using **`ruff`**.
    *   Robust testing suite built with **`pytest`**.
    *   Unified command execution using a clean `Makefile`.

---

### 📂 Project Structure

```bash
.
├── .github/             # CI/CD Workflows (GitHub Actions)
│   └── workflows/
├── data/                # Data storage (raw, processed, commercial calendars)
├── notebooks/           # Jupyter Notebooks for EDA & rapid prototyping
│   └── 01_eda.ipynb     # Exploratory Data Analysis
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
cd walmart_sales_benchmark

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
3.  **Containerization**: `compose.yaml` handles consistent local runtime matching development and staging environments.

---

<br/>

---

<a name="español"></a>
## Versión en Español

### 📌 Descripción General del Proyecto
Este repositorio es un **Benchmark de Predicción de Ventas de Walmart** de nivel de producción, diseñado para evaluar, comparar y desplegar una variedad de modelos de **Machine Learning (ML)** y **Deep Learning (DL)** sobre conjuntos de datos de ventas comerciales.

Más allá del modelado comparativo, este proyecto sirve como vitrina para prácticas modernas de **MLOps**, incluyendo **pipelines de CI/CD** robustos, entornos totalmente reproducibles, contenedorización y pipelines estructurados para un flujo de trabajo empresarial.

---

### 🚀 Características Clave

*   **Modelado Comparativo**:
    *   **Machine Learning Clásico**: Uso de [scikit-learn](https://scikit-learn.org/) para construir modelos base (p. ej., Random Forests, Gradient Boosting, modelos lineales y regularizados) aprovechando características tabulares.
    *   **Deep Learning de Vanguardia**: Uso de [GluonTS](https://ts.gluon.ai/) respaldado por [PyTorch](https://pytorch.org/) para construir modelos avanzados de predicción de series temporales (p. ej., DeepAR, Temporal Fusion Transformers (TFT)) capaces de capturar patrones complejos, series múltiples y ciclos estacionales de ventas.
*   **Infraestructura de MLOps Robustez**:
    *   Entornos reproducibles gestionados mediante la resolución ultra rápida de dependencias de **`uv`**.
    *   Pipelines automatizados de preprocesamiento de datos que alinean las ventas brutas con calendarios comerciales y fiscales.
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
├── notebooks/           # Notebooks de Jupyter para EDA y prototipado rápido
│   └── 01_eda.ipynb     # Análisis Exploratorio de Datos
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
cd walmart_sales_benchmark

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
3.  **Contenedorización**: `compose.yaml` gestiona entornos de ejecución locales consistentes, que coinciden exactamente con desarrollo y preproducción.
