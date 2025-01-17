import importlib.util
from pathlib import Path
import pytest


def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def spawner():
    file_path = Path(__file__).parent / "../../../../../src/_nebari/stages/kubernetes_services/template/modules/kubernetes/services/jupyterhub/files/jupyterhub/02-spawner.py"
    return module_from_file("spawner", file_path)


def test_get_conda_store_environments(spawner):
    import pdb; pdb.set_trace()

    assert True