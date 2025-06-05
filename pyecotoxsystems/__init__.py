from .setup_julia import jl

# Get exported names and convert symbols to strings
exported = jl.seval("""[String(sym) for sym in names(EcotoxSystems; all=false, imported=false)]""")

__all__ = exported  # now __all__ is a list of strings

# Dynamically re-export
for name in exported:
    try:
        globals()[name] = getattr(jl.EcotoxSystems, name)
    except Exception as e:
        print(f"Warning: could not import {name}: {e}")
