from datetime import datetime, timedelta
import threading
import requests
import json

class Request_thread(threading.Thread):

    def __init__(self, url):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}
        self.count = 0

    def run(self):
        http_response = requests.get(self.url)
        # Check the status code to see if the request succeeded.
        if http_response.status_code == 200:
            self.response = http_response.json()
            self.count += 1
        else:
            print('RESPONSE = ', http_response.status_code)

class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        #self.reshuffle()
        self.remaining = 52


    def reshuffle(self):
        print(f'reshuffle')
        t = Request_thread(rf'https://deckofcardsapi.com/api/deck/{self.id}/shuffle/asdfasdfads')
        t.start()
        t.join()

    def draw_card(self):
        t = Request_thread(rf'https://deckofcardsapi.com/api/deck/{self.id}/draw/')
        t.start()
        t.join()
        self.remaining = t.response['remaining']
        card = f"{t.response['cards'][0]['value']}-{t.response['cards'][0]['suit']}"
        return card

    def cards_remaining(self):
        return self.remaining


    def draw_endless(self):
        if self.remaining <= 0:
            self.reshuffle()
        return self.draw_card()


if __name__ == '__main__':

    # TODO - run the program team_get_deck_id.py and insert
    #        the deck ID here.  You only need to run the 
    #        team_get_deck_id.py program once. You can have
    #        multiple decks if you need them

    deck_id = 'pluk3jnfmbxz'

    deck = Deck(deck_id)
    for i in range(55):
        card = deck.draw_endless()
        print(i, card, flush=True)
    print()
    
    # for _ in range(54):
    #     t = Request_thread(r'https://deckofcardsapi.com/api/deck/pluk3jnfmbxz/draw/')
    #     t.start()
    #     t.join()
    #     card = t.response['cards'][0]
    #     remaining = t.response['remaining']
    #     if remaining == 0:
    #         print('reshuffling...')
    #         reshuffle_t = Request_thread(f'https://deckofcardsapi.com/api/deck/pluk3jnfmbxz/shuffle/')
    #         reshuffle_t.start()
    #         reshuffle_t.join()
    #     print(f"{card['value']}-{card['suit']}")

