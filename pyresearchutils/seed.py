import random

import numpy as np


def set_seed(seed: int = 0):
    import torch
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    print(f"Setting Random Seed to {seed}")
