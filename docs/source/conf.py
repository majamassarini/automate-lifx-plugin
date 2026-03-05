# Configuration file for the Sphinx documentation builder.
#
# For a full list of options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../../"))

# -- Project information -----------------------------------------------------

project = "lifx-plugin"
copyright = "2021, Maja Massarini"
author = "Maja Massarini"

# The full version, including alpha/beta/rc tags
release = "0.9"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
]
autodoc_inherit_docstrings = True
autodoc_default_options = {
    "member-order": "bysource",
    "members": True,
    "undoc-members": True,
}

templates_path = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
