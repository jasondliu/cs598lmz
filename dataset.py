import os
import json

import torch
from torch.utils.data import Dataset

class lineDataset(Dataset):
    def __init__(self, tokenizer, file_type='line', block_size=924):
        datafile = os.path.join("data", f"{file_type}.json")
        with open(datafile) as f:
            datas = f.readlines()

        length = len(datas)
        self.inputs = []
        for data in datas:
            data = json.loads(data.strip())
            self.inputs.append(tokenizer.encode(data["input"])[-block_size:])

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, item):
        return torch.tensor(self.inputs[item])
