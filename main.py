from ShippingCalculator import ShippingCalculator;

def readPositiveFloat(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be greater than 0.")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def readShippingType(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["estándar", "standard", "exprés", "expres", "express"]:
            return value
        print("Error: Shipping type must be 'estándar' or 'exprés'.")

if __name__ == "__main__":
    try:
        print("=== Shipping Cost Calculator ===")
        weight = readPositiveFloat("Enter weight (kg): ")
        length = readPositiveFloat("Enter length (m): ")
        width = readPositiveFloat("Enter width (m): ")
        height = readPositiveFloat("Enter height (m): ")
        distance = readPositiveFloat("Enter distance (km): ")
        shippingType = readShippingType("Enter shipping type (standard/expres): ")

        calculator = ShippingCalculator(
            weight=weight,
            length=length,
            width=width,
            height=height,
            distance=distance,
            shippingType=shippingType
        )

        total = calculator.calculateTotalCost()
        print(f"\nTotal shipping cost: ${total:,}")

    except Exception as e:
        print(f"Fatal error: {e}")
