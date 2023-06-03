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
        n_iterations = 10000000

        start_time = time.time()
        pi_approximation = self.monte_carlo_pi(n_iterations)
        end_time = time.time()

        execution_time = end_time - start_time

        print("Approximation of pi:", pi_approximation)
        print("Execution time:", execution_time, "seconds")