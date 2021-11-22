"""

Program: investmentGUI.py
Author: Narvar 11/15/2021

*** Note: the file breezypythongui.py Must be in the same directory as this file for the application to work***

"""

from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):
	"""An investment calculator that demonstrates the use of a multi-line text area widget."""

	def __init__(self):
		"""Sets up the window an the widgets."""
		EasyFrame.__init__(self, title = "Investment Calculator")
		self.addLabel(text = "Initial Amount", row = 0, column = 0)
		self.addLabel(text = "Number of Years", row = 1, column = 0)
		self.addLabel(text = "Interest rate in %", row = 2, column = 0)
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)

		self.outputArea = self.addTextArea("", row = 4, column = 0, columnspan = 2, width = 50, height = 15)

		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		# button color change
		self.compute["background"] = "orange"


	# Event handling method
	def compute(self):
		"""Computes the investments schedule based on the inputs and outputs the schedules"""
		# Obtain and validates the inputs
		startBalance = self.amount.getNumber()
		rate = self.rate.getNumber() / 100
		years = self.period.getNumber()
		if  startBalance == 0 or rate == 0 or years == 0:
			return


		#Set the header for the table
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting balance", "Interest", "Ending balance")

		# Compute and append the results for eachc for each year
		totalInterest = 0.0 
		for year in range(1, years, + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % \
				(year, startBalance, interest, endBalance)
			totalInterest += interest

		# Append the totals for the period
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total Interest earned: $%0.2f\n" % totalInterest

		# Output the result while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"	
		
		
# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	TextAreaDemo().mainloop()

# global call to trigger main() function
if __name__ == "__main__":
	main()