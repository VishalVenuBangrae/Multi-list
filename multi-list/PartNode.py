class PartNode:

    def __init__(self, pno, pname, nxt, first_supply):
        self.pno = pno
        self.pname = pname
        self.next = nxt
        self.first_supply = first_supply
        self.num_supply = 0

    def get_pno(self):
        return self.pno

    def set_pno(self, pno):
        self.pno = pno

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt

    def get_pname(self):
        return self.pname

    def set_pname(self, pname):
        self.pname = pname

    def get_first_supply(self):
        return self.first_supply

    def set_first_supply(self, first_supply):
        self.first_supply = first_supply

    def get_num_supply(self):
        return self.num_supply

    def set_num_supply(self, num_supply):
        self.num_supply = num_supply

    def __str__(self):
        return f"({self.pno},{self.pname}) Supplied by: "
