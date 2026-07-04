# Diagrama de Clases (Clean Architecture)

A continuación se detalla el diagrama de clases del sistema **Analizador Estático de Código con Métricas**, modelado bajo los principios de Clean Architecture. 

```mermaid
classDiagram
    %% Capa de Presentación (Routers / Controllers)
    class AnalysisRouter {
        +submit_code(code: str, user_id: int)
        +get_dashboard(user_id: int)
    }
    class AuthRouter {
        +login(credentials: dict)
        +register(user_data: dict)
    }

    %% Capa de Negocios (Use Cases / Coordinators)
    class AnalysisCoordinator {
        -lexical_analyzer: LexicalAnalyzer
        -syntactic_analyzer: SyntacticAnalyzer
        -ast_builder: ASTBuilder
        -metrics_calc: MetricsCalculator
        -repository: AnalysisRepository
        +execute_full_analysis(code: str): AnalysisResult
        +get_user_history(user_id: int): List~AnalysisResult~
    }
    class SecurityService {
        +hash_password(password: str): str
        +verify_token(token: str): bool
    }

    %% Capa Core (Motor de Análisis)
    class LexicalAnalyzer {
        +tokenize(code: str): List~Token~
    }
    class SyntacticAnalyzer {
        +parse(tokens: List~Token~): bool
        +get_syntax_errors(): List~str~
    }
    class ASTBuilder {
        +build_tree(tokens: List~Token~): ASTNode
    }
    class MetricsCalculator {
        +calculate_complexity(tree: ASTNode): int
        +count_lines_of_code(code: str): int
        +detect_code_smells(tree: ASTNode): List~str~
    }

    %% Entidades de Dominio
    class Token {
        +type: str
        +value: str
        +line: int
    }
    class ASTNode {
        +type: str
        +children: List~ASTNode~
        +value: Any
    }

    %% Capa de Persistencia (Repositories & Models)
    class UserRepository {
        +save(user: User): bool
        +find_by_username(username: str): User
    }
    class AnalysisRepository {
        +save(result: AnalysisResult): bool
        +find_by_user(user_id: int): List~AnalysisResult~
    }
    class User {
        +id: int
        +username: str
        +password_hash: str
    }
    class AnalysisResult {
        +id: int
        +user_id: int
        +code_snippet: str
        +complexity_score: int
        +loc: int
        +code_smells: str
        +timestamp: datetime
    }

    %% Relaciones (Dependencies)
    AnalysisRouter ..> AnalysisCoordinator : Uses
    AuthRouter ..> SecurityService : Uses
    AuthRouter ..> UserRepository : Uses

    AnalysisCoordinator --> LexicalAnalyzer : Composes
    AnalysisCoordinator --> SyntacticAnalyzer : Composes
    AnalysisCoordinator --> ASTBuilder : Composes
    AnalysisCoordinator --> MetricsCalculator : Composes
    AnalysisCoordinator ..> AnalysisRepository : Uses

    LexicalAnalyzer ..> Token : Produces
    SyntacticAnalyzer ..> Token : Consumes
    ASTBuilder ..> Token : Consumes
    ASTBuilder ..> ASTNode : Produces
    MetricsCalculator ..> ASTNode : Consumes

    UserRepository --> User : Manages
    AnalysisRepository --> AnalysisResult : Manages
```
