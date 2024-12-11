import requests
import re
import tkinter as tk

def fetch_exchange_rate():
    url = "https://v6.exchangerate-api.com/v6/a002013ab04e441f414cefea/latest/USD"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    # Extract EUR rate from the response text using regex
    pattern = r'"EUR"\s*:\s*([0-9.]+)'
    match = re.search(pattern, response.text)
    if not match:
        return None

    eur_to_usd = float(match.group(1))
    return eur_to_usd

def create_widget(eur_rate):
    # Create main window
    root = tk.Tk()
    root.title("Daily USD/EUR Exchange Rate")
    
    # Set window attributes:
    # Remove the title bar (optional): uncomment next line if you want a borderless window
    root.overrideredirect(True)
    
    # Set it always on top
    root.attributes("-topmost", True)
    
    # Position the window in a corner (adjust values according to your screen size)
    # e.g., "200x100+1500+50" means a 200x100px window placed at x=1500, y=50 on your screen
    root.geometry("200x100+1240+0")

   # If we have a rate
    if eur_rate is not None:
        usd_rate = 1 / eur_rate   # How many USD for 1 EUR
        # 10 EUR in USD
        ten_eur_in_usd = 10 * usd_rate
        # 10 USD in EUR
        ten_usd_in_eur = 10 * eur_rate

        # Create multiline label text
        label_text = (
            f"1 USD = {eur_rate:.4f} EUR\n"
            f"1 EUR = {usd_rate:.4f} USD\n"
            f"10 EUR = {ten_eur_in_usd:.4f} USD\n"
            f"10 USD = {ten_usd_in_eur:.4f} EUR"
        )
    else:
        label_text = "Rate not available"
    
    label = tk.Label(root, text=label_text, font=("Arial", 12), justify="left")
    label.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    eur_rate = fetch_exchange_rate()
    create_widget(eur_rate)