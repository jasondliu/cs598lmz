import types
types.BooleanType

# get all the local vars and globals
def show_vars(my_locals,my_globals):
    print "my_locals:"
    for k,v in my_locals.iteritems():
        print "\t",k,"\t",v
    print "my_globals:"
    for k,v in my_globals.iteritems():
        print "\t",k,"\t",v

#-------------------------------------
# return a sub set of cards within a range
# of a given suit
#-------------------------------------
def within_suit(cards,suit,low,high):

    # list of cards
    # suit is a string
    # low and high are lists of ints

    # get cards of a given range
    # make an empty list
    card_list = []
    # get the cards in the hand
    for i in range(len(cards)):
        # get the card
        card = cards[i]
        # ignore trump cards
        if card.suit == suit:
            if card.int_value >= low and
