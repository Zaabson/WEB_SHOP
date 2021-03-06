from web_shop.models import Product


class Cart:

    def __init__(self, dict=None):
        self.dict = dict or {}

    @classmethod
    def from_form_data(cls, data):
        dictionary = {}
        for d in data:
            dictionary[int(d['product_id'])] = int(d['quantity'])

        return cls(dict=dictionary)

    def for_session(self):
        d = {str(key): value for key, value in self.dict.items()}
        return d

    def for_form(self):
        a = [{'product_id': key, 'quantity': value} for key, value in self.dict.items()]
        return a

    def get_total_price(self):
        total = sum((Product.query.get(int(id)).price * quantity for id, quantity in self.dict.items()))
        return total

    # def keys(self):
    #     return self.dict.keys()
    #
    # def __getitem__(self, item):
    #     return self.dict[item]