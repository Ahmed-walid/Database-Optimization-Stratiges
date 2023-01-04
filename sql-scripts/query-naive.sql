
SELECT C.FIRST_NAME, C.LAST_NAME, P.COST
FROM customer AS C
INNER JOIN customer_offer AS CO ON C.ID = CO.CUSTOMER_ID
INNER JOIN complaints AS CT ON C.ID = CT.CUSTOMER_ID
INNER JOIN offer AS O ON CO.OFFER_ID = O.ID
INNER JOIN plan AS P ON C.PLAN_ID = P.ID
WHERE CT.DATE > '2015-01-01' AND O.PRICE > 3000;

---------------------------------------------------------

SELECT E.FIRST_NAME, E.LAST_NAME
FROM employee AS E
INNER JOIN complaints AS CO ON E.SSN = CO.EMPLOYEE_ID
INNER JOIN customer AS C ON CO.CUSTOMER_ID = C.ID
INNER JOIN customer_service AS CS ON C.ID = CS.CUSTOMER_ID
INNER JOIN service AS S ON CS.SERVICE_ID = S.SERVICE_ID
WHERE CO.DATE > '2019-01-01' AND S.COST > 150;

---------------------------------------------------------
 
SELECT  B.LOCATION, D.MGR_SSN
FROM branch AS B
INNER JOIN employee AS E ON B.BNUM = E.BRANCH
INNER JOIN department AS D ON E.DEPT_NUM = D.DNUM
INNER JOIN faq AS F ON F.SSN = E.SSN
WHERE F.IS_ANSWERED = 1;

---------------------------------------------------------

SELECT D.DNAME, C.FIRST_NAME, C.LAST_NAME, E.FIRST_NAME, E.LAST_NAME
FROM department AS D
INNER JOIN employee AS E ON D.DNUM = E.DEPT_NUM
INNER JOIN complaints AS CT ON E.SSN = CT.EMPLOYEE_ID
INNER JOIN customer AS C ON CT.CUSTOMER_ID = C.ID
INNER JOIN card AS CD ON C.ID = CD.CUSTOMER_ID
WHERE CD.VALUE > 5000;

---------------------------------------------------------