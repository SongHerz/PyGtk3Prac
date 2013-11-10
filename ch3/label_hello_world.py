#!/usr/bin/env python

from gi.repository import Gtk

win = Gtk.Window( title = "Hello World")

label = Gtk.Label()
label.set_label("Hello World")
label.set_angle( 25)
label.set_halign( Gtk.Align.END)

win.add( label)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
