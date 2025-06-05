# pyecotoxsystems/__init__.py
from .setup_julia import jl  # Make sure Julia is ready

# Load package explicitly
jl.seval("using EcotoxSystems")

# Dynamically re-export all exported functions
_exported = jl.seval("names(EcotoxSystems, all=false)")

__all__ = []

for name in _exported:
    # Get reference to function
    try:
        func = jl.eval(f"EcotoxSystems.{name}")
        globals()[name] = func
        __all__.append(name)
    except Exception as e:
        print(f"Skipping {name}: {e}", file=sys.stderr)
