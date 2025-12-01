from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

from .docking import run_vina

app = FastAPI()

class DockingParams(BaseModel):
    receptor_path: str
    ligand_path: str
    center_x: float
    center_y: float
    center_z: float
    size_x: float
    size_y: float
    size_z: float
    runs: int = 1
    exhaustiveness: int = 8

@app.post("/dock")
def dock(params: DockingParams):
    out_files = run_vina(
        receptor=Path(params.receptor_path),
        ligand=Path(params.ligand_path),
        center_x=params.center_x,
        center_y=params.center_y,
        center_z=params.center_z,
        size_x=params.size_x,
        size_y=params.size_y,
        size_z=params.size_z,
        runs=params.runs,
        exhaustiveness=params.exhaustiveness,
    )
    return {"output_files": [str(p) for p in out_files]}