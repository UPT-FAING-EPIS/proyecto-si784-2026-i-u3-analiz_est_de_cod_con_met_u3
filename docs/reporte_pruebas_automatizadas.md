## Resultados de Pruebas Automatizadas

El proyecto emplea una estrategia integral de pruebas continuas (Continuous Testing) para asegurar el comportamiento correcto en todas sus capas (pirámide de pruebas). A través del flujo de GitHub Actions se automatizó la ejecución y reportería de los siguientes tipos de pruebas:

### 1. Pruebas Unitarias y de Integración
Se implementaron pruebas enfocadas en validar la lógica core del motor de análisis estático (analizador léxico, sintáctico y constructor AST).
*   **Herramienta:** `pytest` con `pytest-cov`.
*   **Resultados:** Se alcanzó una cobertura global de código (Code Coverage) del **62.2%**.
*   **Reporte:** El pipeline genera dinámicamente un reporte en HTML que permite visualizar qué líneas de código específico del back-end han sido ejecutadas durante las pruebas, asegurando que las reglas de negocio y los coordinadores (`analysis_coordinator.py`) operen sin errores.

### 2. Pruebas de Mutación
Para evaluar la calidad real y la robustez de los casos de prueba unitarios diseñados, se introdujo el testing de mutación.
*   **Herramienta:** `mutmut`.
*   **Resultados:** La herramienta inyecta deliberadamente fallos sintácticos temporales (mutantes) en el código principal (`app/main.py` y el motor de análisis) y verifica si las pruebas unitarias son capaces de detectarlos y fallar. 
*   **Reporte:** Se genera un reporte detallado en `public/mutmut/index.html` listando los mutantes "sobrevivientes" (aquellos que el test suite no detectó), proporcionando métricas estrictas sobre las deficiencias de los tests actuales.

### 3. Pruebas de Comportamiento (BDD - Behavior-Driven Development)
Para alinear los requerimientos del cliente con la implementación de software, se establecieron pruebas legibles para humanos enfocadas en el comportamiento del sistema.
*   **Herramienta:** `pytest-bdd` (junto con la estructura de carpetas `features/` y `step_defs/`).
*   **Resultados:** Se validaron flujos completos como la respuesta del análisis de código o la validación de archivos incorrectos descritos bajo la sintaxis Gherkin (Given-When-Then).
*   **Reporte:** Los resultados de aceptación de características se reflejan en el reporte `public/bdd/index.html`, evidenciando el cumplimiento de las Historias de Usuario clave de manera automatizada.

### 4. Pruebas de Interfaz de Usuario (UI) Automáticas
Se realizaron pruebas de interfaz de usuario de extremo a extremo (E2E) para verificar la correcta interacción visual y funcional en el dashboard principal que consumirá el usuario final.
*   **Herramienta:** `Playwright` para Python.
*   **Resultados:** Scripts definidos en el directorio `tests/ui/` orquestan navegadores headless (Chromium, Firefox, WebKit) simulando clics, llenado de formularios (ingreso del código fuente) y validación de las métricas renderizadas.
*   **Artefactos Generados:** Se configuró Playwright con el parámetro `--video=on`. Esto genera **grabaciones en video (formato webm)** del comportamiento del navegador durante la ejecución de los tests. Estos videos se almacenan automáticamente en el servidor y pueden ser consultados en `public/ui-videos/`, sirviendo como depuración innegable en caso de que alguna prueba frontend falle.

---
**Conclusión de Calidad:**
La combinación de estas cuatro capas asegura que (1) los métodos internos son exactos, (2) las pruebas son sólidas frente a cambios, (3) se cumple con la especificación de negocio y (4) el flujo de trabajo visual del usuario no sufre regresiones.
