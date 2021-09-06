# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# G Tedeschi, 8.29.21, Added code to Data and Processing sections
# G Tedeschi, 8.31.21, Added code to Presentation section
# G Tedeschi, 9.03.21, Added code to main body
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
import time  # Use to add pauses in main body while loop for readability

strFileName = 'products.txt'
lstOfProductObjects = []
user_choice = ""  # Captures user choice for options in menu

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        G Tedeschi, 8.29.21, Added code to Product class
    """

    #  Constructor
    def __init__(self, p_name="", p_price=0.0):
        #  Attributes
        self.__product_name = p_name
        self.__product_price = float(p_price)

    #  Properties
    #  product_name getter
    @property
    def product_name(self):
        return str(self.__product_name).title()

    #  product_name setter
    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    #  product_price getter
    @property
    def product_price(self):
        return float(self.__product_price)

    #  product_price setter
    @product_price.setter
    def product_price(self, value):
        self.__product_price = float(value)

    #  Methods
    def __str__(self):
        return self.__product_name + ", " + str(self.__product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        G Tedeschi,8.29.21, Added functions to class
    """

    @staticmethod
    def read_data_from_file(file):
        """ Reads data from a file into a list of Product objects

        :param file: (string) with name of file:
        :return p_list: (list) of objects:
        """
        objFile = open(file, "r")
        p_list = []
        for row in objFile.read().splitlines():
            p_name, p_price = row.split(", ")
            obj_new = Product(p_name, float(p_price))
            p_list.append(obj_new)
        objFile.close()
        return p_list

    @staticmethod
    def save_data_to_file(file, list_of_product_objects):
        """ Writes data to a file from a list of Product objects

        :param file: (string) with name of file:
        :param list_of_product_objects: (list) of objects:
        """
        objFile = open(file, "w")
        for row in list_of_product_objects:
            objFile.write(str(row) + "\n")
        objFile.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Presents menu and data to user and captures user input

     methods:
         print_menu options:

         capture_user_choice: -> choice

         present_data(p_list):

         get_user_product_data(): -> user_obj

     changelog: (When,Who,What)
         RRoot,1.1.2030,Created Class
         G Tedeschi,8.31.21, Added functions to class
     """

    @staticmethod
    def print_menu_options():
        """ Prints menu of options to user

        """
        print('''
        Menu of Options:
        1) Show current product data
        2) Add product data
        3) Save data to file
        4) Exit
        ''')
        print()

    @staticmethod
    def capture_user_choice():
        """ Captures user menu choice with error handling to prevent invalid choice

        :return choice: (string) with user's choice
        """
        while(True):
            try:
                choice = str(input("Which action would you like to perform? [1 to 4] - ").strip())
                if choice not in ["1", "2", "3", "4"]:
                    raise Exception("Please choose 1, 2, 3, or 4.")
                break
            except Exception as e:
                print(e)
        return choice

    @staticmethod
    def present_data(p_list):
        """ Loops through list of objects to print data

        :param p_list: (list) of objects
        """
        for row in p_list:
            print(str(row))

    @staticmethod
    def get_user_product_data():
        """ Capture user product and price data and store in a Product object

        :return user_obj: Product object storing product name and price
        """
        while(True):
            try:
                new_p_name = input("Please enter a product name: ").strip()
                if new_p_name.isnumeric() == True:
                    raise Exception("Product name cannot be a number.")
                break
            except Exception as e:
                print(e)
                print()

        while(True):
            try:
                new_p_price = float(input("Please enter its price: ").strip())
                break
            except ValueError:
                print("Product price must be a number.")
                print()

        user_obj = Product(new_p_name,new_p_price)
        return user_obj

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while(True):
    # Show user a menu of options
    IO.print_menu_options()

    # Get user's menu option choice
    user_choice = IO.capture_user_choice()

    # Show user current data in the list of product objects
    if user_choice == "1":
        IO.present_data(lstOfProductObjects)
        print()

    # Let user add data to the list of product objects
    elif user_choice == "2":
        lstOfProductObjects.append(IO.get_user_product_data())
        print("Data added to list!\n")

    # let user save current data to file and exit program
    elif user_choice == "3":
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("Data saved to file!\n")

    else:
        break

    time.sleep(0.75)  # Use to add pause before menu prints each time for readability
# Main Body of Script  ---------------------------------------------------- #