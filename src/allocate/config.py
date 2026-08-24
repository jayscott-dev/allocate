from dataclasses import dataclass
from pathlib import Path
import tomllib

GLOBAL_CONFIG = Path.home() / ".config" / "allocate" / "config.toml"
LOCAL_CONFIG = Path("config.toml")
DEFAULT_CONFIG = Path("default_config.toml")

@dataclass(frozen=True)
class Settings:
    budgets_file: str

def read_config(config_file: Path) -> dict:
    if config_file.exists():
        with config_file.open("rb") as f:
            config = tomllib.load(f)
    else:
        config = {}
    return config

def load_config() -> Settings:
    config = read_config(DEFAULT_CONFIG)
    config = config | read_config(LOCAL_CONFIG)
    config = config | read_config(GLOBAL_CONFIG)

    return Settings(budgets_file = config["budgets_file"])

SETTINGS = load_config()
