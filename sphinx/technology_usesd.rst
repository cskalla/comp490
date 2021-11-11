Technology Used
=================

Maps
-----
To generate our maps we used a library called ipyLeaflet, which is a popular Java Script library Leaflet, implemented in Python. Python is very efficient and is a powerful tool for data analysis, which makes pair well a mapping library.
We wrote the code for the maps in a deveopment environment called Jupyter Notebook. Jupyter Notebook is web based and supports several different programming languages, including Python. Jupyter Notebook is popular among the scientific computing because of it's ability to integrate documentation and code. Jupyter Notebook allows code cells to be intermixed with markdown cells which can contain formatted text, pictures and other nice features. Additionally, output from code blocks can be displayed directly under the code cell, which is especially nice for producing visualizations. Jupyter Notebook files can be easily downloaded into formats such as PDF, HTML and LaTex. For our project the interactive nature of the maps prevents us from simply downloading them as HTML files, to assist us with this process we used a package called Sphinx to generate HTML files containing the interactive maps.

.. panels::

    .. image:: 25869250.png

    ++++++++++++++
--------
    .. image:: 619282-middle.png

Website

--------
This website was generated using an auto-documentation package called Sphinx. Sphinx has been used to create websites for other software products such as ipyLeaflet itself, and seaborn, a Python visualization library. Shinx takes Python files and creates nicely formatted documents to serve as code documentation. Sphinx has a special extension called nbconvert which can convert Jupyter Notebook .ipyb files and conver them into neat HTML files while preserving the functions of interactive maps and widgets. Once it was designed, the website was hosted in Github Pages, which is a free statis wwebpage hosting service provided by Github

.. panels::

    .. image:: 1_k55zm6GMp9tXzlNKM0es8A.png

    ++++++++++++++
