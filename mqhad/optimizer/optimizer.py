from mqhad.optimizer.optimizer_base import OptimizerBase
from mqhad.optimizer.metal.optimizer import Optimizer as MetalOptimizer
from mqhad.mapper.canvas.canvas_base import CanvasBase
import numpy as np


class Optimizer(OptimizerBase):
    def __init__(
        self,
        design_backend: str = "metal",
        canvas: CanvasBase = None,
        qubit_frequencies: np.ndarray = [],
        config: dict = {},
    ):
        """Optimizer class for metal designs

        Args:
            design_backend (str, optional): Backend for design. Defaults to "metal".
            design (DesignPlanar): Metal design
            qubit_frequencies (np.ndarray, optional): Array of qubit frequencies
            config (dict, optional): Config dict
        """
        self._design_backend = design_backend
        self._design = canvas.get_canvas()
        self._qubit_frequences = qubit_frequencies
        self._config = config

    def optimize(self):
        if self._design_backend == "metal":
            return self._optimize_metal(
                self._design, self._qubit_frequences, self._config
            )

    def _optimize_metal(self, design, qubit_frequencies: np.ndarray, config: dict):
        MetalOptimizer(design, qubit_frequencies, config).optimize()