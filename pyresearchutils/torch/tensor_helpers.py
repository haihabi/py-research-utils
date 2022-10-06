import torch
import numpy as np
from typing import Any


def change2torch(x: Any) -> torch.Tensor:
    """

    Args:
        x:

    Returns:

    """
    if isinstance(x, torch.Tensor):  # If is tensor return
        return x
    if isinstance(x, (float, int)):  # Change float to tensor
        x = [x]
    return torch.Tensor(x)


def torch2numpy(x: torch.Tensor) -> np.ndarray:
    return x.detach().cpu().numpy()
