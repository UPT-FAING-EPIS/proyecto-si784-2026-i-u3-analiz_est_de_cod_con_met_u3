# UPT Code Analyzer - VS Code Extension

Esta extensión oficial permite utilizar el Motor de Análisis Estático de Código de la Universidad Privada de Tacna (UPT) directamente desde tu editor Visual Studio Code.

## Características

- 🔍 **Análisis Estático Instantáneo:** Evalúa tu código fuente con un solo click.
- 📁 **Análisis de Carpetas (Workspace):** Analiza recursivamente todos los archivos válidos dentro de tu proyecto abierto.
- 📊 **Métricas Clave:** Calcula Líneas de Código (LOC) y Complejidad Ciclomática.
- 🛡️ **Code Smells:** Detecta posibles errores de diseño, código muerto y malas prácticas.
- 🚀 **Integración Transparente:** La extensión se comunica con nuestro backend (Clean Architecture) de forma remota, por lo que no consume recursos locales de tu máquina.

## Uso

### Analizar un solo archivo
1. Abre cualquier archivo de código fuente soportado (`.java`, `.py`, `.cs`, `.js`, `.ts`, etc).
2. Abre la Paleta de Comandos (`Ctrl+Shift+P` en Windows/Linux o `Cmd+Shift+P` en macOS).
3. Busca y ejecuta: **"UPT Analyzer: Analizar archivo actual"**.
4. ¡Visualiza los resultados en el panel lateral!

### Analizar una carpeta entera (Workspace)
1. Asegúrate de tener tu proyecto/carpeta abierta en VS Code.
2. Haz clic derecho sobre cualquier carpeta en el **Explorador** de archivos y selecciona **"UPT Analyzer: Analizar Workspace (Carpeta)"** o búscalo directamente en la Paleta de Comandos.
3. ¡Espera los resultados consolidados en el panel lateral!

## Requisitos

- Conexión a internet activa (la extensión se comunica con la API desplegada en Render).

## Equipo de Desarrollo

Proyecto desarrollado para la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna.
- Colque Quispe, Rodrigo Sídney
- Ramos Atahuachi, Fabricio Farid Edmilson
