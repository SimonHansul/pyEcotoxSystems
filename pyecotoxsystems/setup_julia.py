# pyecotoxsystems/setup_julia.py
import os
import sys
from juliacall import Main as jl
import juliapkg


juliapkg.add(
        "EcotoxSystems", "a070e96f-54e2-4e3c-8571-6208d1dd8981",
        url="https://github.com/simonhansul/ecotoxsystems.jl.git"
    )
juliapkg.resolve()
jl.seval("using EcotoxSystems")
