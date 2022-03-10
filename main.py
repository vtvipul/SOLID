# this class is doing too many things and a class or method should be responsible for only one thing
# this increases the cohesion in the code.
# this is also 1st priciple of the SOLID principles = single responsibility principle.


# class Order:
#     items = []
#     quantities = []
#     prices = []
#     status = "open"

#     def addItem(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)

#     def totalPrice(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

#     def pay(self, paymentType, securityCode):
#         if paymentType == "debit":
#             print("processing payment debit type...")
#             print(f"verifying security code {securityCode}")
#             self.status = "paid"
#         elif paymentType == "credit":
#             print("processing payment credit type...")
#             print(f"verifying security code {securityCode}")
#             self.status = "paid"
#         else:
#             raise Exception(f"unkown payment type {paymentType}")



# order = Order()
# order.addItem("keyboard", 1, 50)
# order.addItem("ssd", 1, 150)
# order.addItem("usb cable", 2, 5)

# print(order.totalPrice())
# order.pay("debit", "123456")


# Now here there are two classes Order (responsible only for orders) and PaymentProcessor (responsible only for payment processing)
# but now if we have to add more payment options then we will have to change existing PaymentProcessor class
# so instead we can use 2nd SOLID principle i.e open/close principle(open for extension of functionality but closed for
# modification in existing code)


# class Order:
#     items = []
#     quantities = []
#     prices = []
#     status = "open"

#     def addItem(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)

#     def totalPrice(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total



# class PaymentProcessor:
    
#     def payDebit(self, order, securityCode):
#         print("processing payment debit type...")
#         print(f"verifying security code {securityCode}")
#         order.status = "paid"
        
#     def payCredit(self, order, securityCode):
#         print("processing payment debit type...")
#         print(f"verifying security code {securityCode}")
#         order.status = "paid"
        


# order = Order()
# order.addItem("keyboard", 1, 50)
# order.addItem("ssd", 1, 150)
# order.addItem("usb cable", 2, 5)

# paymentProcessor = PaymentProcessor()

# print(order.totalPrice())
# paymentProcessor.payDebit(order, "123456")


# from abc import ABC, abstractmethod


# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order, securityCode):
#         pass



# class Order:
#     items = []
#     quantities = []
#     prices = []
#     status = "open"

#     def addItem(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)

#     def totalPrice(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total


# class DebitPaymentProcessor(PaymentProcessor):
    
#     def pay(self, order, securityCode):
#         print("processing payment debit type...")
#         print(f"verifying security code {securityCode}")
#         order.status = "paid"


# class CreditPaymentProcessor(PaymentProcessor):
    
#     def pay(self, order, securityCode):
#         print("processing payment credit type...")
#         print(f"verifying security code {securityCode}")
#         order.status = "paid"
        

# # so now if I want to add more payment processing options such as paypal we won't have to touch anything 
# # that is already coded instead we can just add a new class to do that 2nd principle of solid principles
# # open/close principle

# class PayPalPaymentProcessor(PaymentProcessor):
    
#     def pay(self, order, securityCode):
#         print("processing payment paypal type...")
#         print(f"verifying security code {securityCode}")
#         order.status = "paid"



# order = Order()
# order.addItem("keyboard", 1, 50)
# order.addItem("ssd", 1, 150)
# order.addItem("usb cable", 2, 5)

# paymentProcessor = DebitPaymentProcessor()

# print(order.totalPrice())
# paymentProcessor.pay(order, "123456")





# # now if paypal payment method takes email address to validate rather than security code then PaypalPaymentProcessor
# # will fail, instead we should we can use __init__ to initialize Processor classes with security code or 
# # email addresses thus making our code compatible with any kind of payment system
# # which is also the 3rd principle of SOLID principles which is Liskov's substitution principle

# # it states that if we have objects/instances in our program then they should be easily replacable by 
# # instances/objects of subclasses or subtypes without altering the functionality of pre-existing code
# # or with altering the correctness of pre-existing code.




# from abc import ABC, abstractmethod


# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order):
#         pass



# class Order:
#     items = []
#     quantities = []
#     prices = []
#     status = "open"

#     def addItem(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)

#     def totalPrice(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total


# class DebitPaymentProcessor(PaymentProcessor):
    
#     def __init__(self, securityCode) -> None:
#         self.securityCode =  securityCode

#     def pay(self, order):
#         print("processing payment debit type...")
#         print(f"verifying security code {self.securityCode}")
#         order.status = "paid"


# class CreditPaymentProcessor(PaymentProcessor):
    
#     def __init__(self, securityCode) -> None:
#         self.securityCode =  securityCode

#     def pay(self, order):
#         print("processing payment credit type...")
#         print(f"verifying security code {self.securityCode}")
#         order.status = "paid"
        

# class PayPalPaymentProcessor(PaymentProcessor):
    
#     def __init__(self, email) -> None:
#         self.email =  email

#     def pay(self, order):
#         print("processing payment paypal type...")
#         print(f"verifying email {self.email}")
#         order.status = "paid"



# order = Order()
# order.addItem("keyboard", 1, 50)
# order.addItem("ssd", 1, 150)
# order.addItem("usb cable", 2, 5)

# paymentProcessor = PayPalPaymentProcessor("some@thing.com")

# # we can do the samething using debit payment option as well without thinking if it needs security code or email to verify

# paymentProcessorDebit = DebitPaymentProcessor("123456")

# print(order.totalPrice())
# paymentProcessor.pay(order)
# paymentProcessorDebit.pay(order)




# # now we want to add sms authorization as a functionality in our payment processing system
# # but our credit payment processor doesn't do sms authorization.
# # so we can create another class called SMSAuth class and that can be responsible for sms authorization
# # and not the payment processor so that payment processor class(abstract class) is not responsible for any authorization
# # related things which is also said by 4th SOLID principle i.e its better to have multiple specific interfaces than one 
# # general purpose interface.



