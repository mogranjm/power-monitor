from pathlib import Path
from environ import Env
import logging

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
ENV_FILE = BASE_DIR / ".env"

env = Env()

if Path(ENV_FILE).exists():
	env.read_env(str(ENV_FILE))

ENV_NAME = env("ENVIRONMENT_NAME")

logging.basicConfig(
	filename=f"{LOG_DIR / ENV_NAME}.log",
	format="%(asctime)s | %(levelname)s | %(name)s |\t %(message)s"
)