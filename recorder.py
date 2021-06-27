from config import width, height, top, left, screen
import mss

class Recorder:

    frame = None

    @staticmethod
    def captureScreen():
        with mss.mss() as sct:
            while True:
                display = sct.monitors[screen]
                monitor = {'top': display['top'] + top, 'left': display['left'] + left, 'width': width, 'height': height}
                img = sct.grab(monitor)
                Recorder.frame = mss.tools.to_png(img.rgb, img.size)