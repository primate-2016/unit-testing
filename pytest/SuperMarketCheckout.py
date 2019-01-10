class Checkout:
    class Discount:
        def __init__(self, nbrItems, discountPrice):
            self.nbrItems = nbrItems
            self.discountPrice = discountPrice

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
    
    def addDiscount(self, item, nbrItems, discountPrice):
        discount = self.Discount(nbrItems, discountPrice) # this creates an instance of the sub-class "Discount" which contains the number of items needed to trigger the discount and the discountedPrice
        self.discounts[item] = discount # now we have a dictionary keyed on the item where the item maps to a instance of the Discount class
    
    def addItemPrice(self, item, price): # i.e. the instance of the class, the item ("banana") and the price ("2)")
        self.prices[item] = price # i.e. add to the dictionary of prices (created in init), the item and its price

    def addItem(self, item): # add item is used to keep a running total of the item prices, adding an apple increases the total by the cost of one apple specified in the prices dictionary
        if item not in self.prices:
            raise Exception("Bad Item") # make sure we have a price for the item being added
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items(): # .items() is dictionary method to return the key and value - the value being the count of items
            # print self.items.items()
            if item in self.discounts: # check to see if the item has a discount associated with it
                discount = self.discounts[item]
                if cnt >= discount.nbrItems:
                    nbrOfDiscounts = cnt/discount.nbrItems
                    total += nbrOfDiscounts * discount.discountPrice
                    remaining = cnt % discount.nbrItems
                    total += remaining * self.prices[item]
                else:
                    total += self.prices[item] * cnt
            else:
                total += self.prices[item] * cnt
        return total
