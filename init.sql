CREATE TABLE public.customers (
	customer_email varchar NOT NULL,
	age_at_first_purchase smallint NULL,
	country varchar NULL,
	zip_code varchar NULL,
	CONSTRAINT customers_pk PRIMARY KEY (customer_email)
);
CREATE TABLE public.products (
	product_id varchar NOT NULL,
	product_name varchar NULL,
	product_taxable_category varchar NULL,
	CONSTRAINT products_pk PRIMARY KEY (product_id)
);

CREATE TABLE public.subscriptions (
	subscription_id varchar NOT NULL,
	customer_email varchar NULL,
	CONSTRAINT subscriptions_pk PRIMARY KEY (subscription_id),
	CONSTRAINT subscriptions_customers_fk FOREIGN KEY (customer_email) REFERENCES public.customers(customer_email) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE public.orders (
	order_id varchar NOT NULL,
	order_status varchar NULL,
	order_type varchar NULL,
	product_id varchar NULL,
	total decimal NULL,
	tax decimal NULL,
	fee decimal NULL,
	coupon_applied varchar NULL,
	quantity smallint NULL,
	currency varchar NULL,
	balance_earnings decimal NULL,
	balance_currency varchar NULL,
	"source" varchar NULL,
	checkout varchar NULL,
	"date" timestamp NULL,
	subscription_id varchar NULL,
	CONSTRAINT orders_pk PRIMARY KEY (order_id),
	CONSTRAINT orders_products_fk FOREIGN KEY (product_id) REFERENCES public.products(product_id) ON DELETE RESTRICT ON UPDATE CASCADE,
	CONSTRAINT orders_subscriptions_fk FOREIGN KEY (subscription_id) REFERENCES public.subscriptions(subscription_id) ON DELETE RESTRICT ON UPDATE CASCADE
);
