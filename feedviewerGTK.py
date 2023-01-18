#!/usr/bin/python

import feedparser
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello world")


        # Set size of the window
        self.set_default_size(900, 900)

        # Make a grid and add it to the window I guess?
        self.grid = Gtk.Grid()
        self.add(self.grid)

        # Make a scrollable window and attach the grid to it I guess?
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        # Create a text view
        self.textview = Gtk.TextView()

        # Make it a bit cleaner and nicer
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textview.set_editable(False)
        self.textview.set_cursor_visible(False)

        # Parse the URL
        file = feedparser.parse('https://www.reddit.com/r/news.rss')       
        
        # Get and set the text buffer
        self.text_buffer = self.textview.get_buffer()
        
        # Initialize variables
        i = 0
        text = ""

        # Display all the news headlines
        for elem in file['entries']:
            text += str(i) + ": "
            text += file.entries[i].title
            text += '\n\n\n'
            i += 1

        #self.text_buffer.set_text(file.entries[2].title)
        self.text_buffer.set_text(text)
        #self.add(self.textview)
        scrolledwindow.add(self.textview)


        
    def on_button_clicked(self, widget):
        print("Hello world!!")




window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

