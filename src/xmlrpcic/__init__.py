import gtk
from gui import MainWindow

def main():
    win = MainWindow()
    
    win.setup()
    
    win.set_size_request(600,500)
    win.show_all()
    
    gtk.gdk.threads_init()
    gtk.main()
    
if __name__ == '__main__':
    main()