import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import PhishingTool

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhishingTool()
    window.show()
    sys.exit(app.exec_())