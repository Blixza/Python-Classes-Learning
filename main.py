# Text CS2 buy menu
from weapons import Rifle, Pistol, Heavy, SMG, Grenade, Equip  # import all the weapons
import shop  # import the shop module
from rich.console import Console

console = Console()
shop.initialize()

def display_weapons(weapons):
    for weapon in weapons:
        weapon.display()

def main():
    console.print('[bold]Here is the buy menu:[/bold]')
    console.print('\n:ewe:Rifles:')
    display_weapons(Rifle.rifles)
    console.print('\n:pistol:Pistols:')
    display_weapons(Pistol.pistols)
    console.print('\n:otter:Heavy:')
    display_weapons(Heavy.heavies)
    console.print('\n:ox:SMG:')
    display_weapons(SMG.smgs)
    console.print('\n:cat:Grenades:')
    display_weapons(Grenade.grenades)
    console.print('\n:crab:Equipment:')
    display_weapons(Equip.equips)

if __name__ == '__main__':
    main()