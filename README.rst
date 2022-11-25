Documentation and tooling to help upgrading Robot Framework
===========================================================

Documentation
-------------

Presentable documentation is in the `<RF29to60.pdf>`_ slide deck.
See `Regenerating documentation`_ if you want to make changes.

Tooling
-------

As the documentation explains, the biggest backwards incompatible changes are
the updated FOR loop syntax and changes to the variable item access. With both
of these the old syntax still works in RF 3.2, but causes a deprecation warning,
and with RF 4.0 you need to use the new syntax.

The provided `<rf32to40.py>`_ script can convert data using the old syntax so
that it is compatible with RF 4.0. The script requires using Robot Framework 3.2.x
with Python 3.6 or newer. Notice that the script updates files in-place so you
*should have them in version control* to see what has changed. This is how to
use the script::

    # Install RF 3.2.2 as a precondition. Creating a venv first is recommended.
    pip install robotframework==3.2.2

    # Update one file. File is-updated inplace!
    python rf32to40.py tests.robot

    # Update all '*.robot' files in a directory.
    python rf32to40.py tests/*.robot

    # Update all '*.robot' files in a directory recursively.
    python rf32to40.py tests/**/*.robot

Regenerating documentation
--------------------------

Documentation is generated from `reStructuredText
<https://en.wikipedia.org/wiki/ReStructuredText>`_ source in `<RF29to60.rst>`_
using the `rst2pdf <https://rst2pdf.org>`_ tool. Follow these these steps if you
make changes and want to regenerate the PDF::

    # Install rst2pdf. Consider using a venv.
    pip install rst2pdf

    # Regenerate PDF.
    rst2pdf --stylesheets styles.yaml --break-level 1 RF29to60.rst RF29to60.pdf

Presentation styles or configured in `<styles.yaml>`_. For information about
the syntax see `rt2pdf documentation <https://rst2pdf.org/static/manual.html#styles>`_.
These styles were initially copied from
https://github.com/tibs/reST-slides-talk/blob/main/light16x9.style.
