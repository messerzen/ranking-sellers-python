class SellersRanking:
    """ This Class used for sale control.    
    """

    def best_seller(self, sellers):
        """ Returns a list containing the best seller name based on key 'value'.
        Params:
            - seller(list): Must be a list of dictionaries (one dictionary for                  each seller)
        """
        try:
            best = max(sellers, key=lambda x: x['value'])
        except:
            return sellers
        else:
            best_name = [value for (key, value) in best.items() if key == 'name'] 

            return best_name

    def ranking_list(self, sellers):
        """ Returns a ranked list containing seller names based on key 'value'.
        Params:
            - seller(list): Must be a list of dictionaries (one dictionary for                  each seller)
        """
        try:
            sellers.sort(key=lambda data: data['value'], reverse=True)
        except:
            return sellers
        else:
            rank_name = list(map(lambda data: data['name'], sellers))

            return rank_name

    def best_seller_store(self, sellers, store):
        """ Returns a list containing best seller name of an specific store based on key 'value'.
        Params:
            - seller(list): Must be a list of dictionaries (one dictionary for                  each seller)
            - store (Int): number of the store.
        """

        try:
            seller_store = list(filter(lambda x: x['store'] == store, sellers))
            best = max(sellers, key=lambda x: x['value'])
        except:
            return sellers
        else:
            best_seller = max(seller_store, key=lambda x: x['value'])
            seller_name = [value for (key,value) 
                            in best_seller.items() if key=='name']

            return seller_name

    def sales_goals(self, sellers):
        """ Returns a ranked list containing all seller name that not reach the goal of 500.00.
        Params:
            - seller(list): Must be a list of dictionaries (one dictionary for                  each seller)
        """
        try:
            sellers_bg = list(filter(lambda data: data['value'] < 500.00, sellers))
            sellers_bg.sort(key=lambda data: data['value'])
            sellers_name = list(map(lambda data: data['name'], sellers_bg))
        except:
            return sellers
        else:
            return sellers_name