# from abc import ABC, abstractmethod


# class Auth(ABC):

#     @abstractmethod
#     def authorize(self):
#         pass

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order):
#         pass


# class Order:
#     items = []
#     quantities = []
#     prices = []
#     status = "open"

#     def addItem(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)

#     def totalPrice(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total


# class SMSAuth(Auth):

#     def __init__(self, smsCode):
#         self.smsCode = smsCode
#         self.authorized = False

#     def authorize(self):
#         print(f"verifying sms code {self.smsCode}...")
#         self.authorized = True
        

#     def isAuthorized(self):
#         return self.authorized


# class DebitPaymentProcessor(PaymentProcessor):
    
#     def __init__(self, securityCode, smsCode) -> None:
#         self.securityCode =  securityCode
#         self.smsAuth = SMSAuth(smsCode)

#     def pay(self, order):
#         print("processing payment debit type...")
        
#         print(f"verifying security code {self.securityCode}")
        
#         self.smsAuth.authorize()
        
#         if self.smsAuth.isAuthorized():
#             order.status = "paid"
#         else:
#             print("order couldn't be paid as you are not authorized")


# class CreditPaymentProcessor(PaymentProcessor):
    
#     def __init__(self, securityCode) -> None:
#         self.securityCode =  securityCode

#     def pay(self, order):
#         print("processing payment credit type...")
#         print(f"verifying security code {self.securityCode}")
#         order.status = "paid"
        

# class PayPalPaymentProcessor(PaymentProcessor):
    
#     def __init__(self, email, smsCode) -> None:
#         self.email =  email
#         self.smsAuth = SMSAuth(smsCode)

#     def pay(self, order):
#         print("processing payment paypal type...")
        
#         print(f"verifying email {self.email}")
#         self.smsAuth.authorize()
        
#         if self.smsAuth.isAuthorized():
#             order.status = "paid"
#         else:
#             print("order couldn't be paid as you are not authorized")



# order = Order()
# order.addItem("keyboard", 1, 50)
# order.addItem("ssd", 1, 150)
# order.addItem("usb cable", 2, 5)

# paymentProcessor = PayPalPaymentProcessor("some@thing.com", "1234")

# # we can do the samething using debit payment option as well without thinking if it needs security code or email to verify

# paymentProcessorDebit = DebitPaymentProcessor("123456", "1234")

# paymentProcessorCredit = CreditPaymentProcessor("123456")

# print("Total price = ",order.totalPrice())
# print("-"*50)
# paymentProcessor.pay(order)
# print("-"*50)
# paymentProcessorDebit.pay(order)
# print("-"*50)
# paymentProcessorCredit.pay(order)
# print("-"*50)






# now, we want to have a new authorizer which verifies that the user is not a robot
# NotARobotAuth class inherits Auth abstract class
# this can be done with 5th SOLID principle which is dependency inversion principle it states that
# our classes should not depend on the concrete sub/super classes instead it should depend on abstractions




from abc import ABC, abstractmethod



class Auth(ABC):

    @abstractmethod
    def authorize(self):
        pass

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class Order:

    items = []
    quantities = []
    prices = []
    status = "open"

    def addItem(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def totalPrice(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class NotARobotAuth(Auth):
    
    def __init__(self, captcha):
        self.captcha = captcha
        self.authorized = False

    def authorize(self):
        print(f"verifying captcha {self.captcha}...")
        self.authorized = True    

    def isAuthorized(self):
        return self.authorized


class SMSAuth(Auth):

    def __init__(self, smsCode):
        self.smsCode = smsCode
        self.authorized = False

    def authorize(self):
        print(f"verifying sms code {self.smsCode}...")
        self.authorized = True
        
    def isAuthorized(self):
        return self.authorized


class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, securityCode, smsCode) -> None:
        self.securityCode =  securityCode
        self.smsAuth = SMSAuth(smsCode)

    def pay(self, order):
        print("processing payment debit type...")
        
        print(f"verifying security code {self.securityCode}")
        
        self.smsAuth.authorize()
        
        if self.smsAuth.isAuthorized():
            order.status = "paid"
        else:
            print("order couldn't be paid as you are not authorized")


class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, securityCode) -> None:
        self.securityCode =  securityCode

    def pay(self, order):
        print("processing payment credit type...")
        print(f"verifying security code {self.securityCode}")
        order.status = "paid"
        

class PayPalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email, smsCode, captcha) -> None:
        self.email =  email
        self.smsAuth = SMSAuth(smsCode)
        self.notARobot = NotARobotAuth(captcha)

    def pay(self, order):
        print("processing payment paypal type...")
        
        print(f"verifying email {self.email}")
        self.smsAuth.authorize()
        self.notARobot.authorize()

        if self.smsAuth.isAuthorized():
            order.status = "paid"
        else:
            print("order couldn't be paid as you are not authorized")



order = Order()
order.addItem("keyboard", 1, 50)
order.addItem("ssd", 1, 150)
order.addItem("usb cable", 2, 5)

paymentProcessorPayPal = PayPalPaymentProcessor("some@thing.com", "1234", "captcha")

# we can do the samething using debit payment option as well without thinking if it needs security code or email to verify

paymentProcessorDebit = DebitPaymentProcessor("123456", "1234")

paymentProcessorCredit = CreditPaymentProcessor("123456")

print("Total price = ",order.totalPrice())
print("-"*50)
paymentProcessorPayPal.pay(order)
print("-"*50)
paymentProcessorDebit.pay(order)
print("-"*50)
paymentProcessorCredit.pay(order)
print("-"*50)