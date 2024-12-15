# DesignPatterns.md

## Overview
The Pizza Restaurant application demonstrates two primary design patterns:
1. **Factory Method** for pizza creation.
2. **Strategy** for payment processing.

Additionally, we illustrate how overengineering might occur if we apply patterns excessively or where they’re not needed.

---

## 1. Factory Method Pattern

### Intent
Centralize and encapsulate the creation of pizza objects (Margherita, Pepperoni, etc.) so the main codebase doesn’t depend on concrete classes.

### How It’s Applied
- **Factory Class (`SimplePizzaFactory`)**: Has one method `create_pizza(pizza_type: str)` that returns a concrete pizza object.  
- **Concrete Pizza Classes** (`MargheritaPizza`, `PepperoniPizza`): Each defines base cost and description.

### Benefits
- **Encapsulated Object Creation**: The main code delegates all pizza instantiation logic to a single factory method.
- **Open-Closed Principle**: Adding new pizza types doesn’t break existing code.

---

## 2. Strategy Pattern

### Intent
Define a family of algorithms (payment methods) and make them interchangeable. Each payment strategy implements a common interface for a single operation.

### How It’s Applied
- **PaymentMethod Interface**: Declares a `pay(amount)` method.
- **PayPalPayment**, **CreditCardPayment**: Implement the interface with distinct payment logic.

### Benefits
- **Encapsulation**: Each payment method is wrapped in its own class.
- **Extensibility**: We can add or remove payment methods without altering other parts of the code.

---

## Overengineering Example

### Scenario
If we decided to create a complex Abstract Factory for two pizza types or a full-blown Decorator pattern just for a few simple toppings, that might be overkill.

#### Example Snippet
```python
class AbstractPizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self):
        pass

class MargheritaFactory(AbstractPizzaFactory):
    def create_pizza(self):
        return MargheritaPizza()

class PepperoniFactory(AbstractPizzaFactory):
    def create_pizza(self):
        return PepperoniPizza()

