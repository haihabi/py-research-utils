import numpy as np
from typing import Dict, List

from pyresearchutils.logger import critical


class MetricLister:
    def __init__(self):
        self.data: Dict[str, List] = dict()

    def add_value(self, **kwargs):
        for k, v in kwargs.items():
            if self.data.get(k) is None:
                self.data.update({k: [v]})
            else:
                self.data[k].append(v)

    def get_array(self, name):
        if self.data.get(name) is None:
            critical(f"Can't find parameter{name}")
        return np.asarray(self.data[name])
