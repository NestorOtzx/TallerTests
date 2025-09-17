class ShippingCalculator:
    BASE_RATE = 5000
    WEIGHT_COST_BY_KILOGRAM = 2000
    HEAVY_WEIGHT_LIMIT = 10
    HEAVY_WEIGHT_LIMIT_SURCHARGE = 0.10
    VOLUME_LIMIT = 0.1
    VOLUME_LIMIT_SURCHARGE = 20000
    DISTANCE_LIMIT = 100
    DISTANCE_RATE = 100
    EXPRESS_MULTIPLIER = 1.5

    def __init__(self, weight, length, width, height, distance, shippingType):
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.distance = distance
        self.shippingType = shippingType.lower()
        self._validateInputs()

    def _validateInputs(self):
        if self.weight <= 0:
            raise ValueError("Weight must be a positive number.")
        if self.length <= 0 or self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        if self.distance <= 0:
            raise ValueError("Distance must be a positive number.")
        if self.shippingType not in ["estándar", "standard", "exprés", "expres", "express"]:
            raise ValueError("Shipping type must be 'estándar' or 'exprés'.")

    def _calculateWeightCost(self):
        cost = self.weight * self.WEIGHT_COST_BY_KILOGRAM
        if self.weight > self.HEAVY_WEIGHT_LIMIT:
            cost += cost * self.HEAVY_WEIGHT_LIMIT_SURCHARGE
        return cost

    def _calculateVolumeCost(self):
        volume = self.length * self.width * self.height
        return self.VOLUME_LIMIT_SURCHARGE if volume > self.VOLUME_LIMIT else 0

    def _calculateDistanceCost(self):
        if self.distance > self.DISTANCE_LIMIT:
            extraDistance = self.distance - self.DISTANCE_LIMIT
            return extraDistance * self.DISTANCE_RATE
        return 0

    def calculateTotalCost(self):
        totalCost = self.BASE_RATE
        totalCost += self._calculateWeightCost()
        totalCost += self._calculateVolumeCost()
        totalCost += self._calculateDistanceCost()

        if self.shippingType in ["exprés", "expres", "express"]:
            totalCost *= self.EXPRESS_MULTIPLIER

        return int(totalCost)
