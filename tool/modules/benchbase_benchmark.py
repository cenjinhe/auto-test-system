import time
import logging
from typing import Any, Dict, List


def Prepare() -> None:
  """Prepare stage."""
  print("done Prepare")


def Run() -> List:
  """Run stage."""
  print("done Run")


def Cleanup() -> None:
  """Cleanup stage."""
  print("done Cleanup")
