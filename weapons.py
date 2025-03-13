from rich.console import Console

console = Console()

class Weapon:
    weapons = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__class__.weapons.append(self)

    def display(self):
        console.print(f'[red]{self.name}[/red] - [green]$[/green]{self.price}')

class Rifle(Weapon):
    rifles = []

    def __init__(self, name, price):
        super().__init__(name, price)
        Rifle.rifles.append(self)

class Pistol(Weapon):
    pistols = []

    def __init__(self, name, price):
        super().__init__(name, price)
        Pistol.pistols.append(self)

class Heavy(Weapon):
    heavies = []

    def __init__(self, name, price):
        super().__init__(name, price)
        Heavy.heavies.append(self)

class SMG(Weapon):
    smgs = []

    def __init__(self, name, price):
        super().__init__(name, price)
        SMG.smgs.append(self)

class Equip(Weapon):
    equips = []

    def __init__(self, name, price):
        super().__init__(name, price)
        Equip.equips.append(self)

class Grenade(Weapon):
    grenades = []

    def __init__(self, name, price):
        super().__init__(name, price)
        Grenade.grenades.append(self)