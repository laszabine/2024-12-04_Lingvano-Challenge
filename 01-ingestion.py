from configparser import ConfigParser
import csv
import psycopg2

def cleanup_numerals(mynum: str): 
    # Remove thousands separator: 
    mynum = mynum.replace(',', '')

    return mynum

# Connect to database
try: 
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="DUTHZawxbNXADxzTezhKMtMM5agva9g39nD8S7JwwphSihwu67RbCZbHw2Nsx9b2"
    )

    with connection.cursor() as cursor:

        # Open CSV
        with open('customer_transactions.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            
            for row in reader:

                ################## Create customer if doesn't exist
                customer_email = row["Customer Email"]
                customer_age_at_first_purchase = row["Customer age (at first purchase)"]
                customer_country = row["Customer Country"]
                customer_zip_code = row["Customer Zip Code"]
                # Check whether customer already exists 
                cursor.execute(
                    """SELECT * FROM customers where customer_email = %s""", 
                    (customer_email,)
                )
                if not cursor.fetchone(): 
                    print(f"Creating customer {customer_email} ...")
                    # If not: create customer
                    cursor.execute(
                        """INSERT INTO customers (
                                customer_email, 
                                age_at_first_purchase, 
                                country, 
                                zip_code
                            ) VALUES (%s, %s, %s, %s)""", 
                        (
                            customer_email, 
                            customer_age_at_first_purchase, 
                            customer_country, 
                            customer_zip_code,
                        ),
                    )
                    connection.commit()
                # else: 
                #     print(f"Customer {customer_email} already exists.")

                ################### Create products
                product_id = row["Product ID"]
                product_name = row["Product Name"]
                product_taxable_category = row["Product Taxable Category"]
                # Check whether the product already exists 
                cursor.execute(
                    """SELECT * FROM products where product_id = %s""", 
                    (product_id,)
                )
                if not cursor.fetchone(): 
                    print(f"Creating product {product_id} ...")
                    # If not: create customer
                    cursor.execute(
                        """INSERT INTO products (
                                product_id, 
                                product_name, 
                                product_taxable_category
                            ) VALUES (%s, %s, %s)""", 
                        (
                            product_id, 
                            product_name, 
                            product_taxable_category,
                        ),
                    )
                    connection.commit()
                # else: 
                #     print(f"Product {product_id} already exists.")

                ################### Create subscriptions
                subscription_id = row["User Subscription ID"]
                # Check whether the subscription already exists 
                cursor.execute(
                    """SELECT * FROM subscriptions where subscription_id = %s""", 
                    (subscription_id,)
                )
                if not cursor.fetchone(): 
                    print(f"Creating subscription {subscription_id} ...")
                    # If not: create subscription
                    cursor.execute(
                        """INSERT INTO subscriptions (
                                subscription_id, 
                                customer_email 
                            ) VALUES (%s, %s)""", 
                        (
                            subscription_id, 
                            customer_email, 
                        ),
                    )
                    connection.commit()
                # else: 
                #     print(f"Subscription {subscription_id} already exists.")

                ################## Creating orders
                order_id = row["Order ID"]
                # Check whether the order already exists 
                cursor.execute(
                    """SELECT * FROM orders where order_id = %s""", 
                    (order_id,)
                )
                if not cursor.fetchone(): 
                    print(f"Creating order {order_id} ...")
                    # If not: create order
                    cursor.execute(
                        """INSERT INTO orders (
                                order_id, 
                                order_status, 
                                order_type, 
                                product_id, 
                                total, 
                                tax, 
                                fee, 
                                coupon_applied, 
                                quantity, 
                                currency, 
                                balance_earnings, 
                                balance_currency, 
                                source, 
                                checkout, 
                                date, 
                                subscription_id
                            ) VALUES (%s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, 
                                %s, %s, 
                                %s, %s, %s, %s
                            )""", 
                        (
                            order_id, 
                            row["Order Status"], 
                            row["Order Type"], 
                            product_id, 
                            cleanup_numerals(row["Total"]) or 0, 
                            cleanup_numerals(row["Tax"]) or 0, 
                            cleanup_numerals(row["Fee"]) or 0, 
                            cleanup_numerals(row["Coupon Applied"]) or 0, 
                            cleanup_numerals(row["Quantity"]) or 0, 
                            row["Currency"], 
                            cleanup_numerals(row["Balance Earnings"]) or 0, 
                            row["Balance Currency"], 
                            row["Source"], 
                            row["Checkout"], 
                            row["Date"], 
                            subscription_id,
                        ),
                    )
                    connection.commit()
                else: 
                    print(f"Order {order_id} already exists.")

    
except (Exception, psycopg2.DatabaseError) as error: 
    print(error)
finally:
    connection.close()
