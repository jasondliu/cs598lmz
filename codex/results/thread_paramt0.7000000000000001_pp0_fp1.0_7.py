import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# 시간 측정 시작
start = time.time()

print("\n--- Time Checkpoint 1 ---")
print("\n--- Time Checkpoint 2 ---")
print("\n--- Time Checkpoint 3 ---")

# 시간 측정 종료
end = time.time()
print("\n시간 측정 종료")
print("실행 시간 : {0:.3f}초".format(end - start))

# Time Checkpoint 1 : 0.000초
# Time Checkpoint 2 : 0.000초
# Time Checkpoint 3 : 0.000초
# 시간 측정 종료
# 실행 시간 : 0.001초
