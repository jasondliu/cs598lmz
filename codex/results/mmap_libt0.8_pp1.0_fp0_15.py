import mmap
import contextlib
import sys
import string 
import os


#print '\n'.join([k for k,v in globals().iteritems() if isinstance(v,type)])
#column_names = 'id,addr,type,nick,guid,name,service,country,kills,deaths,kdratio,skill,join_date,time,credits,duel_wins,money_won,karma,email,legend,fpgz,fkpz,fpkz,fpgf,fkpg,fpkp'
#column_names = 'id,addr,type,nick,guid,name,service,country,kills,deaths,kdratio,skill,join_date,time,credits,duel_wins,money_won,karma,email,legend,fpgz,fkpz,fpkz,fpgf,fkpg,fpkp'
#column_names = 'id,addr,type,nick,guid,name,service,country,kills,deaths,kdratio,
