class MenuItem:
    def __init__ (self, itemId, name, description, price, category):
        self.itemId = itemId
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.isAvailable = True
    
    def getItemInfo(self):
        return f"{self.itemId} {self.name} {self.price} {self.category} {self.isAvailable}"

class OrderItem:
    def __init__ (self, menuItem, quantity, specialInstructions):
        self.menuItem = menuItem
        self.quantity = quantity
        self.specialInstructions = specialInstructions
    
    def getSubtotal(self):
        return self.quantity * self.menuItem.price
    
    def getOrderItemDetails(self):
        return f"{self.menuItem.getItemInfo()} {self.quantity} {self.specialInstructions}"
    
class Order:
    def __init__ (self, orderId, tableNumber, orderItems, orderTime, status):
        self.orderId = orderId
        self.tableNumber = tableNumber
        self.orderItems = []
        self.orderTime = orderTime
        self.status = status

    def addItem(self, menuItem, quantity, instructions):
        orderItem = OrderItem(menuItem, quantity, instructions)
        self.orderItems.append(orderItem)

    def removeItem(self, itemId):
        for orderItem in self.orderItems:
            if orderItem.menuItem.itemId == itemId:
                self.orderItems.remove(orderItem)
                return
        print("Айди не найден")
    def getSubtotal(self):
        sum = 0
        for orderItem in self.orderItems:
            sum += orderItem.getSubtotal()
        return sum
    def getTax(self):
        
        return self.getSubtotal() * 0.08
        
    
burger = MenuItem("M001", "Classic Burger",
    "Beef patty with lettuce, tomato, cheese", 12.99, "Main Course")
fries = MenuItem("M002", "French Fries",
    "Crispy golden fries", 4.99, "Appetizer")
salad = MenuItem("M003", "Caesar Salad",
    "Fresh romaine with caesar dressing", 8.99, "Appetizer")
soda = MenuItem("M004", "Soft Drink",
    "Coca-Cola, Sprite, or Fanta", 2.99, "Beverage")
cake = MenuItem("M005", "Chocolate Cake",
    "Rich chocolate layer cake", 6.99, "Dessert")
    
print(burger.getItemInfo())

cakeO = OrderItem(burger, 10, "blabla")

print(cakeO.getSubtotal())
print(cakeO.getOrderItemDetails())
