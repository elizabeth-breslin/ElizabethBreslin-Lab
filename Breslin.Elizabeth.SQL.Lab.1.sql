#1.	Write a query to get Product name and quantity/unit.  
Select northwind.products.product_name, northwind.products.quantity_per_unit 
FROM northwind.products;

#2. Write a query to get current Product list (Product ID and name).  
SELECT northwind.products.id, northwind.products.product_name 
FROM northwind.products; 

#3. Write a query to get discontinued Product list (Product ID and name). 
SELECT northwind.products.id, northwind.products.product_name 
FROM northwind.products 
WHERE discontinued= '1';

#4. Write a query to get most expense and least expensive Product list (name and unit price).  
Select distinct product_name, unit_price 
From order_details 
Join products
ON products.id = order_details.product_id
Where unit_price = (Select Max(unit_price) FROM order_details) OR 
	  unit_price = (Select Min(unit_price) FROM order_details);

#5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.  
select distinct product_id, product_name, unit_price
FROM products 
Join order_details
ON products.id = order_details.product_id 
WHERE unit_price<20;

#6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.  
select distinct product_id, product_name, unit_price 
FROM products 
Join order_details 
ON products.id = order_details.product_id
WHERE unit_price between 15 AND 25;

#7. Write a query to get Product list (name, unit price) of above average price.  
select distinct product_name, unit_price 
FROM order_details 
Join products
ON products.id = order_details.product_id
WHERE unit_price > (Select AVG(unit_price) FROM order_details);

#8. Write a query to get Product list (name, unit price) of ten most expensive products.  
SELECT distinct product_name, unit_price
From order_details 
JOIN products
ON products.id = order_details.product_id
order by unit_price 
desc limit 10;

#9. Write a query to count current and discontinued products. 
Select discontinued, count(*) 
AS 'current' 
from northwind.products 
GROUP BY discontinued;

#10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  
Select northwind.products.product_name, order_details.orderQuantity, inventory_transactions.quantity
FROM products
JOIN inventory_transactions
ON products.id = order_details.product_id
AND order_details.product_id=inventory_transactions.product_id
WHERE inventory_transactions.quantity < order_details.orderQuantity;