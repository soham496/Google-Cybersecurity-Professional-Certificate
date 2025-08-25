## 

## Apply filters to SQL queries





##### Project description



\[In this project, I practiced writing SQL queries that use filtering conditions to find specific information from database tables. I used operators like WHERE, LIKE, BETWEEN, AND, OR, and NOT to filter records by time, date, department, and location.]





##### Retrieve after hours failed login attempts



\[SELECT \*

FROM log\_in\_attempts

WHERE login\_time < '07:00:00' AND success = 0;

###### Explanation:

This query retrieves all login attempts that happened before 07:00:00 (before work hours) and were unsuccessful (success = 0). I combined two conditions using the AND operator.]



##### Retrieve login attempts on specific dates



\[SELECT \*

FROM log\_in\_attempts

WHERE login\_date = '2023-07-15';

###### Explanation:

Here, I filtered the table by a specific date (login\_date). Only rows from July 15, 2023 will appear. This shows how to filter results by date values.]





##### Retrieve login attempts outside of Mexico



\[SELECT \*

FROM log\_in\_attempts

WHERE country NOT LIKE 'Mexico';

###### Explanation:

The NOT keyword is used to exclude rows. This query returns all login attempts where the country column is anything other than "Mexico".]





##### Retrieve employees in Marketing



\[SELECT \*

FROM employees

WHERE department = 'Marketing';

###### Explanation:

This query selects all employees who work in the Marketing department.]





##### Retrieve employees in Finance or Sales



\[SELECT \*

FROM employees

WHERE department = 'Finance' OR department = 'Sales';

###### Explanation:

The OR operator is used here to return employees who belong to either Finance or Sales.]





##### Retrieve all employees not in IT



\[SELECT \*

FROM employees

WHERE department NOT LIKE 'IT';

###### Explanation:

This query retrieves every employee except those in the IT department, using the NOT operator.]





##### Summary

\[n this activity, I used SQL filters to focus on specific subsets of data. I learned how to:

Filter by time and date





* Use AND / OR to combine multiple conditions





* Exclude data with NOT





* Use LIKE to match patterns





* Retrieve only the rows that are relevant to the problem I am solving





* This practice showed me how powerful SQL filters are when investigating issues or analyzing employee/login data.]



