### SQL Notes



##### Filtering data

SELECT \* FROM log\_in\_attempts

WHERE login\_time < '07:00:00';





##### Between times

SELECT \* FROM log\_in\_attempts

WHERE login\_time BETWEEN '06:00:00' AND '07:00:00';





##### Filter by event\_id

SELECT \* FROM log\_in\_attempts

WHERE event\_id BETWEEN 100 AND 150;





##### Employees in Marketing

SELECT \* FROM employees

WHERE department = 'Marketing';





##### Employees in Finance or Sales

SELECT \* FROM employees

WHERE department = 'Finance' OR department = 'Sales';





##### Employees not in IT

SELECT \* FROM employees

WHERE department != 'IT';





##### Using LIKE for patterns

SELECT \* FROM employees

WHERE email LIKE '%@gmail.com';





##### Using JOIN

SELECT e.name, o.office

FROM employees e

INNER JOIN offices o

ON e.office\_id = o.id;



