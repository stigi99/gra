import cx_Freeze

executables = [cx_Freeze.Executable("gra.py")]

cx_Freeze.setup(
    name="moja gra",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["logo.png","paletka.png","tlo.jpeg"]}},
    executables = executables

    )