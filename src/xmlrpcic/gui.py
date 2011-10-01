'''
Created on Oct 1, 2011

@author: kinow
'''
import pygtk
pygtk.require('2.0')
import gtk

class MainWindow(gtk.Window):
    
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect('destroy', lambda w: gtk.main_quit())
        self.connect('delete_event', lambda w, event: gtk.main_quit())
        self.set_title('XML-RPC Introspection Client')
        self.serverEntry = None
        
    def setup(self):
        vbox1 = gtk.VBox(False, 3)
        self.add(vbox1)
        vbox1.show()
        
        topPanel = self.makeTopPanel()
        align1 = gtk.Alignment(0, 0, 1, 0)
        align1.add(topPanel)
        align1.show()
        vbox1.pack_start(align1);
        topPanel.show()
        
        mainPanel = self.makeMainPanel()
        vbox1.pack_start(mainPanel)
        mainPanel.show()
        
    def makeTopPanel(self):
        # create box for xml-server label, input and go button
        box1 = gtk.HBox(False, 3)
        box1.set_border_width(2)
        
        # the server label
        label1 = gtk.Label('XML-RPC Server: ')
        label1.set_padding(10, 0)
        
        # the server text etrny
        self.serverEntry = gtk.Entry(2000)
        self.serverEntry.set_text('http://localhost/testlink-1.9.3/lib/api/xmlrpc.php')
        
        # finally the button
        button1 = gtk.Button('Go')
        button1.set_property('width-request', 50)
        
        box1.pack_start(label1, False, False, 0)
        box1.pack_start(self.serverEntry, True, True, 0)
        box1.pack_start(button1, False, False, 0)
        
        label1.show()
        self.serverEntry.show()
        button1.show()
        
        return box1

    def makeMainPanel(self):
        box1 = gtk.VBox(False, 2)
        
        
        
        return box1

