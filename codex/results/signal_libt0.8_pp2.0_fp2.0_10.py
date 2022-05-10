import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle('Видеоинформационный канал')
window.resize(1500, 800)

central_widget = QWidget()
window.setCentralWidget(central_widget)

main_layout = QHBoxLayout()
central_widget.setLayout(main_layout)


# Определяем виджет для видео
videoWidget = VideoWidget()

# Определяем виджет для звука
soundWidget = SoundWidget()

# Упаковываем созданные виджеты в горизон
