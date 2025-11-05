import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    pd.DataFrame({"A": [1,2,3,4]})
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
