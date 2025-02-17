########################################################################
# IMPORTS
########################################################################
import webbrowser
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, Qt, QPoint
from PySide6.QtGui import QIcon
import sys
########################################################################
# IMPORT GUI FILE
from UI.MainUI import Ui_MainWindow
########################################################################
# CALCULATION
########################################################################
from sympy import symbols, Eq, solve
########################################################################
# MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ########################################################################
        # Main Window
        ########################################################################
        self.ui.pBClose.clicked.connect(self.close)
        self.ui.pBMin.clicked.connect(self.showMinimized)

        self.setWindowTitle("COMPOST RECIPE CALCULATOR")
        self.setWindowIcon(QIcon("CRC.ico"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        ########################################################################
        # Initiation Status
        ########################################################################
        self.W = self.ui.STQDATA
        self.W.setCurrentIndex(0)
        self.ui.ChLangFcomboBox.setCurrentIndex(2)
        self.initiation_status()
        ########################################################################
        # Global Values
        ########################################################################
        self.input_data = [self.ui.CMC01LineE, self.ui.CMC02FLineE, self.ui.CMC03LineE,
                           self.ui.NMN01LineE, self.ui.NMN02FLineE, self.ui.NMN03LineE,
                           self.ui.MMM01LineE, self.ui.MMM02FLineE, self.ui.MMM03LineE]
        self.values_str = [self.ui.Feed01CLineE, self.ui.Feed02CLineE, self.ui.Feed03CLineE,
                           self.ui.Feed01NLineE, self.ui.Feed02NLineE, self.ui.Feed03NLineE,
                           self.ui.Feed01MCLineE, self.ui.Feed02MCLineE, self.ui.Feed03MCLineE,
                           self.ui.CN01LineE, self.ui.MC02FLineE, self.ui.Wt03LineE]
        self.current_index = 1
        ########################################################################
        # Linking Buttons
        ########################################################################
        self.ui.pBNext.clicked.connect(self.next_page)
        self.ui.pBPrev.clicked.connect(self.prev_page)
        self.ui.pBCalc.clicked.connect(self.float_calculate)
        self.ui.pBStart.clicked.connect(self.start_button)
        self.ui.pBRestart.clicked.connect(self.restart_clear)
        self.ui.RounDspinBox.textChanged.connect(self.float_calculate)
        self.ui.pbInf.clicked.connect(self.open_github)
        self.connect_line_edits()
        self.text_bar_triggering()

    ###########################################################################
    # To Move The Frameless Window
    ###########################################################################
    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event) -> None:
        if self.offset is not None and event.buttons() == Qt.LeftButton:

            self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        self.offset = None
        super().mouseReleaseEvent(event)

    ###########################################################################
    # Buttons Functions
    ###########################################################################

    def prev_page(self) -> None:
        old_index = self.current_index
        new_index = (self.current_index - 1) % self.W.count()
        self.current_index = new_index
        self.side_animation(old_index, new_index)
        self.update_buttons(current_index=new_index)

    def next_page(self) -> None:
        old_index = self.current_index
        new_index = (self.current_index + 1) % self.W.count()
        self.current_index = new_index
        self.side_animation(old_index, new_index)
        self.update_buttons(current_index=new_index)

    def start_button(self) -> None:
        self.side_animation(old_index=0, new_index=1)
        self.update_buttons(current_index=self.W.currentIndex())
        self.check_feed_name()

    def restart_clear(self) -> None:
        self.side_animation(old_index=self.W.currentIndex(), new_index=0)
        self.ui.FeedSChFBox.setChecked(False)
        try:
            for i in range(len(self.values_str)):
                self.values_str[i].clear()
        except ValueError:
            pass

        self.initiation_status()

    def initiation_status(self) -> None:
        self.current_index = 1
        self.ui.pBNext.setDisabled(True)
        self.ui.pBPrev.setDisabled(True)
        self.ui.pBCalc.setDisabled(True)
        self.ui.pBRestart.setDisabled(True)
        self.ui.pBStart.setEnabled(True)
        self.ui.RounDspinBox.setValue(2)
        self.ui.progressBar.setValue(0)

    def update_buttons(self, current_index: int) -> None:
        self.ui.pBPrev.setDisabled(current_index <= 1)
        self.ui.pBNext.setEnabled(current_index < self.W.count() - 1)
        self.ui.pBCalc.setDisabled(current_index < 4)
        self.ui.pBRestart.setDisabled(current_index < 4)
        self.ui.pBStart.setDisabled(current_index >= 0)

    @staticmethod
    def open_github() -> None:
        webbrowser.open("https://github.com/OualiA/Compost.Recipe.Calculator")

    ###########################################################################
    # Functions
    ###########################################################################
    def connect_line_edits(self) -> None:
        input_data = self.input_data
        output_data = self.values_str
        for i in range(len(input_data)):
            input_data[i].textChanged.connect(
                lambda text=input_data[i].text, idx=i: self.sync_text(text, output_data, idx))
            output_data[i].textChanged.connect(
                lambda text=output_data[i].text, idx=i: self.sync_text(text, input_data, idx))

    @staticmethod
    def sync_text(text: str, target_list: list, index: int) -> None:
        if index < len(target_list):
            target_list[index].blockSignals(True)
            target_list[index].setText(text)
            target_list[index].blockSignals(False)

    """Calculation and Showing the Results"""

    def float_calculate(self) -> list:
        """Check if the Line edits empty/float and then apply the calculation and Show the result"""
        values_calc = self.values_str
        try:
            data = [float(x.text()) for x in values_calc]
            self.result_show(self.equation_result(values=data, round_to=int(self.ui.RounDspinBox.text())))

        except ValueError:
            for line_edit in values_calc:
                text = line_edit.text()
                if not text:
                    self.ui.FeedSChFBox.setChecked(True)
                    line_edit.setFocus()
                    return line_edit

                try:
                    float(text)
                except ValueError:
                    self.ui.FeedSChFBox.setChecked(True)
                    line_edit.setFocus()
                    return line_edit

            data = [float(x.text()) for x in values_calc]
            self.result_show(self.equation_result(values=data, round_to=int(self.ui.RounDspinBox.text())))

    @staticmethod
    def equation_result(values: list, round_to: int) -> list:
        """The simplified equations gets the data, calculate and then Return the results """
        # the variables
        q1, q2, q3 = symbols('q1 q2 q3')
        c1, c2, c3 = values[0], values[1], values[2]
        n1, n2, n3 = values[3], values[4], values[5]
        m1, m2, m3 = values[6], values[7], values[8]
        tq, cn, mc = values[11], values[9], values[10]

        # Use Matrix to solve the equations 1 and 2
        a = (q1 * (m1 * c3 * (100 - m3) - m1 * cn * n3 * (100 - m3) - m3 * c1 * (100 - m1) + cn * n3 * (
                100 - m3) * mc - cn * n1 * (100 - m1) * mc + c1 * (100 - m1) * mc - c3 * (
                           100 - m3) * mc + m3 * cn * n1 * (
                           100 - m1)))
        b = ((cn * n2 * (100 - m2) * mc) - (cn * n2 * (100 - m2) * m3) - (cn * n3 * (100 - m3) * mc) + (
                cn * n3 * (100 - m3) * m2) - (c2 * (100 - m2) * mc) + (c2 * (100 - m2) * m3) + (
                     c3 * (100 - m3) * mc) - (
                     c3 * (100 - m3) * m2))
        c = (q1 * ((cn * n1 * (100 - m1) * mc) - (cn * n1 * (100 - m1) * m2) - (cn * n2 * (100 - m2) * mc) + (
                cn * n2 * (100 - m2) * m1) - (c1 * (100 - m1) * mc) + (c1 * (100 - m1) * m2) + (
                           c2 * (100 - m2) * mc) - (
                           c2 * (100 - m2) * m1)))
        # Use sympy for a Linear solve of the 3 equations
        eq1 = Eq(a / b, q2)
        eq2 = Eq(c / b, q3)
        eq3 = Eq((q1 + q2 + q3), tq)
        solution = solve([eq1, eq2, eq3], [q1, q2, q3])
        results = [solution[q1], solution[q2], solution[q3]]
        return [str(round(x, round_to)) for x in results]

    def result_show(self, result: list) -> None:
        """Display the result on Widgets"""
        lines_edits = [self.ui.VWP01LineE, self.ui.VWP02LineE, self.ui.VWP03LineE]
        for i in range(len(result)):
            lines_edits[i].setText(result[i])

        feedstocks_names = self.check_feed_name()
        self.ui.ResultLineE.setPlainText(
            f"{feedstocks_names[0]}= {result[0]} (Kg) + "
            f"{feedstocks_names[1]}= {result[1]} (Kg) + "
            f"{feedstocks_names[2]}= {result[2]} (Kg)")

    def check_feed_name(self) -> list:
        # Display it as Sentence

        feed_lines = [self.ui.NameM01LineE, self.ui.NameM02FLineE, self.ui.NameM03LineE]
        groupbox_titles = [self.ui.Feed01F, self.ui.Feed02F, self.ui.Feed03F]
        lang = self.ui.ChLangFcomboBox.currentIndex()
        names_feed = {0: "المادة الأولية", 1: "Matières Premières", 2: "FeedStock", 3: "原料"}

        for i, line_edit in enumerate(feed_lines):
            if line_edit.text().strip():
                groupbox_titles[i].setTitle(line_edit.text().strip())

            else:
                groupbox_titles[i].setTitle(f"{names_feed.get(lang)} 0{i + 1}")
        titles = [x.title() for x in groupbox_titles]
        return titles

    ########################################################################
    # Animation
    ########################################################################
    """The Slide Animation in the StackWidget"""

    def side_animation(self, old_index: int, new_index: int) -> None:
        """Animate the StackWidget pages"""
        direction = 1 if old_index < new_index else -1

        current_widget = self.W.widget(old_index)
        next_widget = self.W.widget(new_index)

        width = self.W.frameGeometry().width()

        next_widget.setGeometry(QRect(width, 0, width, self.W.height()))
        next_widget.show()

        self.anim = QPropertyAnimation(next_widget, b"geometry")
        self.anim.setDuration(500)
        self.anim.setEasingCurve(QEasingCurve.OutQuad)
        self.anim.setStartValue(QRect(direction * width, 0, width, self.W.height()))
        self.anim.setEndValue(QRect(0, 0, width, self.W.height()))

        self.anim2 = QPropertyAnimation(current_widget, b"geometry")
        self.anim2.setDuration(500)
        self.anim2.setEasingCurve(QEasingCurve.OutQuad)
        self.anim2.setStartValue(QRect(0, 0, width, self.W.height()))
        self.anim2.setEndValue(QRect(-direction * width, 0, width, self.W.height()))

        self.anim.start()
        self.anim2.start()

        self.anim2.finished.connect(lambda: self.W.setCurrentIndex(new_index))

    """The Animation of the progress Bar"""

    def text_bar_triggering(self) -> None:
        """Update the Progress Bar Every time Lineedit changes"""
        line = self.values_str[8:] + self.input_data
        for c in range(len(line)):
            line[c].textChanged.connect(self.update_progressbar)

    def update_progressbar(self) -> None:
        """Update the Progress Bar"""
        filled_edits = sum(1 for line_edit in self.values_str if line_edit.text().strip())
        total_edits = len(self.values_str)
        progress = (filled_edits / total_edits)
        self.ui.progressBar.setValue(int(progress * 100))

    ########################################################################


########################################################################
# EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    app.setStyleSheet(open("Assets/Themes/Dark.qss").read())
    Window.show()
    sys.exit(app.exec())
########################################################################
# END===>
########################################################################
