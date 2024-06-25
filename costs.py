class SacrificeCost:
    def __init__(self, amount: int, adjs: list[str], target_type: list[str]) -> None:
        self.amount = amount
        self.adj = adj
        self.target_type = target_type
        self.paid = False


    def pay(self) -> None:
        for _ in range(self.amount):
            pass # PUT SACRIFICE FUNCTION IN HERE


class TapCost:
    def __init__(self, target: list[str]) -> None:
        self.target = target
        self.paid = False


    def pay(self) -> None:
        pass # PUT FUNCTION TO SELF TAP


class ManaCost:
    def __init__(self, pips: list[str]) -> None:
        self.pips = pips
        self.paid = False


    def pay(self) -> None:
        for item in self.pips:
            pass # PUT FUNCTION TO CHECK MANA IN MANA POOL


class ActivationCost:
    def __init__(self, costs: list) -> None:
        self.costs = costs

    def check(self):
        for item in self.costs:
            item.pay()
            if not item.paid:
                return False
        return True
