from dataclasses import dataclass
from pathlib import Path
import tomllib

@dataclass
class Settings:
    my_config: str

def load_config(config_file: Path) -> Settings:
    with config_file.open("rb") as f:
        config = tomllib.load(f)
    return Settings(my_config = config["my_config"])
