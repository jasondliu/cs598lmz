import threading
threading.enumerate()

#%%

############################################################################################################
#                                                                                                          #
# 3. 쓰레드 동기화와 잠금 객체                                                                             #
#                                                                                                          #
# 쓰레드 세이프를 위해서는 여러 쓰레드가 공유 변수에 접근할 때 특정 시점에 오직 하나의 쓰레드만 접근 가능하도록 해야 한다.
# 접근을 제한하는
