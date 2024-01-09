""" Put where UniteDescriptor.ndf located and run 
    For 9 jan 2024 UniteDescriptor.ndf location is:
    <mod_name>/GameData/Generated/Gameplay/Gfx/Ammunition.ndf
"""

from tqdm import tqdm  # type: ignore


def change_all_ammo_description(
    PorteeMaximaleMultiplier: int = 10,
) -> str:
    new_buffer: str = ""
    with open("Ammunition.ndf", "r+", encoding="utf-8") as f:
        for line in tqdm(f.readlines()):
            # Distance Of Shoting
            if "PorteeMaximale                    =" in line:
                extracted_digits = "".join(filter(str.isdigit, line))
                default_number = int(extracted_digits)
                new_buffer += f"    PorteeMaximale                    = (({default_number*PorteeMaximaleMultiplier}) * Metre)\n"
                continue
            new_buffer += line
    return new_buffer


def write_buffer(path: str, new_buffer: str) -> None:
    with open(path, "w+", encoding="utf-8") as f:
        f.write(new_buffer)


def main():
    new_buffer = change_all_ammo_description()
    write_buffer(path="Ammunition.ndf", new_buffer=new_buffer)


if __name__ == "__main__":
    main()
