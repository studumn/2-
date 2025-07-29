class Distance:
    CONVERSION_TO_METERS = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0
    }

    def __init__(self, value, measure):
        if measure not in self.CONVERSION_TO_METERS:
            raise ValueError(f"Invalid measure: {measure}")
        self.value = value
        self.measure = measure

    def __str__(self):
        return f"{self.value} {self.measure}"

    def to_meters(self):
        return self.value * self.CONVERSION_TO_METERS[self.measure]

    def _from_meters(self, meters, target_measure):
        return meters / self.CONVERSION_TO_METERS[target_measure]

    def _operate(self, other, op):
        if not isinstance(other, Distance):
            raise TypeError("Operands must be of type Distance")
        self_m = self.to_meters()
        other_m = other.to_meters()
        result_m = op(self_m, other_m)
        result_value = self._from_meters(result_m, self.measure)
        return Distance(result_value, self.measure)

    def __add__(self, other):
        return self._operate(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self._operate(other, lambda x, y: x - y)
