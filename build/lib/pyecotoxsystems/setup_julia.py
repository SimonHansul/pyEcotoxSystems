# pyecotoxsystems/setup_julia.py
import os
import sys
from juliacall import Main as jl
import juliapkg

# Ensure the package is installed
def ensure_ecotoxsystems():
    # Add the package from GitHub (or Registry if published)
    juliapkg.add(
        "EcotoxSystems", "a070e96f-54e2-4e3c-8571-6208d1dd8981",
        url="https://github.com/simonhansul/ecotoxsystems.jl.git"
    )
    juliapkg.resolve()

    # Load package in Julia
    jl.seval("using EcotoxSystems")

# Call on import
ensure_ecotoxsystems()
