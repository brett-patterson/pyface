#------------------------------------------------------------------------------
# Copyright (c) 2007, Riverbank Computing Limited
# All rights reserved.
# 
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#------------------------------------------------------------------------------

import wx

from enthought.pyface.api import Toolkit

from about_dialog import AboutDialog_wx
from application_window import ApplicationWindow_wx
from confirmation_dialog import ConfirmationDialog_wx
from dialog import Dialog_wx
from directory_dialog import DirectoryDialog_wx
from file_dialog import FileDialog_wx
from gui import GUI_wx
from image_cache import ImageCache_wx
from image_resource import ImageResource_wx
from message_dialog import MessageDialog_wx
from python_shell import PythonShell_wx
from resource_manager import PyfaceResourceFactory_wx
from splash_screen import SplashScreen_wx
from system_metrics import SystemMetrics_wx
from widget import Widget_wx
from window import Window_wx

from action.action_item import _MenuItem_wx, _Tool_wx
from action.menu_bar_manager import MenuBarManager_wx
from action.menu_manager import MenuManager_wx
from action.tool_bar_manager import ToolBarManager_wx

from workbench.editor import Editor_wx
from workbench.view import View_wx
from workbench.workbench_window_layout import WorkbenchWindowLayout_wx

# Private initialisers to call after the toolkit has been initialised.
from enthought.pyface.dock.dock_sizer import init_dock_sizer


class Toolkit_wx(Toolkit):
    """ Implementation of the wx toolkit. """

    _MenuItem = _MenuItem_wx
    _Tool = _Tool_wx
    AboutDialog = AboutDialog_wx
    ApplicationWindow = ApplicationWindow_wx
    ConfirmationDialog = ConfirmationDialog_wx
    Dialog = Dialog_wx
    DirectoryDialog = DirectoryDialog_wx
    Editor = Editor_wx
    FileDialog = FileDialog_wx
    GUI = GUI_wx
    ImageCache = ImageCache_wx
    ImageResource = ImageResource_wx
    MenuBarManager = MenuBarManager_wx
    MenuManager = MenuManager_wx
    MessageDialog = MessageDialog_wx
    PyfaceResourceFactory = PyfaceResourceFactory_wx
    PythonShell = PythonShell_wx
    SplashScreen = SplashScreen_wx
    SystemMetrics = SystemMetrics_wx
    ToolBarManager = ToolBarManager_wx
    View = View_wx
    Widget = Widget_wx
    Window = Window_wx
    WorkbenchWindowLayout = WorkbenchWindowLayout_wx

    def init_toolkit(self, *args, **kw):
        """ Initialises the toolkit. """
        if wx.VERSION < (2, 6):
            raise RuntimeError, "Need wx version 2.6 or higher, but got %s" \
                    % str(wx.VERSION)

        self._app = wx.GetApp()

        if self._app is None:
            # FIXME v3: redirect and filename should have '_wx' or '_hint'
            # suffixes.
            try:
                redirect = kw['redirect']
            except KeyError:
                redirect = False
            else:
                del kw['redirect']

            try:
                filename = kw['filename']
            except KeyError:
                filename = None
            else:
                del kw['filename']

            self._app = wx.PySimpleApp(redirect=redirect, filename=filename)

            # Before we can load any images we have to initialize wxPython's
            # image handlers.
            wx.InitAllImageHandlers()

        # Other toolkit specific initialisation.
        init_dock_sizer()