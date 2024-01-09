""" Put where UniteDescriptor.ndf located and run 
    For 9 jan 2024 UniteDescriptor.ndf location is:
    <mod_name>/GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf
"""

from tqdm import tqdm # type: ignore


def change_all_units_description(
    DetectionTBA: int=1400000,
    PorteeVision: int=1400000,
    OpticalStrength: int=999,
    UnitConcealmentBonus: float=0.0
) -> str:
    new_buffer: str = ""
    with open("UniteDescriptor.ndf", "r+", encoding="utf-8") as f:
        for line in tqdm(f.readlines()):
            # Detection FOV 1
            if "DetectionTBA = " in line:
                new_buffer += f"            DetectionTBA = (({DetectionTBA}) * Metre)\n"
                continue
            # Detection FOV 2
            if "PorteeVision = " in line:
                new_buffer += f"            PorteeVision = (({PorteeVision}) * Metre)\n"
                continue
            # Strengh of optics 
            if "OpticalStrength = " in line:
                new_buffer += f"            OpticalStrength = {OpticalStrength}\n"
                continue
            # No hidding bonus 
            if "UnitConcealmentBonus = " in line:
                new_buffer += f"            UnitConcealmentBonus = {UnitConcealmentBonus}"
            new_buffer += line 
    return new_buffer


def write_buffer(
    path: str,
    new_buffer: str
) -> None:
    with open(path, "w+", encoding="utf-8") as f:
        f.write(new_buffer)


def main():
    new_buffer = change_all_units_description()
    write_buffer(
        path="UniteDescriptor.ndf",
        new_buffer=new_buffer
    )


if __name__ == "__main__":
    main()