from typing import Any
from ..optimal_geometry_finder_base import OptimalGeometryFinderBase


class OptimalGeometryFinder(OptimalGeometryFinderBase):
    def __init__(self, models: Any = None):
        self._models = models

    def find_optimal_geometry(
        self, target_parameter: str, target_parameter_value: float
    ):
        return self._models[target_parameter].predict([[target_parameter_value]])[0]