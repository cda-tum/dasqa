import pytest
import os
import yaml
from src.utils import Utils


class TestUtils:
    def test_check_type_failure(self):
        with pytest.raises(TypeError):
            Utils.check_type("1", int)

    def test_check_type_failure_with_list(self):
        with pytest.raises(TypeError):
            Utils.check_type("1", [int, list])

    def test_check_type_failure_without_raise_error(self):
        result = Utils.check_type("1", int, raise_error=False)
        assert result == False

    def test_check_type_success(self):
        result = Utils.check_type(1, int)
        assert result == True

    # Test for no exception
    def test_load_yaml(self):
        CONFIG_FILE_PATH = os.getcwd() + "/src/tests/test_config/config.yml"
        Utils.load_yaml(CONFIG_FILE_PATH)
