import types
typesOR = types.Union[str,list,dict]

class bitmask:
    #TODO add more bit strings
    m = {}   #dict of active and inactive strings
    m['mood'] = ['moody','cheery','friendly','unfriendly','unsociable','sociable']
    m['dnd'] = ['do_not_disturb','free_for_chat','chatty','chat_in_common','group_chat']
    m['attitude'] = ['positive','negative','neutral','uncertain','inadvertent','adversarial','confidant','tricky','trust']
    m['commitment'] = ['in_love','attracted','indifferent','married','engaged','complicated']
    m['communication'] = ['lengthy_conversations','roleplaying_conversations','flirting_conversations']
    #m['affiliation'] =['friend','family']
