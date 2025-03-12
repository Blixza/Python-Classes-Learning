from rich.console import Console

console = Console()

class Rifles:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        console.print(f'[red]{self.name}[/red] - [green]$[/green]{self.price}')

rifles = [
    Rifles('AK-47', 1200),
    Rifles('M16', 1500)
]

class Pistols:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        console.print(f'[red]{self.name}[/red] - [green]$[/green]{self.price}')

pistols = [
    Pistols('Desert Eagle', 800),
    Pistols('Glock', 400),
    Pistols('Five-Seven', 600),
    Pistols('Revolver R8', 500)
]

class Heavy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        console.print(f'[red]{self.name}[/red] - [green]$[/green]{self.price}')

heavies = [
    Heavy('Nova', 1200),
    Heavy('XM1014', 2000),
    Heavy('MAG-7', 1800),
    Heavy('Negev', 4000),
    Heavy('M249', 5200)
]

class SMG:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        console.print(f'[red]{self.name}[/red] - [green]$[/green]{self.price}')

smgs = [
    SMG('MP9', 1250),
    SMG('Mac-10', 1050),
    SMG('UMP-45', 1200),
    SMG('PP-Bizon', 1400),
    SMG('P90', 2350),
    SMG('MP7', 1700),
    SMG('MP5-SD', 1500)
]

class Equip:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        console.print(f'[red]{self.name}[/red] - [green]$[/green]{self.price}')

equips = [
    Equip('Kevlar Vest', 650),
    Equip('Helmet', 350),
    Equip('Defuse Kit', 400),
    Equip('Zeus x27', 200)
]

class Grenades:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        console.print(f'[red]{self.name}[/red] - [green]$[/green]{self.price}')

grenades = [
    Grenades('Flashbang', 200),
    Grenades('Smoke Grenade', 300),
    Grenades('HE Grenade', 300),
    Grenades('Molotov/Incendiary', 400),
    Grenades('Decoy Grenade', 50)
]
