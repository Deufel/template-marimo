import marimo

__generated_with = "0.15.2"
app = marimo.App(app_title="Mike's Python Notes")

with app.setup:
    import marimo as mo


@app.cell
def _():
    mo.md(r"""# Python Notes""")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## Archive""")
    return


@app.cell(hide_code=True)
def _():
    mo.accordion(
        {"venv": mo.md(
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
        )}
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## Random Usefull""")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""### Shuffle data""")
    return


@app.cell
def _():
    import numpy as np
    data = np.array(['a', 'b', 'c', 'd', 'e'])
    indices = np.random.permutation(len(data))
    shuffled = data[indices]
    print(f"{data = }")
    print(f"{indices = }")
    print(f"{shuffled = }")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""### F string tricks""")
    return


@app.cell
def _():
    from datetime import datetime
    n = 345_320_000
    print(f'{n:,}')                 # 1,000s seperator with ',' (can also use _)
    print(f'{n:>20}')               # Right align w/ 20 spaces; 
    print(f'{n:^20}')               # center align w/ 20 spaces; 
    print(f'{datetime.now(): %c}')  # Date formatting lots more optins available ..
    print(f'{n = }')                # Will output "n = ...." much nicer way to check vars
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    ### Concise breadth-first search
    h/t JH
    """
    )
    return


@app.cell
def _():
    tree = {1: {2: {4: {}}, 3: {5: {}, 6: {}}}}

    def bfs(q):
        while q:
            k,v = zip(*q)
            print(*k)
            q = [x for o in v for x in o.items()]

    bfs(tree.items())
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## VIM""")
    return


@app.cell(hide_code=True)
def _():
    mo.md(
        r"""
    usefull commands
    ```
    :set wrap
    :set nowrap
    :set textwidth=80
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""## testing""")
    return


@app.cell
def _():
    mo.sidebar(
        [
            mo.md("# marimo"),
            mo.nav_menu(
                {
                    "#/home": f"{mo.icon('lucide:home')} Home",
                    "#/about": f"{mo.icon('lucide:user')} About",
                    "#/contact": f"{mo.icon('lucide:phone')} Contact",
                    "Links": {
                        "https://github.com/deufel": "GitHub",
                    },
                },
                orientation="vertical",
            ),
        ]
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
