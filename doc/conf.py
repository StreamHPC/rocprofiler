# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

doxygen_project = {"name": "rocprofilerv2", "path": "."}
doxygen_root = "."
doxysphinx_enabled = True
extensions = ["rocm_docs", "rocm_docs.doxygen"]
external_projects_current_project = "rocprofiler"
full_project_name = "rocprofilerv2"
html_theme = "rocm_docs_theme"
html_title = full_project_name
