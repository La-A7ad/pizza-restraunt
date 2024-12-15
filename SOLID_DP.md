# SOLID_DP.md

## Overview
In our Pizza Restaurant system, we applied specific design patterns that naturally align with several SOLID principles. Below is an explanation of how each principle is addressed:

---

## 1. Single Responsibility Principle (SRP)

- **Pizza Classes** (`MargheritaPizza`, `PepperoniPizza`): Each pizza class only handles the base properties, description, and cost. Toppings are just appended to a list; no extra logic is lumped in.
- **Factory Class** (`SimplePizzaFactory`): Responsible solely for creating the correct pizza type. It doesn’t handle payments or user interaction.
- **Payment Classes** (`PayPalPayment`, `CreditCardPayment`): Each handles only one thing—payment processing.

Because of these small, focused classes, the codebase remains modular and easy to maintain.

---

## 2. Open-Closed Principle (OCP)

- **Factory Method**: We can add new pizza types (e.g., `BBQPizza`) by creating a new class and updating our factory method minimally, without altering existing pizza classes.
- **Strategy Interface**: Payment strategies can be extended by creating new classes implementing the `PaymentMethod` interface (e.g., `CryptoPayment`) without modifying existing logic.

This means the system is open for extension (add new pizzas/payment methods) but closed for modification (no need to rewrite existing core classes).

---

## 3. Liskov Substitution Principle (LSP)

- **Pizza** classes all inherit from the same abstract `Pizza` interface. Anywhere a `Pizza` is expected, `MargheritaPizza` or `PepperoniPizza` can be substituted seamlessly.
- **PaymentMethod** interface ensures any concrete payment class can substitute another, fulfilling the same `pay(amount)` contract.

This upholds LSP by allowing objects of different subclasses to be used interchangeably.

---

## 4. Interface Segregation Principle (ISP)

- **PaymentMethod** only has one method, `pay()`, which is the sole responsibility of the payment strategy. There are no extraneous methods forced upon implementing classes.
- **Pizza** interface consists only of the essential methods/attributes (`get_base_description()`, `description`, `cost`)—no unrelated behaviors.

The system avoids “fat interfaces” and ensures each interface is minimal and focused.

---

## 5. Dependency Inversion Principle (DIP)

- High-level modules (like the main ordering logic) depend on **abstract** interfaces (`Pizza`, `PaymentMethod`) rather than concrete implementations. 
- The factory object returns an abstract `Pizza` type, and the main code doesn’t need to know which specific pizza class is created.

This keeps the design flexible and testable. If we want to replace or modify how pizzas are created or how payments are processed, we only need to swap in new implementations of the same interfaces without changing the core logic.

---

## Conclusion
By using the **Factory Method** and **Strategy** patterns with clearly defined interfaces, our Pizza Restaurant system adheres to SOLID principles. Each principle helps make our code easier to maintain, extend, and reason about.

