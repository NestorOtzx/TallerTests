import pytest
from ShippingCalculator import ShippingCalculator

def test_base_rate_included():
    calc = ShippingCalculator(1, 0.1, 0.1, 0.1, 50, "standard")
    cost = calc.calculateTotalCost()
    assert cost >= ShippingCalculator.BASE_RATE

def test_weight_cost_with_surcharge():
    calc = ShippingCalculator(15, 0.1, 0.1, 0.1, 50, "stdard")
    base = 15 * ShippingCalculator.WEIGHT_COST_BY_KILOGRAM
    expected = base + base * ShippingCalculator.HEAVY_WEIGHT_LIMIT_SURCHARGE
    assert calc._calculateWeightCost() == expected

def test_volume_cost_below_limit():
    calc = ShippingCalculator(1, 0.2, 0.2, 0.2, 50, "standa")
    assert calc._calculateVolumeCost() == 0

def test_volume_cost_above_limit():
    calc = ShippingCalculator(1, 1, 1, 0.2, 50, "standa")
    assert calc._calculateVolumeCost() == ShippingCalculator.VOLUME_LIMIT_SURCHARGE

def test_distance_cost_below_limit():
    calc = ShippingCalculator(1, 0.1, 0.1, 0.1, 80, "stad")
    assert calc._calculateDistanceCost() == 0

def test_distance_cost_above_limit():
    calc = ShippingCalculator(1, 0.1, 0.1, 0.1, 150, "standar")
    extra = (150 - ShippingCalculator.DISTANCE_LIMIT) * ShippingCalculator.DISTANCE_RATE
    assert calc._calculateDistanceCost() == extra

def test_express_multiplier_applied():
    calc = ShippingCalculator(1, 0.1, 0.1, 0.1, 50, "express")
    cost_without_multiplier = (
        ShippingCalculator.BASE_RATE
        + calc._calculateWeightCost()
        + calc._calculateVolumeCost()
        + calc._calculateDistanceCost()
    )
    assert calc.calculateTotalCost() == int(cost_without_multiplier * ShippingCalculator.EXPRESS_MULTIPLIER)

def test_standard_shipping_no_multiplier():
    calc = ShippingCalculator(1, 0.1, 0.1, 0.1, 50, "Standar")
    cost_without_multiplier = (
        ShippingCalculator.BASE_RATE
        + calc._calculateWeightCost()
        + calc._calculateVolumeCost()
        + calc._calculateDistanceCost()
    )
    assert calc.calculateTotalCost() == int(cost_without_multiplier)
