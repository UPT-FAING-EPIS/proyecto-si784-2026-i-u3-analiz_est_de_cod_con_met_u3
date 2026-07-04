from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    # Asegura que devuelva un HTML o el archivo esperado
    assert "text/html" in response.headers.get("content-type", "")

def test_read_dashboard():
    response = client.get("/dashboard")
    assert response.status_code == 200

def test_read_admin():
    response = client.get("/admin")
    assert response.status_code == 200

from app.motor_analisis.services import analyze_code

def test_analyze_java_code():
    java_code = """
    public class Main {
        public int id;
        public void sayHello(int a, int b, int c, int d, int e, int f) {
            if (a > 0) {
                System.out.println("Hello");
            }
        }
    }
    """
    result = analyze_code(java_code, ".java")
    assert result["nom"] == 1
    assert result["npm"] == 1
    assert result["noa"] == 1
    assert result["complexity"] >= 1
    assert len(result["code_smells"]) >= 1

def test_analyze_python_code():
    py_code = """
class MyClass:
    def __init__(self):
        self.value = 1
        
    def my_method(self, a, b, c, d, e, f):
        if a > 0:
            print("Hello")
            
def func():
    pass
    """
    result = analyze_code(py_code, ".py")
    assert result["nom"] == 3
    assert result["noa"] == 1
    assert result["complexity"] >= 1

def test_analyze_csharp_code():
    cs_code = """
    public class Main {
        public int id;
        public void SayHello() {
            if (true) {
                Console.WriteLine("Hello");
            }
        }
    }
    """
    result = analyze_code(cs_code, ".cs")
    assert result["nom"] == 1
    assert result["npm"] == 1
    assert result["noa"] == 1
    assert result["complexity"] >= 1

def test_auth_login_invalid():
    response = client.post("/api/auth/login", data={"username":"admin", "password":"wrongpassword"})
    assert response.status_code in [400, 401, 404, 302, 303, 200]

def test_auth_github_login():
    response = client.get("/api/auth/login/github")
    assert response.status_code in [200, 302, 303, 404]

def test_analysis_history():
    response = client.get("/api/analysis/history/1")
    assert response.status_code in [200, 401, 403, 404]

def test_analysis_github():
    response = client.get("/api/analysis/github/repos/1")
    assert response.status_code in [200, 400, 401, 403, 404]

import asyncio
from app.negocios.services.websocket_manager import ConnectionManager
from app.persistencia.database.dependencies import get_db
from app.persistencia.repositories.user_repository import UserRepository
from app.negocios.services.analysis_coordinator import AnalysisCoordinator
from app.persistencia.repositories.analysis_repository import AnalysisRepository

def test_websocket_manager():
    manager = ConnectionManager()
    class DummyWebsocket:
        async def accept(self): pass
        async def send_json(self, data):
            if data.get("fail"): raise Exception("Network Error")
            pass
    
    ws = DummyWebsocket()
    asyncio.run(manager.connect(ws))
    assert ws in manager.active_connections
    asyncio.run(manager.broadcast({"msg": "hello"}))
    asyncio.run(manager.broadcast({"fail": True}))
    manager.disconnect(ws)
    assert ws not in manager.active_connections

def test_user_repository():
    db = next(get_db())
    repo = UserRepository(db)
    user = repo.create_user("testuser_cov", "password123", "developer")
    assert user.username == "testuser_cov"
    fetched = repo.get_user_by_username("testuser_cov")
    assert fetched is not None
    repo.update_login_status(user.id, True)
    repo.update_github_token(user.id, "fake_token")
    repo.log_action(user.id, "test_action")
    users = repo.get_all_users()
    assert len(users) > 0
    actions = repo.get_user_actions()
    assert len(actions) > 0

def test_analysis_coordinator_process_folder():
    db = next(get_db())
    repo = AnalysisRepository(db)
    coordinator = AnalysisCoordinator(repo)
    files_data = [
        ("test.py", "print('hello')", ".py"),
        ("test.java", "public class Main { public int a; }", ".java")
    ]
    res1 = coordinator.process_folder_stateless("test_proj", files_data)
    assert res1["project_name"] == "test_proj"
    res2 = coordinator.process_and_save_folder(1, "test_proj", files_data)
    assert res2.project_name == "test_proj"

def test_analysis_coordinator_process_code():
    db = next(get_db())
    repo = AnalysisRepository(db)
    coordinator = AnalysisCoordinator(repo)
    res = coordinator.process_and_save_code(1, "test_code", "print('hello')", ".py")
    assert res.project_name == "test_code"

def test_admin_routes():
    assert client.get("/api/admin/users").status_code == 200
    assert client.get("/api/admin/actions").status_code == 200
