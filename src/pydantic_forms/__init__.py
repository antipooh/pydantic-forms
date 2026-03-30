from importlib.metadata import version

from .forms import PydanticForm
from .interfaces import BaseStrategy
from .objects import FormField
from .strategies import DefaultStrategy

__version__ = version("pydantic-forms")
