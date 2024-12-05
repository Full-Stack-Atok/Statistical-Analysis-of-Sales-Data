import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"],
    "Product_A_Sales": [230, 220, 250, 275, 300, 280, 290, 310, 320, 330, 340, 360],
    "Product_B_Sales": [450, 430, 460, 480, 500, 490, 510, 520, 540, 550, 560, 580],
}

print("Sales Data for Product A and Product B over a year: ")

df = pd.DataFrame(data)

print(df)
