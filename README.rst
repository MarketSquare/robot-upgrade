Documentation and tooling to help upgrading Robot Framework
===========================================================

Documentation
-------------

Presentable documentation is in `<RF29to60.pdf>`_.

Documentation is generated from `<RF29to60.rst>`_ using `rst2pdf <https://rst2pdf.org>`_.
Follow these these steps if you make updates and want to regenerate the PDF::

    # Install rst2pdf.
    pip install rst2pdf

    # Regenerate PDF.
    rst2pdf --stylesheets styles.yaml --break-level 1 RF29to60.rst RF29to60.pdf

Tooling
-------

The biggest backwards incompatible changes are updated FOR loop syntax and
changes to the variable item access. With both of these the old syntax still
works in RF 3.2 but causes a deprecation warning and with RF 4.0 you need to
use the new syntax.

The provided `<rf32to40.py>`_ script can convert data using old syntax so that
it is compatible with RF 4.0. The script requires using Robot Framework 3.2.x
with Python 3.6 or newer. Notice that the script updates files in place so you
*should have them in version control*. This is how to use it::

    # Install RF 3.2.2 as a precondition.
    pip install robotframework==3.2.2

    # Update one file. File is updated inplace!
    python rf32to40.py tests.robot

    # Update all '*.robot' files in a directory.
    python rf32to40.py tests/*.robot

    # Update all '*.robot' files in a directory recursively.
    python rf32to40.py tests/**/*.robot
