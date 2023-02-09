import numpy as np
from mqhad.architecture_generator.chip import ChipInfo


class TestChip:
    def test_load_from_file(self):
        chip = ChipInfo()
        chip.load_from_file("mqhad/tests/test_chip/17q_bus2.chip")
        assert chip.qubit_num == 17
        np.testing.assert_array_equal(
            chip.coupling_list,
            [
                [2, 6],
                [2, 3],
                [6, 7],
                [3, 7],
                [7, 11],
                [11, 15],
                [3, 4],
                [0, 4],
                [7, 8],
                [4, 8],
                [11, 12],
                [8, 12],
                [15, 16],
                [12, 16],
                [0, 1],
                [4, 5],
                [1, 5],
                [8, 9],
                [5, 9],
                [12, 13],
                [9, 13],
                [9, 10],
                [13, 14],
                [10, 14],
            ],
        )

        np.testing.assert_array_equal(
            chip.grid_edge_list,
            [
                [2, 6],
                [2, 3],
                [6, 7],
                [3, 7],
                [7, 11],
                [11, 15],
                [3, 4],
                [0, 4],
                [7, 8],
                [4, 8],
                [11, 12],
                [8, 12],
                [15, 16],
                [12, 16],
                [0, 1],
                [4, 5],
                [1, 5],
                [8, 9],
                [5, 9],
                [12, 13],
                [9, 13],
                [9, 10],
                [13, 14],
                [10, 14],
            ],
        )
        np.testing.assert_array_equal(
            chip.via_edge_list,
            [
                [2, 3, 4],
                [6, 7, 8],
                [3, 4, 5],
                [7, 8, 9],
                [11, 12, 13],
                [8, 9, 10],
                [12, 13, 14],
                [3, 7, 11],
                [7, 11, 15],
                [0, 4, 8],
                [4, 8, 12],
                [8, 12, 16],
                [1, 5, 9],
                [5, 9, 13],
            ],
        )
        np.testing.assert_array_equal(
            chip.edge_list,
            np.array(
                [
                    [4, 1],
                    [0, 5],
                    [6, 3],
                    [2, 7, 4],
                    [3, 0, 8, 5],
                    [4, 1, 9],
                    [2, 7],
                    [6, 3, 11, 8],
                    [7, 4, 12, 9],
                    [8, 5, 13, 10],
                    [9, 14],
                    [7, 15, 12],
                    [11, 8, 16, 13],
                    [12, 9, 14],
                    [13, 10],
                    [11, 16],
                    [15, 12],
                ],
                dtype=object,
            ),
        )
        np.testing.assert_array_equal(
            chip.qubit_grid,
            [
                [-1, 2, 6, -1, -1],
                [-1, 3, 7, 11, 15],
                [0, 4, 8, 12, 16],
                [1, 5, 9, 13, -1],
                [-1, -1, 10, 14, -1],
            ],
        )
        np.testing.assert_array_equal(
            chip.adjacency_matrix,
            [
                [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            ],
        )
        assert chip.cross_bus_list == []

    def test_generatefromAll2QBus(self):
        chip = ChipInfo()
        chip.load_from_file("mqhad/tests/test_chip/17q_bus2.chip")
        chip.generate_from_all_2q_bus()
        np.testing.assert_array_equal(
            chip.adjacency_matrix,
            [
                [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            ],
        )
        np.testing.assert_array_equal(
            chip.coupling_list,
            [
                [2, 6],
                [2, 3],
                [6, 7],
                [3, 7],
                [7, 11],
                [11, 15],
                [3, 4],
                [0, 4],
                [7, 8],
                [4, 8],
                [11, 12],
                [8, 12],
                [15, 16],
                [12, 16],
                [0, 1],
                [4, 5],
                [1, 5],
                [8, 9],
                [5, 9],
                [12, 13],
                [9, 13],
                [9, 10],
                [13, 14],
                [10, 14],
                [2, 6],
                [2, 3],
                [6, 7],
                [3, 7],
                [7, 11],
                [11, 15],
                [3, 4],
                [0, 4],
                [7, 8],
                [4, 8],
                [11, 12],
                [8, 12],
                [15, 16],
                [12, 16],
                [0, 1],
                [4, 5],
                [1, 5],
                [8, 9],
                [5, 9],
                [12, 13],
                [9, 13],
                [9, 10],
                [13, 14],
                [10, 14],
            ],
        )
        np.testing.assert_array_equal(
            chip.grid_edge_list,
            [
                [2, 6],
                [2, 3],
                [6, 7],
                [3, 7],
                [7, 11],
                [11, 15],
                [3, 4],
                [0, 4],
                [7, 8],
                [4, 8],
                [11, 12],
                [8, 12],
                [15, 16],
                [12, 16],
                [0, 1],
                [4, 5],
                [1, 5],
                [8, 9],
                [5, 9],
                [12, 13],
                [9, 13],
                [9, 10],
                [13, 14],
                [10, 14],
                [2, 6],
                [2, 3],
                [6, 7],
                [3, 7],
                [7, 11],
                [11, 15],
                [3, 4],
                [0, 4],
                [7, 8],
                [4, 8],
                [11, 12],
                [8, 12],
                [15, 16],
                [12, 16],
                [0, 1],
                [4, 5],
                [1, 5],
                [8, 9],
                [5, 9],
                [12, 13],
                [9, 13],
                [9, 10],
                [13, 14],
                [10, 14],
            ],
        )
        np.testing.assert_array_equal(
            chip.via_edge_list,
            [
                [2, 3, 4],
                [6, 7, 8],
                [3, 4, 5],
                [7, 8, 9],
                [11, 12, 13],
                [8, 9, 10],
                [12, 13, 14],
                [3, 7, 11],
                [7, 11, 15],
                [0, 4, 8],
                [4, 8, 12],
                [8, 12, 16],
                [1, 5, 9],
                [5, 9, 13],
                [2, 3, 4],
                [6, 7, 8],
                [3, 4, 5],
                [7, 8, 9],
                [11, 12, 13],
                [8, 9, 10],
                [12, 13, 14],
                [3, 7, 11],
                [7, 11, 15],
                [0, 4, 8],
                [4, 8, 12],
                [8, 12, 16],
                [1, 5, 9],
                [5, 9, 13],
            ],
        )
        np.testing.assert_array_equal(
            chip.edge_list,
            [
                [4, 1, 4, 1],
                [0, 5, 0, 5],
                [6, 3, 6, 3],
                [2, 7, 4, 2, 7, 4],
                [3, 0, 8, 5, 3, 0, 8, 5],
                [4, 1, 9, 4, 1, 9],
                [2, 7, 2, 7],
                [6, 3, 11, 8, 6, 3, 11, 8],
                [7, 4, 12, 9, 7, 4, 12, 9],
                [8, 5, 13, 10, 8, 5, 13, 10],
                [9, 14, 9, 14],
                [7, 15, 12, 7, 15, 12],
                [11, 8, 16, 13, 11, 8, 16, 13],
                [12, 9, 14, 12, 9, 14],
                [13, 10, 13, 10],
                [11, 16, 11, 16],
                [15, 12, 15, 12],
            ],
        )

    def test_patch4qbus(self):
        chip = ChipInfo()
        chip.load_from_file("mqhad/tests/test_chip/17q_bus4.chip")
        chip.patch_4q_bus()
        np.testing.assert_array_equal(
            chip.adjacency_matrix,
            [
                [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
            ],
        )
        np.testing.assert_array_equal(
            chip.coupling_list,
            [
                [2, 6],
                [2, 3],
                [6, 7],
                [3, 7],
                [7, 11],
                [11, 15],
                [3, 4],
                [0, 4],
                [7, 8],
                [4, 8],
                [11, 12],
                [8, 12],
                [15, 16],
                [12, 16],
                [0, 1],
                [4, 5],
                [1, 5],
                [8, 9],
                [5, 9],
                [12, 13],
                [9, 13],
                [9, 10],
                [13, 14],
                [10, 14],
                [5, 0],
                [4, 1],
                [8, 3],
                [7, 4],
                [10, 5],
                [11, 6],
                [13, 8],
                [12, 9],
                [16, 11],
                [15, 12],
                [5, 0],
                [4, 1],
                [8, 3],
                [7, 4],
                [10, 5],
                [11, 6],
                [13, 8],
                [12, 9],
                [16, 11],
                [15, 12],
            ],
        )
        np.testing.assert_array_equal(
            chip.edge_list,
            [
                [4, 1, 5, 5],
                [0, 5, 4, 4],
                [6, 3],
                [2, 7, 4, 8, 8],
                [3, 0, 8, 5, 1, 7, 1, 7],
                [4, 1, 9, 0, 10, 0, 10],
                [2, 7, 11, 11],
                [6, 3, 11, 8, 4, 4],
                [7, 4, 12, 9, 3, 13, 3, 13],
                [8, 5, 13, 10, 12, 12],
                [9, 14, 5, 5],
                [7, 15, 12, 6, 16, 6, 16],
                [11, 8, 16, 13, 9, 15, 9, 15],
                [12, 9, 14, 8, 8],
                [13, 10],
                [11, 16, 12, 12],
                [15, 12, 11, 11],
            ],
        )
