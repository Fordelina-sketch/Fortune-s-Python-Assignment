def print_pattern_table(n):
    print(f"\n--- Multiplication Table up to {n} ---")
    
    # nested loops for the table
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            ans = i * j
            
            # highlight multiples of 3, 5, or 7
            if ans % 3 == 0 or ans % 5 == 0 or ans % 7 == 0:
                row = row + str(ans) + "*\t"
            else:
                row = row + str(ans) + "\t"
                
        print(row)
        
    print(f"\n--- Visual Pattern for n = {n} ---")
    # basic triangle pattern using nested loops
    for i in range(1, n + 1):
        stars = ""
        for j in range(i):
            stars += "*"
        print(stars)

# Run tests for n = 10 and n = 15 as requested
print_pattern_table(10)
print_pattern_table(15)