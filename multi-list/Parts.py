from PartNode import *
from SupplyNode import *

class Parts:
    def __init__(self):
        self.head = PartNode("", "", None, None)
        self.size = 0

    def find(self, pno):
        pointer = self.head
        while pointer.get_next():
            if pointer.get_next().get_pno() == pno:
                return True, pointer
            pointer = pointer.get_next()
        return False, pointer

    def insert(self, pno, pname):
        found, pointer = self.find(pno)
        if found:
            return False

        new_node = PartNode(pno, pname, None, None)
        if not self.head.get_next():
            self.head.set_next(new_node)
        else:
            current = self.head
            while current.get_next() and new_node.get_pno() > current.get_next().get_pno():
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
        self.size += 1
        return True

    def delete(self, pno):
        found, pointer = self.find(pno)
        if not found:
            return False
        pointer.set_next(pointer.get_next().get_next())
        self.size -= 1
        return True

    def update(self, pno, pname):
        found, pointer = self.find(pno)
        if found:
            pointer.get_next().set_pname(pname)
            return True
        return False

    def __str__(self):
        result = []
        part_pointer = self.head.get_next()
        while part_pointer:
            supplies_info = []
            supply_pointer = part_pointer.get_first_supply()
            while supply_pointer:
                supplies_info.append((supply_pointer.get_sowner().get_sno()[0:], supply_pointer.get_price()))
                supply_pointer = supply_pointer.get_pnext()
            supplies_info.sort()
            supplies_str = " ".join(f"({sno},{price})" for sno, price in supplies_info)
            result.append(f"{part_pointer} {supplies_str}")
            part_pointer = part_pointer.get_next()
        return "\n".join(result)
