
# 7. If a valid menu option is chosen, call a function named similarly to the menu option that prints the menu option chosen i.e. def buy_burger() prints('Burger bought!')
# 8. The menu options should repeatedly be displayed after each selection (and appropriate delegate function is called) until user selects exist

# ------ Place code below here \/ \/ \/ ------


def display_menu(menu):
    stack = 0
    if isinstance(menu, tuple) == False:
        return -1
    else:
        menu_size = len(menu)
        i = 1
        for item in range(menu_size):
            print (i+". " + menu[i])
            i = i+1
        print("Exit by pressing" + size+1)
    def input(n):
        n = input("Please type an item number (1-" + size + "). Then press enter to order: ", n)
        stack = n
        if ((n <= 0 or n > (size+1)) or isinstance(n, int) == False):
            print("That entry was invalid.\n")
            input(n)
        elif n == (size + 1):
            input(n)
            print("Menu has " + size + " items total.")

        else:               
            if ("buy".casefold() in item and "ethereum".casefold() in item):
                def buy_ethereum():
                    print("ethereum bought")
                buy_ethereum()
            elif ("buy".casefold() in item and "bitcoin".casefold() in item):
                def buy_bitcoin():
                    print("bitcoin bought")
                buy_bitcoin()
            elif("sell".casefold() in item and "ethereum".casefold() in item):
                def sell_ethereum():
                    print("ethereum sold")
                sell_ethereum()
            else("sell".casefold() in item and "ethereum".casefold() in item):
                def sell_bitcoin():s
                    print("bitcoin sold")
                sell_bitcoin()

                

# def test_exercise08(self):
#     print('Testing exercise 8')
#     menu = ['Buy Bitcoin','Buy Ethereum','Sell Bitcoin','Sell Ethereum']
#     r, l = display_menu(menu)
#     self.assertEqual(r,-1)
#     self.assertEqual(l,4)
#     menu = ('Buy Bitcoin','Buy Ethereum','Sell Bitcoin','Sell Ethereum')
#     r, l = display_menu(menu)
#     self.assertTrue(r > 0)
#     self.assertEqual(l,4)