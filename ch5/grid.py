#!/usr/bin/env python

from gi.repository import Gtk

class GridWindow( Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__( self, title = "Grid Example")

        grid = Gtk.Grid()
        self.add( grid)

        buttons = [ Gtk.Button( label = "Button {}".format( n)) for n in xrange(1, 7)]
        map( lambda w: w.connect( "clicked", self.on_button_clicked), buttons)


        grid.add( buttons[0])
        grid.attach( buttons[1], 1, 0, 2, 1)
        grid.attach_next_to( buttons[2], buttons[0], Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to( buttons[3], buttons[2], Gtk.PositionType.RIGHT, 2, 1)
        grid.attach( buttons[4], 1, 2, 1, 1)
        grid.attach_next_to( buttons[5], buttons[4], Gtk.PositionType.RIGHT, 1, 1)
        pass

    def on_button_clicked( self, widget):
        print widget.get_label()
        pass

win = GridWindow()
win.connect( "delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
