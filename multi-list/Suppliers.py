from SupplierNode import *
from SupplyNode import *

class Suppliers:
    def __init__(self):
        self.head = SupplierNode("", "", None, None)
        self.size = 0

    def find(self, sno):
        pointer = self.head
        while pointer.get_next():
            if pointer.get_next().get_sno() == sno:
                return True, pointer
            pointer = pointer.get_next()
        return False, pointer

    def insert(self, sno, sname):
        found, pointer = self.find(sno)
        if found:
            return False

        new_node = SupplierNode(sno, sname, None, None)
        if not self.head.get_next():
            self.head.set_next(new_node)
        else:
            current = self.head
            while current.get_next() and new_node.get_sno() > current.get_next().get_sno():
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
        self.size += 1
        return True

    def delete(self, sno):
        found, pointer = self.find(sno)
        if not found:
            return False
        pointer.set_next(pointer.get_next().get_next())
        self.size -= 1
        return True

    def update(self, sno, sname):
        found, pointer = self.find(sno)
        if found:
            pointer.get_next().set_sname(sname)
            return True
        return False

    def __str__(self):
        result = []
        supplier_pointer = self.head.get_next()
        while supplier_pointer:
            supplies_info = []
            supply_pointer = supplier_pointer.get_first_supply()
            while supply_pointer:
                supplies_info.append((supply_pointer.get_powner().get_pno()[0:], supply_pointer.get_price()))
                supply_pointer = supply_pointer.get_snext()
            supplies_info.sort()
            supplies_str = " ".join(f"({pno},{price})" for pno, price in supplies_info)
            result.append(f"{supplier_pointer} {supplies_str}")
            supplier_pointer = supplier_pointer.get_next()
        return "\n".join(result)
