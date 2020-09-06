
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5)) 

v_c = pd.merge(visits, cart, how='left')
print(len(v_c))
null_cart_time=len(v_c[v_c.cart_time.isnull()])
print(null_cart_time)
#visit no cart
print(float(null_cart_time)/len(v_c))

cart_checkout_left = pd.merge(cart, checkout, how='left')
null_checkout_time = len(cart_checkout_left[cart_checkout_left.checkout_time.isnull()])
print(null_checkout_time)
# cart no checkout
print(float(null_checkout_time)/len(cart_checkout_left))

all_data = visits.merge(cart, how='left')\
                 .merge(checkout, how='left')\
                 .merge(purchase, how='left')

print(all_data.head(5))
checkout_no_purchase=len(all_data[(~all_data['checkout_time'].isnull() )& (all_data['purchase_time'].isnull())])
print(checkout_no_purchase)
print(float(checkout_no_purchase)/len(all_data))

#visit but no cart is the weakest part.
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase.mean()) 

    
                      
