import subprocess
from pathlib import Path
from typing import List, Dict

VINA_PATH = Path("third_party/autodock_vina/macos/vina_1.2.7_mac_aarch64")

def run_vina(
    receptor: Path,
    ligand: Path,
    center_x: float,
    center_y: float,
    center_z: float,
    size_x: float,
    size_y: float,
    size_z: float,
    runs: int = 1,
    exhaustiveness: int = 8,
    output_dir: Path = Path("outputs"),
) -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    receptor_name = receptor.stem
    ligand_name = ligand.stem

    out_files: List[Path] = []

    for i in range(1, runs + 1):
        out_file = output_dir / f"{receptor_name}_{ligand_name}_{i}.pdbqt"
        cmd = [
            str(VINA_PATH),
            "--receptor", str(receptor),
            "--ligand", str(ligand),
            "--center_x", str(center_x),
            "--center_y", str(center_y),
            "--center_z", str(center_z),
            "--size_x", str(size_x),
            "--size_y", str(size_y),
            "--size_z", str(size_z),
            "--exhaustiveness", str(exhaustiveness),
            "--seed", str(i),
            "--out", str(out_file),
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Vina failed on run {i}: {result.stderr}")

        out_files.append(out_file)

    return out_files