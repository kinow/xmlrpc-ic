'''
Created on Oct 1, 2011

@author: kinow
'''
import gtk

class MainWindow(gtk.Window):
    
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect('destroy', lambda w: gtk.main_quit())
        self.connect('delete_event', lambda w, event: gtk.main_quit())
        self.set_title('XML-RPC Introspection Client')
        
        self.topPanel = None
        self.methodsPanel = None
        self.mainPanel = None
        self.statusBar = None
        
    def setup(self):
        