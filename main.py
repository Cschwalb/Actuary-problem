
class printMenu:
    sWidgetName = None

    def MillerBanner(self):
        '''
        a nice little header...
        '''
        print("\t\t\t\t\t\t---------------------------------------------\n")
        print("\t\t\t\t\t\t****Miller Company Sales Forecast Program****\n")
        print("\t\t\t\t\t\t---------------------------------------------\n")


    def NameOfProduct(self):
        ''' This is to get the widget name'''
        self.sWidgetName = input("What is the name of the product:")
        return self.sWidgetName

    def warningScream(self):
        """ Demand numerics only"""
        print("\t\t\t\t\t\t\t\t****ENTER ONLY NUMERIC INFORMATION IN ALL THE FOLLOWING PROMPTS***\n")

    def getWidgetPrice(self):
        nNumber = 0
        while nNumber == 0:
            self.WidgetPrice = input("Enter current annual sales for the product %s : $" % self.sWidgetName)
            nNumber = self.WidgetPrice
        return self.WidgetPrice
        ''' returning input on widget cost'''

    def getExpectedAnualGrowth(self):
        ''' this is going to be a weird decimal.'''
        nNumber = 0
        while nNumber == 0:
            self.fGrowth = input("Enter expeced annual growth rate (in decimal format such as 7% is 7): ")
            nNumber = self.fGrowth
        return self.fGrowth

    def getNumberOfYears(self):
        nNumber = 0
        while nNumber == 0:
            self.Years = input("Enter the number of years you want to project sales growth: ")
            nNumber = self.Years
        return self.Years


class doActuary:

    def showMenu(self):
        print("****** WIDGET SALES INFORMATION ******\n")

    def main(self, fWidgetCost=1000.00, nYear=5, fGrowth=.07, fBeginningSales=1000.00, fEndingSales=(1.07) * 1000):
        object=printMenu()
        print("\n\n")
        object.MillerBanner()
        sWidgetName = object.NameOfProduct()
        object.warningScream()
        print("\n\n")
        self.fWidgetCost = object.getWidgetPrice()
        self.APR = object.getExpectedAnualGrowth()
        self.Years = object.getNumberOfYears()
        self.writeTop()
        self.RunLine()
        print("Total money expected off this item over five years ")


    def writeTop(self):
        print("year\t\t\tBeginning Sales\t\t\tGrowth\t\t\tEnding Sales\n")
        print("------------------------------------------------------")


    def RunLine(self, nCount=1):
        fTotalMoney = 0.0;
        while nCount <= self.Years:
            self.fEndingCost = self.fWidgetCost * (1 + self.APR)
            self.lastGrowth = self.lastGrowth * (1 + (nCount * self.APR))
            self.fTotal = 0
            # lastGrowth needs to change...
            fTotalMoney = fTotalMoney + self.lastGrowth
            print("%d\t\t\t%.2f\t\t\t%.2f\t\t\t%.2f" % nCount,
                  self.fWidgetCost,
                self.fEndingCost)

            nCount = nCount + 1
            self.fTotal = self.fTotal + self.lastGrowth
        print("Total sales growth for %d years is: $%.2\nf",
              self.Years,
              self.lastGrowth)
        print("Percent Growth of Initial %.2f sales is: %.1f%" % self.fWidgetCost,
              self.fTotal)
        print("The total amount of sales for the %d year period is: %.2f",
              self.Years, fTotalMoney)

object=doActuary()
object.main()