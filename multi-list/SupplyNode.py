class SupplyNode:

    def __init__(self, snxt, pnxt, sown, pown, p):
        self.snext = snxt
        self.pnext = pnxt
        self.sowner = sown
        self.powner = pown
        self.price = p

    def get_snext(self):
        return self.snext

    def set_snext(self, snext):
        self.snext = snext

    def get_pnext(self):
        return self.pnext

    def set_pnext(self, pnext):
        self.pnext = pnext

    def get_sowner(self):
        return self.sowner

    def set_sowner(self, sowner):
        self.sowner = sowner

    def get_powner(self):
        return self.powner

    def set_powner(self, powner):
        self.powner = powner

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f"({self.powner},{self.price}) \n"
