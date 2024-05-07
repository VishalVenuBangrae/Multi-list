class SupplierNode:

    def __init__(self, sno, sname, next, supply):
        self.sno = sno
        self.sname = sname
        self.next = next
        self.first_supply = supply
        self.num_supply = 0

    def get_sno(self):
        return self.sno

    def set_sno(self, sno):
        self.sno = sno

    def get_sname(self):
        return self.sname

    def set_sname(self, sname):
        self.sname = sname

    def set_next(self, snext):
        self.next = snext

    def get_next(self):
        return self.next

    def get_first_supply(self):
        return self.first_supply

    def set_first_supply(self, first_supply):
        self.first_supply = first_supply

    def get_num_supply(self):
        return self.num_supply

    def set_num_supply(self, num_supply):
        self.num_supply = num_supply

    def __str__(self):
        result = f"({self.sno},{self.sname}), Supplies: "
        return result


