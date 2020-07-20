divi :: Int -> Int -> Int
divi m n = 
  (if m < n then 0
  else 1 + ( divi ( m - n ) n ))