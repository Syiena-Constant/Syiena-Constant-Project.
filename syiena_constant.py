import math

def calculate_syiena(n_terms):
    return sum(1 / (n**2) for n in range(1, n_terms + 1))

if __name__ == "__main__":
    print(f"Syiena Constant (Theoretical): {math.pi**2 / 6}")
    print(f"Syiena Constant (1 Million terms): {calculate_syiena(1000000)}")
                     
