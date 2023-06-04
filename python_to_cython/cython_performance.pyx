class Performance:
    def __init__(self) -> None:
        pass

    def fibonacci(self,n):
        if n <= 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)    
    
    def some_random_computations(self, n=4):
        import time
        import math
        start_time = time.time()
        starting_alpha, val = 97, 0
        my_map = {}
        for i in range(26):
            my_map[chr(starting_alpha+i)] = val+10
            val+=10 
        
        sorted_map = dict(sorted(my_map.items(), key=lambda x: x[0]))
        my_result = {}
        # Perform Random computations
        i=0
        for k, v in sorted_map.items():
            my_result[k] = self.fibonacci(v)
            i+=1
            if i==n:
                break
        i=0
        for k, v in sorted_map.items():
            i+=1
            if i>n and i<=n+2:
                my_result[k] = math.sqrt(v)
            elif i<=n+4:
                my_result[k] = math.cos(v)
            elif i<=n+6:
                my_result[k] = math.sin(v)
            elif i<26:  
                my_result[k] = (v * (v+1) + v+2**(v-1))%2 +math.sqrt(v)+math.sqrt(v-1)

        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")