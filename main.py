import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit, 
                             QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtGui import QColor

class RevenueCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Twitch Ad Revenue Calculator")
        self.setGeometry(400, 300, 400, 300)
        self.setStyleSheet("background-color: #192843; color: white")

        # Create labels and input fields
        self.ads_run_label = QLabel("Number of Ads Run per Stream:")
        self.ads_run_entry = QLineEdit()
        self.duration_per_ad_label = QLabel("Duration per Ad (minutes):")
        self.duration_per_ad_entry = QLineEdit()
        self.rate_per_ad_label = QLabel("Rate per Ad:")
        self.rate_per_ad_entry = QLineEdit()
        self.calculate_button = QPushButton("Calculate Revenue")
        self.calculate_button.clicked.connect(self.calculate_revenue)
        self.calculate_button.setStyleSheet("background-color: #00FF00; color: white; font-weight: bold; font-size: 18px; border-radius: 5px; padding: 8px")
        self.revenue_label = QLabel("")
        
        # Create layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.ads_run_label)
        self.layout.addWidget(self.ads_run_entry)
        self.layout.addWidget(self.duration_per_ad_label)
        self.layout.addWidget(self.duration_per_ad_entry)
        self.layout.addWidget(self.rate_per_ad_label)
        self.layout.addWidget(self.rate_per_ad_entry)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.revenue_label)
        
        self.setLayout(self.layout)

    def calculate_revenue(self):
        ads_run = int(self.ads_run_entry.text())
        rate_per_ad = float(self.rate_per_ad_entry.text())

        # calculate revenue
        revenue = ads_run * rate_per_ad
        self.revenue_label.setText("You have earned $" + str(revenue) + " from your ads.")
        self.revenue_label.setStyleSheet("background-color: #6441a5; color: white; font-weight: bold; font-size: 18px; border-radius: 5px; padding: 8px")
        self.revenue_label = QLabel("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = RevenueCalculator()
    calculator.show()
    sys.exit(app.exec_())
