from fastapi.testclient import TestClient

from core.main import app

client = TestClient(app)


def test_get_contract_correct_info():
    pass


def test_get_contract_wrong_info():
    pass
