import pyqtgraph as pg
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Temperature vs time plot
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)

        

app = QtWidgets.QApplication([])
main = MainWindow()



time =          [0, 1, 2, 3, 4,  5,  6,  7,   8,   9,   10]
temperature =   [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

pen = pg.mkPen(color=(255, 255, 255), width=2)

main.plot_graph.addLegend()

main.plot_graph.plot(
    time,
    temperature,
    name="Temperature Sensor",
    pen=pen,
    symbol="x",
    symbolSize=10,
    symbolBrush="#ffffff",
)

main.plot_graph.showGrid(x=True, y=True)

styles = {"color": "#ffffff", "font-size": "18px"}
main.plot_graph.setTitle("Temperature vs Time", **styles)
main.plot_graph.setLabel("left", "Temperature (°C)", **styles)
main.plot_graph.setLabel("bottom", "Time (min)", **styles)

main.plot_graph.setXRange(0, 11, padding = 0)
main.plot_graph.setYRange(0, 1100, padding = 0)

main.resize(1800, 900)

main.show()
app.exec()