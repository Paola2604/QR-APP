from cx_Freeze import setup, Executable

modules = ["codigoprincipalQR.py", "generadorQR.py", "QRlector.py", "lecturaempleados.py", "codigoinicio.py"]

build_exe_options = {
    "packages": [],
    "excludes": [],
    "includes": ["calendar", "tkinter"]
}

executables = [Executable(module, base="Win32GUI", icon="icono.ico") for module in modules]

setup(
    name="QRapp",
    version="1.0",
    description="lector y generador de QR",
    options={
        "build_exe": build_exe_options,
    },
    executables=executables
)
