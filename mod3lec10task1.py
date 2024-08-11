def product_of_min_max(arr):
  def find_min_max(arr, start, end):
      if start > end:
          return float('inf'), float('-inf')
      min_val = max_val = arr[start]
      for i in range(start, end + 1):
          if arr[i] < min_val:
              min_val = arr[i]
          if arr[i] > max_val:
              max_val = arr[i]
      return min_val, max_val

  n = len(arr)
  min_val, max_val = find_min_max(arr, 0, n - 1)
  return min_val * max_val

n = int(input())
arr = list(map(int, input().split()))
print(product_of_min_max(arr))
