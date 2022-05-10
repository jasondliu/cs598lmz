import threading
# Test threading daemon mode
# 守护线程：守护线程的存在与否不影响主线程的退出。守护线程在主线程结束后立即终止。
# 守护线程被用于在后台执行一些任务而不用太多担心主线程是否终止,常用于实时事件监控
# setDaemon(True) 将线程声明为守护线程，主线程退出后守护线程也会随之退
