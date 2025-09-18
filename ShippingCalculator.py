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

    def _calculateWeightCost(self):
        cost = self.weight * self.WEIGHT_COST_BY_KILOGRAM
        if self.weight > self.HEAVY_WEIGHT_LIMIT:
            cost += cost * self.HEAVY_WEIGHT_LIMIT_SURCHARGE
        return cost

    def _calculateVolumeCost(self):
        volume = self.length * self.width * self.height
        if volume > self.VOLUME_LIMIT:
            return self.VOLUME_LIMIT_SURCHARGE
        else:
            return 0

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
        if self.shippingType[0] == 'e':
            totalCost *= self.EXPRESS_MULTIPLIER

        return int(totalCost)
