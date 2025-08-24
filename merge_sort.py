# マージソート
def merge_sort(arr):
    # 配列が１つだけになったらマージ処理を実行
    if len(arr) <= 1:
        return arr

    arr_center = len(arr) // 2
    # 再帰処理
    arr_left = merge_sort(arr[:arr_center])
    arr_right = merge_sort(arr[arr_center:])

    # マージ処理
    return merge(arr_left, arr_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 比較で残った要素を最後に追加
    result.extend(left[i:])
    result.extend(right[j:])
    return result
