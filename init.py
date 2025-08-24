import json
import copy
import time
from bubble_sort import bubble_sort
from merge_sort import merge_sort

# JSONファイル読み込み
with open("data.json", "r") as f:
    arr = json.load(f)

bubble_arr = copy.deepcopy(arr)
merge_arr = copy.deepcopy(arr)

# バブルソート 結果
start = time.time()
bubble_result = bubble_sort(bubble_arr)
end = time.time()

print("バブルソート結果:")
print(bubble_result)
print("バブルソート実行時間:", end - start, "秒")

# マージソート 結果
start = time.time()
merge_result = merge_sort(merge_arr)
end = time.time()

print("マージソート結果:")
print(merge_result)
print("マージソート実行時間:", end - start, "秒")