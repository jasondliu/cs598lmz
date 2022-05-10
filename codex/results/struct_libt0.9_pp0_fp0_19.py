import _struct
import _io

from larq_zoo import recovery_pruning

from zquantum.core.interfaces.cost_function import ExpectationValueCostFunction
from zquantum.core.circuit import SingleAnsatzState
from zquantum.core.measurement import create_measurement_object
from zquantum.core.matrix_operator import create_matrix_operator_object
from zquantum.core.circuit.converter import convert_ansatz_to_circuit
from zquantum.core.utils import resolve_parameter_values
import qcengine


def create_evaluator_object(
    ansatz: object,
    depth: int,
    cost_function: object,
    backend: str,
    optimization_objective: object = None,
    measurement: object = None,
    matrix_operator: object = None,
    n_shots: int = 0,
    noise_model: object = None,
    recovery_object: object = None,
    return_error_vectors: bool = False,
):
    """

