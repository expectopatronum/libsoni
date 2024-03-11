# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import re
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))
LIBSONI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
assert os.path.exists(os.path.join(LIBSONI_DIR, 'libsoni'))
sys.path.insert(0, LIBSONI_DIR)
sys.path.insert(0, os.path.join(LIBSONI_DIR, 'util'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'libsoni'
copyright = '2024, Yigitcan Özer, Leo Brütting, Simon Schwär, Meinard Müller'
author = 'Yigitcan Özer, Leo Brütting, Simon Schwär, Meinard Müller'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme',
			  'sphinx.ext.autodoc',  # documentation based on docstrings
              'sphinx.ext.napoleon',  # for having google/numpy style docstrings
              'sphinx.ext.viewcode',  # link source code
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosummary',
              'sphinx.ext.extlinks']

templates_path = ['_templates']
exclude_patterns = []
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_use_index = True
html_use_modindex = True
html_logo = os.path.join(html_static_path[0], 'libsoni_logo.png')
napoleon_custom_sections = [('Returns', 'params_style'), ('Parameters', 'params_style')]