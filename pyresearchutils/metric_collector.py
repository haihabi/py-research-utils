class MetricCollector(object):
    def __init__(self):
        self.data_dict = {}

    def insert(self, **kwargs):
        for k, v in kwargs.items():
            self.__setitem__(k, v)

    def clear(self):
        self.data_dict.clear()

    def __getitem__(self, item):
        return self.data_dict.get(item)

    def __setitem__(self, key, val):
        if self.data_dict.get(key) is None:
            self.data_dict.update({key: [val]})
        else:
            self.data_dict[key].append(val)
