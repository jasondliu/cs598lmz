import select
from typing import Iterable, List, Tuple, Union
from sklearn.metrics import f1_score


def evaluate_torch(
        data,  # pylint: disable=R0913
        model: nn.Module,
        tokenizer,
        labels,
        batch_size: int,
        eval_examples: Iterable[InputExample],  # pylint: disable=W0622
        eval_features: Iterable[InputFeatures],
        device: torch.device,
        label_list: List[str],
        output_mode: Union[str, Callable[[List[int]], List[int]]] = None,
        silent=False,
        is_task2=False,
        n_gpu: int = 1,
        fp16: bool = False,
        local_rank=-1,
        args=None
        ):
    # only needs to compute the last sentence_classication layer
    # print("model name: ", model.config.name)
    model.bert.encoder.output_hidden_states = True
    # for layer
