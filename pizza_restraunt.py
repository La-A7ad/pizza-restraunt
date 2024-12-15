"""
pizza_restaurant.py

Reimplementation of the Pizza Restaurant using ONLY:
1. Factory Method Pattern (for Pizza creation)
2. Strategy Pattern (for Payment)

Toppings are handled in a simpler manner (not using Decorator).
"""

from abc import ABC, abstractmethod

# --------------------------
# Payment Strategy Interface
# --------------------------
class PaymentMethod(ABC):
    """Strategy interface for payment."""
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"\nPaying ${amount:.2f} using PayPal...")
        print("Payment successful via PayPal!\n")

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"\nPaying ${amount:.2f} using Credit Card...")
        print("Payment successful via Credit Card!\n")

# --------------------------
# Pizza Interface (Abstract)
# --------------------------
class Pizza(ABC):
    """Represents a pizza with dynamic toppings."""
    def __init__(self):
        self.toppings = []    # We'll store toppings as strings
        self.base_cost = 0.0  # Set in concrete classes

    @abstractmethod
    def get_base_description(self) -> str:
        pass

    @property
    def description(self) -> str:
        """Build description from base pizza + toppings."""
        desc = self.get_base_description()
        if self.toppings:
            desc += " with " + ", ".join(self.toppings)
        return desc

    @property
    def cost(self) -> float:
        """Calculate total cost = base cost + toppings cost."""
        topping_prices = {
            "Cheese": 1.0,
            "Olives": 0.5,
            "Mushrooms": 0.7
        }
        toppings_cost = sum(topping_prices[t] for t in self.toppings)
        return self.base_cost + toppings_cost

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.base_cost = 5.0

    def get_base_description(self) -> str:
        return "Margherita Pizza"

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.base_cost = 6.0

    def get_base_description(self) -> str:
        return "Pepperoni Pizza"

# --------------------------
# Factory Method
# --------------------------
class PizzaFactory(ABC):
    """Abstract factory to create Pizza objects."""
    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        pass

class SimplePizzaFactory(PizzaFactory):
    """
    A single factory method that creates the requested pizza
    (Margherita or Pepperoni) - an example of the Factory Method pattern.
    """
    def create_pizza(self, pizza_type: str) -> Pizza:
        pizza_type = pizza_type.lower()
        if pizza_type == "margherita":
            return MargheritaPizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")

# --------------------------
# Singleton-like Inventory Manager (Optional)
# (Not strictly from the lecture, but included for completeness)
# --------------------------
class InventoryManager:
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def check_and_decrement(self, item: str) -> bool:
        """Check item availability and decrement if possible."""
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        """Return current inventory status."""
        return self._inventory

# --------------------------
# Main Function
# --------------------------
def main():
    inventory_manager = InventoryManager()
    factory = SimplePizzaFactory()

    print("Welcome to the Pizza Restaurant!")
    
    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")

        choice = input("Enter the number of your choice: ")
        if choice == '0':
            break

        if choice == '1':
            if inventory_manager.check_and_decrement("Margherita"):
                pizza = factory.create_pizza("Margherita")
            else:
                print("Margherita is out of stock!")
                continue
        elif choice == '2':
            if inventory_manager.check_and_decrement("Pepperoni"):
                pizza = factory.create_pizza("Pepperoni")
            else:
                print("Pepperoni is out of stock!")
                continue
        else:
            print("Invalid input. Try again.")
            continue

        # Add toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")

            topping_choice = input("Enter the number of your choice: ")
            if topping_choice == '1':
                # Check inventory for Cheese
                if inventory_manager.check_and_decrement("Cheese"):
                    pizza.toppings.append("Cheese")
                else:
                    print("Cheese out of stock!")
            elif topping_choice == '2':
                # Check inventory for Olives
                if inventory_manager.check_and_decrement("Olives"):
                    pizza.toppings.append("Olives")
                else:
                    print("Olives out of stock!")
            elif topping_choice == '3':
                # Check inventory for Mushrooms
                if inventory_manager.check_and_decrement("Mushrooms"):
                    pizza.toppings.append("Mushrooms")
                else:
                    print("Mushrooms out of stock!")
            elif topping_choice == '4':
                break
            else:
                print("Invalid topping choice!")

        # Display order details
        print("\nYour order:")
        print(f"Description: {pizza.description}")
        print(f"Total cost: ${pizza.cost:.2f}")

        # Payment Strategy
        print("\nChoose Payment Method:")
        print("1. PayPal")
        print("2. Credit Card")
        pm_choice = input("Enter payment method: ")

        if pm_choice == '1':
            payment_method = PayPalPayment()
        elif pm_choice == '2':
            payment_method = CreditCardPayment()
        else:
            print("Invalid choice! Defaulting to PayPal.")
            payment_method = PayPalPayment()

        payment_method.pay(pizza.cost)

        # Show final inventory
        print("Remaining Inventory:", inventory_manager.get_inventory())

if __name__ == "__main__":
    main()

