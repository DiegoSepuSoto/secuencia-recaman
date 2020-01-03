from graphics import *


class Arc(Oval):  # Código robado totalmente de stackoverflow
    def __init__(self, p1, p2, start, extent):
        self.extent = extent
        self.start = start
        super().__init__(p1, p2)

    def __repr__(self):
        return "Arc({}, {}, {})".format(
            str(self.p1), str(self.p2), self.start, self.extent
        )

    def clone(self):
        other = Arc(self.p1, self.p2, self.start, self.extent)
        other.config = self.config.copy()
        return other

    def _draw(self, canvas, options):
        p1 = self.p1
        p2 = self.p2
        x1, y1 = canvas.toScreen(p1.x, p1.y)
        x2, y2 = canvas.toScreen(p2.x, p2.y)
        options["style"] = tk.ARC
        options["extent"] = self.extent
        options["start"] = self.start
        return canvas.create_arc(x1, y1, x2, y2, options)
