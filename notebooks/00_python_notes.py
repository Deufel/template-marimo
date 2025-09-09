import marimo

__generated_with = "0.15.2"
app = marimo.App(app_title="Mike's Python Notes")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""# Python Notes (archive)""")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## Virtual Enviorments""")
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        rf"""
    ```py
    python3 -m venv .venv                 # Create Virtual Enviorment
    source ./.venv/bin/activate           # Activate Virtual Enviorment
    pip install numpy pandas              # Install Package(s)
    pip install --upgrade <package_name>  # Upgrade Package
    pip freeze > requirements.txt         # make requirements.txt file
    deactivate                            # To exit .venv
    pip install -r requirements.txt       # How to use the requirements.txt file


    # ----- Additional usefull commands ----- 
    echo ".venv/" >> .gitignore           # Don't commit venv to git
    pip list                              # Show installed packages
    pip show <package_name>               # Show package info/dependencies
    pip uninstall <package_name>          # Remove a package
    pip install -e .                      # Install current proj in edit mode
    pip install -e '.[dev]'       # Install current proj in edit mode + dev deps 
    which python                          # Verify you're using venv Python
    rm -rf .venv                          # Delete virtual environment
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## Random Usefull """)
    return


@app.cell
def _():
    # Shuffle data
    import numpy as np
    data = np.array(['a', 'b', 'c', 'd', 'e'])
    indices = np.random.permutation(len(data))
    shuffled = data[indices]
    print(f"{data = }")
    print(f"{indices = }")
    print(f"{shuffled = }")
    return


@app.cell
def _():
    # F-string tricks
    from datetime import datetime
    n = 345_320_000
    print(f'{n:,}')                 # 1,000s seperator with ',' (can also use _)
    print(f'{n:>20}')               # Right align w/ 20 spaces; 
    print(f'{n:^20}')               # center align w/ 20 spaces; 
    print(f'{datetime.now(): %c}')  # Date formatting lots more optins available ..
    print(f'{n = }')                # Will output "n = ...." much nicer way to check vars
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
