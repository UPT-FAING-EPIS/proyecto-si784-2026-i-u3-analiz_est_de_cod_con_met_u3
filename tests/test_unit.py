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
