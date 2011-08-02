""" Defines all of the window elements, as well as tying everything together into one
app. """

# I seriously need to figure out what the hell I'm doing with the imports.

import wx
import PreviewRenderer
from SaveLoad import *

class PygameDisplay(wx.Window):
    """ Taken from a pygame.org entry by David Barker 
        Still learning what's what."""
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.parent = parent
        self.hwnd = self.GetHandle()
        
        self.size = self.GetSizeTuple()
        self.size_dirty = True
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.Update, self.timer)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        
        self.fps = 60.0
        self.timespacing = 1000.0 / self.fps
        self.timer.Start(self.timespacing, False)
        
        
    
    def Update(self, event):
        # Any update tasks would go here (moving sprites, advancing animation frames etc.)
        self.Redraw()
    
    def Redraw(self):
        
        
        s = pygame.image.tostring(self.screen, 'RGBA')  # Convert the surface to an RGB string
        img = wx.ImageFromData(self.size[0], self.size[1], s)  # Load this string into a wx image
        bmp = wx.BitmapFromImage(img)  # Get the image in bitmap form
        dc = wx.ClientDC(self)  # Device context for drawing the bitmap
        dc.DrawBitmap(bmp, 0, 0, False)  # Blit the bitmap image to the display
        del dc
    
    def OnPaint(self, event):
        self.Redraw()
        event.Skip()  # Make sure the parent frame gets told to redraw as well
    
    def OnSize(self, event):
        # Need to figure out a way to make this a static size.
        # That way I can keep the previewer embedded into it's own frame.
        self.size = self.GetSizeTuple()
        self.size_dirty = True
    
    def Kill(self, event):
        # Make sure Pygame can't be asked to redraw /before/ quitting by unbinding all methods which
        # call the Redraw() method
        # (Otherwise wx seems to call Draw between quitting Pygame and destroying the frame)
        # This may or may not be necessary now that Pygame is just drawing to surfaces
        self.Unbind(event = wx.EVT_PAINT, handler = self.OnPaint)
        self.Unbind(event = wx.EVT_TIMER, handler = self.Update, source = self.timer)

class MasterWindow(wx.Frame):
    """The frame that contains everything!
    Nothing in it, at the moment, except for test junk."""
    def __init__(self, parent=None, ID=-1, title='Charas+'):
        super(MasterWindow, self).__init__(parent, ID, title)
        self.Show()

# Test code Down There.

app = wx.App()
test = MasterWindow()
app.MainLoop()