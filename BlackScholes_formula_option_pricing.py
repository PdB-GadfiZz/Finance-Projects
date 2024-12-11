import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
        d1 = (math.log(S /K) + (r + 0.5 * sigma ** 2)*T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)

        if option_type == 'call':
                return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        elif option_type == 'put':
                return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        
# Usage examples & values to change in the formula
S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

call_price = black_scholes(S, K, T, r, sigma, option_type='call')
put_price = black_scholes(S, K, T, r, sigma, option_type='put')

print(f"Call option price: {call_price:.2f}")
print(f"Put option price: {put_price}")