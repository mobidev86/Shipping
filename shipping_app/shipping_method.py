from abc import ABC, abstractmethod


#Main Class
class ShippingMethod(ABC):

    @abstractmethod
    def create_waybill(self):
        pass


    @abstractmethod
    def print_waybill_label(self):
        pass

    
    @abstractmethod
    def get_status(self):
        pass
