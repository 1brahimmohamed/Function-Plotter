from main import *
from ui_functions import *

import numpy as np


class Functions(MainWindow):
    """
    This class contains all the application logic functions

    ...

    Methods
    -------
    plot()
        Plots the function on the canvas
    isValidFunction(function_string)
        Checks if the function is valid
    isValidInterval(min_limit, max_limit)
        Checks if the interval is valid
    getFunctionString()
        Returns the function string
    getMaxMinValues()
        Returns the max and min values
    """

    def __init__(self):
        super().__init__()

    def plot(self):

        """
        get the function string and the max and min values and validate them then plot the function
        :return:
        """

        # get the function string and the max and min values
        function_string = Functions.getFunctionString(self)
        max_limit, min_limit = Functions.getMaxMinValues(self)
        Functions.plotting_operations(self, function_string, min_limit, max_limit)

    def plotting_operations(self, function_string, min_limit, max_limit):
        # check if the user entered "**" instead of "^"
        if '**' in function_string:
            UIFunctions.setFunctionStringError(self, 'You must use ^ instead of **')
            return False

        # replace ^ with ** to be able to evaluate the function
        function_string = function_string.replace('^', '**')

        # replace X with x to be able to evaluate the function
        function_string = function_string.replace('X', 'x')

        # check if the function is valid
        if not Functions.isValidFunction(self, function_string):
            return

        # check if the interval is valid
        if not Functions.isValidInterval(self, min_limit, max_limit):
            return

        # set the style sheet of the function string to no error
        UIFunctions.setFunctionStringNoError(self)
        UIFunctions.setMaxMinLimitNoError(self, self.ui.maxLimitNumber)
        UIFunctions.setMaxMinLimitNoError(self, self.ui.minLimitNumber)

        # plot the function
        Functions.plotFunction(self, function_string, min_limit, max_limit)

    def isValidFunction(self, function_string):

        """
        check if the function is valid
        :param function_string: the user entered function
        :return: True if the function is valid, False otherwise
        """
        if function_string == '':
            UIFunctions.setFunctionStringError(self, 'You must enter a function')
            return False

        # if user entered a function with a variable other than x
        if 'x' not in function_string:
            UIFunctions.setFunctionStringError(self, 'You must enter a function with a variable x')
            return False

        # check if the function has other variables except x and numbers
        for i in range(len(function_string)):
            if function_string[i] == 'x':
                continue
            elif function_string[i] == '+' \
                    or function_string[i] == '-' \
                    or function_string[i] == '*' \
                    or function_string[i] == '/' \
                    or function_string[i] == '^' \
                    or function_string[i] == '(' \
                    or function_string[i] == ')' \
                    or function_string[i] == ' ':
                continue
            elif function_string[i].isdigit():
                continue
            else:
                UIFunctions.setFunctionStringError(self, 'You must enter a function with a variable x only')
                return False

        # check if there is unbalanced parentheses
        if function_string.count('(') != function_string.count(')'):
            UIFunctions.setFunctionStringError(self, 'You must enter a function with balanced parentheses')
            return False

        # check if there is a division by zero
        if '/0' in function_string:
            UIFunctions.setFunctionStringError(self, 'You must not divide by zero')
            return False

        return True

    def isValidInterval(self, min_limit, max_limit):

        """
        check if the interval is valid
        :param min_limit: user entered min limit
        :param max_limit: user entered max limit
        :return: True if the interval is valid, False otherwise
        """

        if max_limit == min_limit:
            UIFunctions.setMaxMinLimitError(self, self.ui.maxLimitNumber,
                                            'You must enter a max limit that is not equal '
                                            'to the min limit')
            UIFunctions.setMaxMinLimitError(self, self.ui.minLimitNumber,
                                            'You must enter a max limit that is not equal '
                                            'to the min limit')
            return False

        # if user entered a max limit that is less than the min limit
        if max_limit < min_limit:
            UIFunctions.setMaxMinLimitError(self, self.ui.maxLimitNumber, 'You must enter a max limit that is greater '
                                                                          'than the min limit')
            UIFunctions.setMaxMinLimitError(self, self.ui.minLimitNumber, 'You must enter a max limit that is greater '
                                                                          'than the min limit')
            return False

        return True

    def getFunctionString(self):
        """
        get the function string from the text box
        :return: the function string
        """
        return self.ui.functionString.text()

    def getMaxMinValues(self):
        """
        get the max and min values from the spin boxes
        :return: the max and min values
        """

        return self.ui.maxLimitNumber.value(), self.ui.minLimitNumber.value()

    def plotFunction(self, function_string, min_limit, max_limit):

        """
        plot the function on the canvas
        :param function_string: user entered function
        :param min_limit: user entered min limit
        :param max_limit: user entered max limit
        :return: None
        """

        # create a numpy array of x values from the min limit to the max limit
        x = np.linspace(min_limit, max_limit, 500)

        # evaluate the function

        try:
            y = eval(function_string)
        except:
            UIFunctions.setFunctionStringError(self, 'You must enter a valid function')
            return

        new_x, y = Functions.save_eval(self, x, function_string)

        # if there is a plot already, clear it
        if self.plotExists:
            self.figure.clear()
            self.plotExists = False

        # add the subplot to the figure
        ax = self.figure.add_subplot(111)

        # change the background color of the subplot
        ax.set_facecolor(color='#272c36')
        self.figure.patch.set_facecolor('#272c36')

        # change the color of the labels to white
        ax.xaxis.label.set_color('#FFFFFF')
        ax.yaxis.label.set_color('#FFFFFF')

        # set the labels of the x and y axis
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')

        # remove the borders of the subplot
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        ax.tick_params(axis='x', colors='#FFFFFF')
        ax.tick_params(axis='y', colors='#FFFFFF')

        # Show the x and y axes
        ax.axhline(0, color='white', linewidth=0.2)  # x-axis
        ax.axvline(0, color='white', linewidth=0.2)  # y-axis

        # plot the function
        ax.plot(new_x, y, color='#55aaff')

        # draw the canvas
        self.plotExists = True
        self.canvas.draw()

    def save_eval(self, x_vals, function_string):
        valid_x = []
        valid_y = []

        for x in x_vals:
            y = Functions.catch_zero_division(self, x, function_string)
            if y is not None:
                valid_x.append(x)
                valid_y.append(y)

        return np.array(valid_x), np.array(valid_y)

    def catch_zero_division(self, x, function_string):
        try:
            result = eval(function_string, {"x": x})
            return result

        except ZeroDivisionError:
            print("Error: Division by zero occurred.")
            return None
