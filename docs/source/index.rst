Welcome to the Pyface documentation!
=======================================

If you want to display Traits-based user interfaces, you need, in addition to
the Traits project:

    -The TraitsUI project
    -A Python GUI toolkit, either wxPython or PyQt
    -A "backend" connector, either TraitsBackendWX or TraitsBackendQt

TraitsUI contains a toolkit-independent GUI abstraction layers, used to support
the "visualization" features of the Traits package. Thus, you can write code in
terms of the Traits API (view, items, editors, etc.), and let Pyface and your
selected toolkit and backend take care of the details of displaying them.

Pyface
------

Pyface enables programmers to interact with generic GUI objects, such as an
"MDI Application Window", rather than with raw GUI widgets. (Pyface is named by
analogy to JFace in Java.) Traits uses Pyface to implement views and editors
for displaying and editing Traits-based objects.

Toolkit Backends
----------------

Traits and Pyface define APIs that are independent of any GUI toolkit. However,
in order to actually produce user interfaces with them, you must install a
supported Python-based GUI toolkit and the appropriate toolkit-specific backend
project. Conversely, if you wish to use Traits without a UI, a "null" backend
is automatically used in the absence of a real backend.

Currently, the supported GUI toolkits are wxPython, PySide and PyQt. While all
toolkits funtion with Traits, integration with wxPython is currently more
complete. All future development, however, will focus on supporting Qt.

.. warning:: Currently the default toolkit if none is supplied is 'wx', but
   this will change to `qt` in Pyface 5.0.

NOTE: Although the code in this library is BSD licensed, when the PyQt backend
is used the more restrictive terms of PyQt's GPL or proprietary licensing will
likely apply to your code.

Contents
--------

.. toctree::
   :maxdepth: 2

   API Documentation <api/pyface>
