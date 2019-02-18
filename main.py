def prime_eratosthenes(n):
  if n == None:
      n=1000
  not_prime_list = [] 
  for i in range(2, n+1): 
    if i not in not_prime_list: 
      print (i) 
      for j in range(i*i, n+1, i): 
        not_prime_list.append(j) 
prime_eratosthenes(int(input("The prime_eratosthenes are:\n")))
