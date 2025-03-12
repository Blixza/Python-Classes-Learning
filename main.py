# Text CS2 buy menu
from weapons import * # import all the weapons
from rich.console import Console

console = Console()

def main():
    console.print('[bold]Here is the buy menu:[/bold]')
    print('\nRifles:')
    for rifle in rifles:
        rifle.display()
    print('\nPistols:')
    for pistol in pistols:
        pistol.display()
    print('\nHeavy:')
    for heavy in heavies:
        heavy.display()
    print('\nSMG:')
    for smg in smgs:
        smg.display()
    print('\nEquipment:')
    for equip in equips:
        equip.display()

main()