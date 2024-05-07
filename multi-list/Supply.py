from SupplyNode import *


def find_supply(suppliers, parts, sno, pno):
    supplier_found, sup_pointer = suppliers.find(sno)
    part_found, part_pointer = parts.find(pno)
    if supplier_found and part_found:
        supplier_head = sup_pointer.get_next().get_first_supply()
        while supplier_head:
            if supplier_head.get_sowner().get_sno() == sno and supplier_head.get_powner().get_pno() == pno:
                return True, supplier_head
            supplier_head = supplier_head.get_snext()
    return False, None


def insert_supply(suppliers, parts, sno, pno, price):
    found, _ = find_supply(suppliers, parts, sno, pno)
    if found:
        return False

    supplier_found, sup_pointer = suppliers.find(sno)
    part_found, part_pointer = parts.find(pno)

    if supplier_found and part_found:
        sup_pointer = sup_pointer.get_next()
        part_pointer = part_pointer.get_next()

        new_node = SupplyNode(None, None, sup_pointer, part_pointer, price)

        if not sup_pointer.get_first_supply():
            sup_pointer.set_first_supply(new_node)
        else:
            last = sup_pointer.get_first_supply()
            while last.get_snext():
                last = last.get_snext()
            last.set_snext(new_node)

        if not part_pointer.get_first_supply():
            part_pointer.set_first_supply(new_node)
        else:
            last = part_pointer.get_first_supply()
            while last.get_pnext():
                last = last.get_pnext()
            last.set_pnext(new_node)

        sup_pointer.num_supply += 1
        part_pointer.num_supply += 1

        return True
    return False


def delete_supply(suppliers, parts, sno, pno):
    supplier_found, sup_pointer = suppliers.find(sno)
    part_found, part_pointer = parts.find(pno)

    if not supplier_found or not part_found:
        return False

    # Delete from supplier's list
    previous = None
    current = sup_pointer.get_next().get_first_supply()
    while current:
        if current.get_sowner().get_sno() == sno and current.get_powner().get_pno() == pno:
            if previous:
                previous.set_snext(current.get_snext())
            else:
                sup_pointer.get_next().set_first_supply(current.get_snext())
            break
        previous = current
        current = current.get_snext()

    # Delete from part's list
    previous = None
    current = part_pointer.get_next().get_first_supply()
    while current:
        if current.get_sowner().get_sno() == sno and current.get_powner().get_pno() == pno:
            if previous:
                previous.set_pnext(current.get_pnext())
            else:
                part_pointer.get_next().set_first_supply(current.get_pnext())
            break
        previous = current
        current = current.get_pnext()

    if current:  # If a node was removed
        sup_pointer.get_next().num_supply -= 1
        part_pointer.get_next().num_supply -= 1
        return True
    return False


def update_supply(suppliers, parts, sno, pno, price):
    supplier_found, sup_pointer = suppliers.find(sno)
    if supplier_found:
        supply = sup_pointer.get_next().get_first_supply()
        while supply:
            if supply.get_sowner().get_sno() == sno and supply.get_powner().get_pno() == pno:
                supply.set_price(price)
                return True
            supply = supply.get_snext()
    return False


def print_suppliers_given_part(parts, pno):
    part_found, part_pointer = parts.find(pno)
    if part_found:
        supply = part_pointer.get_next().get_first_supply()
        if not supply:
            print("None")
            return

        suppliers_info = []
        while supply:
            suppliers_info.append((supply.get_sowner().get_sno(), supply.get_sowner().get_sname(), supply.get_price()))
            supply = supply.get_pnext()

        suppliers_info.sort(key=lambda x: x[0][1:])  # Sort based on supplier number
        for info in suppliers_info:
            print(f"({info[0]}, {info[1]}, {info[2]})")
    else:
        print("None")


def print_parts_given_supplier(suppliers, sno):
    supplier_found, sup_pointer = suppliers.find(sno)
    if supplier_found:
        supply = sup_pointer.get_next().get_first_supply()
        if not supply:
            print("None")
            return

        parts_info = []
        while supply:
            parts_info.append((supply.get_powner().get_pno(), supply.get_powner().get_pname(), supply.get_price()))
            supply = supply.get_snext()

        parts_info.sort(key=lambda x: x[0][1:])  # Sort based on part number
        for info in parts_info:
            print(f"({info[0]}, {info[1]}, {info[2]})")
    else:
        print("None")


def print_cheapest_suppliers_given_part(parts, pno):
    part_found, part_pointer = parts.find(pno)
    if part_found:
        supply = part_pointer.get_next().get_first_supply()
        if not supply:
            print("The given pno does not exist.")
            return

        cheapest_price = float('inf')
        suppliers_info = []

        while supply:
            price = int(supply.get_price())
            if price < cheapest_price:
                cheapest_price = price
                suppliers_info = [(supply.get_sowner().get_sno(), supply.get_sowner().get_sname())]
            elif price == cheapest_price:
                suppliers_info.append((supply.get_sowner().get_sno(), supply.get_sowner().get_sname()))
            supply = supply.get_pnext()

        if suppliers_info:
            print("Cheapest Suppliers:")
            suppliers_info.sort(key=lambda x: x[0][1:])  # Sort based on supplier number
            for info in suppliers_info:
                print(f"({info[0]}, {info[1]}, {cheapest_price})")
    else:
        print("The given pno does not exist.")
