import wx


# OopCompanion:suppressRename

class ColorFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(ColorFrame, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        sizer = wx.GridSizer(2, 2, 5, 5)  # 2 rows, 2 columns, 5px gaps

        # Button labels and corresponding colors
        self.buttons_config = [
            ("red", wx.Colour(255, 0, 0)),
            ("green", wx.Colour(0, 255, 0)),
            ("blue", wx.Colour(0, 0, 255)),
            ("quit", None)
        ]

        self.buttons = {}  # Store button references for testing

        for label, color in self.buttons_config:
            btn = wx.Button(panel, label=label)
            btn.Bind(wx.EVT_BUTTON, self.on_button)
            btn.color = color  # Custom attribute
            sizer.Add(btn, 1, wx.ALL | wx.EXPAND, 5)
            self.buttons[label] = btn  # Store button reference

        panel.SetSizer(sizer)
        self.panel = panel

        self.SetTitle("Color Buttons Example")
        self.SetSize((300, 200))  # More square-shaped for 2x2 grid
        self.Centre()

        # For testing purposes
        self.closed = False

    def on_button(self, event):
        btn = event.GetEventObject()
        return self.handle_button_click(btn.GetLabel())

    def handle_button_click(self, button_label):
        """Handle button click by label - can be called programmatically for testing"""
        print(f"Button clicked: {button_label}")

        if button_label == "quit":
            print("Action: Closing application")
            self.Close()
            self.closed = True
            return True
        else:
            btn = self.buttons.get(button_label)
            if btn and btn.color:
                color_str = f"({btn.color.Red()}, {btn.color.Green()}, {btn.color.Blue()})"
                print(f"Action: Changing background color to {button_label} {color_str}")
                self.panel.SetBackgroundColour(btn.color)
                self.panel.Refresh()
                return btn.color
            else:
                print(f"Action: Invalid button - no action taken")
        return False

    def get_background_color(self):
        """Get the current background color - useful for testing"""
        return self.panel.GetBackgroundColour()

    def simulate_button_click(self, button_label):
        """Simulate clicking a button - useful for testing"""
        return self.handle_button_click(button_label)


def run_app():
    app = wx.App(False)
    frame = ColorFrame(None)
    frame.Show()
    app.MainLoop()
    return app


if __name__ == "__main__":
    run_app()
