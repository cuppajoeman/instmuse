from typing import Tuple, Set, List
from .stringed_instrument import ModularGridNoteCollection
import re

def convert_modular_grid_shorthand_to_modular_grid_positions(shorthand_text: str) -> Set[Tuple[int, int]]:
    """Takes in a string of the form 'X1 X2 ... XN' and turns it into a list of x y coordinates"""
    return {(i, int(ele)) for i, ele in enumerate(shorthand_text.split()) if ele != "X"}

def generate_MGNCs_from_MG_shorthand(mg_shorthand: str) -> List[ModularGridNoteCollection]:
    """An example of mg_shorthand could be

            "(X 5 X 5 5 5) (X X 5 7 6 7) (X 3 5 4 5 X)"

    """
    MGNCs = []
    matches = re.findall(
        '\[[^\]]*\]|\([^\)]*\)|"[^"]*"|\<[^\>]*\>|\S+', mg_shorthand
    )
    for match in matches:
        # slicing to remove the parenthesis
        MGNCs.append(ModularGridNoteCollection(convert_modular_grid_shorthand_to_modular_grid_positions(match[1: -1])))
    return MGNCs



    

