import random
import time

class TestPerformace:

    def __init__(self):
        pass

    def monte_carlo_pi(self,n):
        inside_circle = 0
        total_points = n

        for _ in range(total_points):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            distance = x**2 + y**2

            if distance <= 1:
                inside_circle += 1

        pi_estimate = 4 * inside_circle / total_points
        return pi_estimate
    
    def test_monte_carlo_pi(self):
        n_iterations = 100000000

        start_time = time.time()
        pi_approximation = self.monte_carlo_pi(n_iterations)
        end_time = time.time()

        execution_time = end_time - start_time

        print("Approximation of pi:", pi_approximation)
        print("Execution time:", execution_time, "seconds")

    def newton_raphson(self,f, f_prime, x0, epsilon, max_iterations):
        x = x0
        iterations = 0

        while abs(self.f(x)) > epsilon and iterations < max_iterations:
            x = x - self.f(x) / self.f_prime(x)
            iterations += 1

        return x

    def f(self,x):
        return x**3 - x**2 + 2

    def f_prime(self,x):
        return 3*x**2 - 2*x
    
    def test_newton_raphson(self):
        x0 = 1 
        epsilon = 1e-6  
        max_iterations = 100000  
        start_time = time.time()
        root = self.newton_raphson(self.f, self.f_prime, x0, epsilon, max_iterations)
        end_time = time.time()

        execution_time = end_time - start_time

        print("Approximate root:", root)
        print("Execution time:", execution_time, "seconds")
    
    def fibonacci(self,n):
        if n <= 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
    
    def test_fibonacci(self, n=None):
        if not n:
            n = 40  # Value of Fibonacci number to calculate
        
        start_time = time.time()
        fib_result = self.fibonacci(n)
        end_time = time.time()

        execution_time = end_time - start_time
        print("Fibonacci number:", fib_result)
        print("Execution time:", execution_time, "seconds")

    def test_random(self):
        start_time = time.time()
        import math
        a = 10
        b = 20
        c = 30
        d = 40
        e = 50
        f = 60
        g = 70
        h = 80
        i = 90
        j = 100
        k = 110
        l = 120
        m = 130
        n = 140
        o = 150
        p = 160
        q = 170
        r = 180
        s = 190
        t = 200

        # Perform computations
        ra = self.fibonacci(b)
        rb = self.fibonacci(b)
        rc = self.fibonacci(c)
        rd = self.fibonacci(d)

        result1 = (a + b) * c / d
        result2 = math.sqrt(e) + math.sin(f)
        result3 = g ** h
        result4 = i % j
        result5 = k // l
        result6 = m * n - o + p
        result7 = q ** r % s
        result8 = math.cos(t)
        end_time = time.time()

        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")

a = TestPerformace()
a.test_random()