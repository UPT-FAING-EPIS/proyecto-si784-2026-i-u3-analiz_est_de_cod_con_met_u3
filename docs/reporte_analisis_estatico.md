## Resultados de Análisis Estático y Seguridad Automatizada

Como parte del aseguramiento de la calidad del software (SQA) y la filosofía DevSecOps, se implementó un pipeline automatizado mediante GitHub Actions. Este pipeline orquesta múltiples herramientas de análisis estático y dinámico, centralizando sus resultados para facilitar la auditoría del código fuente.

### 1. Hub Centralizado de Reportes (GitHub Pages)

Para democratizar el acceso a las métricas del proyecto, se construyó un recolector de artefactos que genera un *Dashboard de Calidad y Pruebas* alojado de forma estática en GitHub Pages.

![Hub Central de Reportes GitHub Pages](../media/hub_reportes_ghpages.png)
*Figura 1: Interfaz del Hub centralizado generado automáticamente tras la ejecución del pipeline principal.*

Este portal provee enlaces directos a los reportes HTML generados por las diferentes herramientas (Coverage, Mutmut, BDD, Playwright, Snyk y Semgrep), permitiendo a cualquier miembro del equipo visualizar el estado de salud del proyecto sin necesidad de acceder a los logs de consola.

### 2. Calidad de Código y Deuda Técnica (SonarCloud)

Se integró **SonarCloud** para realizar un escaneo profundo sobre la mantenibilidad y fiabilidad de la base de código en cada iteración.

![Dashboard de resultados en SonarCloud](../media/sonarcloud_overview.png)
*Figura 2: Panel de control de SonarCloud mostrando el estado actual del repositorio.*

**Hallazgos y Métricas Actuales:**
*   **Cobertura de Pruebas (Coverage):** El proyecto alcanza un **62.2%** de cobertura general, lo que representa un aumento positivo de +135.6% respecto a la medición anterior.
*   **Duplicidad de Código:** Se mantiene en un **6.7%**, habiendo logrado una reducción del 2.9% en los últimos 30 días, lo que denota un esfuerzo en refactorización.
*   **Deuda Técnica (Open Issues):** Se detectaron **87 issues** (code smells y bugs menores) que requieren revisión para mejorar la mantenibilidad a largo plazo.
*   **Seguridad:** Se identificaron **5 incidentes de seguridad** de severidad media (Rating C). A pesar de esto, no se detectaron *Security Hotspots* (Rating A).
*   **Quality Gate:** Actualmente en estado *Failed* debido a las condiciones estrictas del umbral (threshold) configurado por defecto, lo que traza una hoja de ruta clara para las próximas refactorizaciones.

### 3. Análisis de Vulnerabilidades en Dependencias (Snyk)

Para garantizar la seguridad de la cadena de suministro de software (Supply Chain Security), se utilizó **Snyk** con el objetivo de auditar las dependencias declaradas en el proyecto y prevenir el uso de paquetes con vulnerabilidades públicas conocidas (CVEs).

![Reporte de Snyk](../media/snyk_report.png)
*Figura 3: Reporte final de Snyk indicando cero vulnerabilidades.*

**Resultado del Escaneo:**
Snyk examinó la ruta del entorno de integración y certificó **0 vulnerabilidades conocidas** (0 known vulnerabilities) en los árboles de dependencias actuales. Esto garantiza que las librerías base (tanto de Python como del frontend) son versiones seguras y estables.

### 4. Análisis Estático Avanzado y Reglas de Seguridad (Semgrep)

**Semgrep** fue incorporado para realizar un análisis sintáctico enfocado estrictamente en patrones de seguridad y malas prácticas a nivel de código y configuraciones de infraestructura.

![Resultados de Semgrep](../media/semgrep_report.png)
*Figura 4: Tabla de hallazgos detectados por las reglas preconfiguradas de Semgrep.*

**Hallazgos Detectados:**
El reporte arrojó una serie de advertencias (**WARNING**) centradas exclusivamente en los archivos de orquestación de GitHub Actions (`pipeline-principal.yml` y `versionamiento-despliegue.yml`). 
*   **Motivo de la advertencia:** Los flujos de trabajo están utilizando *tags* mutables (ej. `@v3`, `@v4` o ramas como `master`) al importar Actions de terceros. 
*   **Recomendación de Seguridad:** Semgrep advierte que las etiquetas mutables pueden ser alteradas silenciosamente por los propietarios de las actions, habilitando ataques de cadena de suministro (supply-chain attacks). Recomienda "anclar" (pin) las referencias utilizando el hash completo de 40 caracteres (commit SHA) para asegurar la inmutabilidad y mitigar riesgos.
