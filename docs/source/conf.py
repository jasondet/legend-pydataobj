# Configuration file for the Sphinx documentation builder.

import sys
from pathlib import Path

from pkg_resources import get_distribution

sys.path.insert(0, Path(__file__).parents[2].resolve().as_posix())
sys.path.append(Path("extensions").resolve().as_posix())

project = "legend-pydataobj"
copyright = "2023, the LEGEND Collaboration"
version = get_distribution("legend-pydataobj").version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "nbsphinx",
    "myst_parser",
    "IPython.sphinxext.ipython_console_highlighting",
    "numbadoc",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"

# Furo theme
html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/legend-exp/legend-pydataobj",
    "source_branch": "main",
    "source_directory": "docs/source",
}
html_title = f"{project} {version}"

# sphinx-napoleon
# enforce consistent usage of NumPy-style docstrings
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_use_ivar = True
napoleon_use_rtype = False

# intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "numba": ("https://numba.readthedocs.io/en/stable", None),
    "pandas": ("https://pandas.pydata.org/docs", None),
    "h5py": ("https://docs.h5py.org/en/stable", None),
    "pint": ("https://pint.readthedocs.io/en/stable", None),
}  # add new intersphinx mappings here

# sphinx-autodoc
autodoc_default_options = {"ignore-module-all": True}
# Include __init__() docstring in class docstring
autoclass_content = "both"
autodoc_typehints = "both"
autodoc_typehints_description_target = "documented_params"
autodoc_typehints_format = "short"

# nbsphinx
nbsphinx_epilog = """
----

This page has been automatically generated by nbsphinx_ and can be run as a
Jupyter_ notebook available in the `legend-pydataobj repository
<https://github.com/legend-exp/legend-pydataobj/tree/main/docs/source/notebooks>`_.

.. _nbsphinx: https://nbsphinx.readthedocs.io/
.. _Jupyter: https://jupyter.org/
"""
