
QUERY 1 - 5 TABLES
SELECT C.FIRST_NAME, C.LAST_NAME, P.COST
FROM customer AS C, customer_offer AS CO, complaints AS CT, offer AS O, plan as P
WHERE CT.DATE > '2015-01-01' AND CT.CUSTOMER_ID = C.ID AND C.ID = CO.CUSTOMER_ID AND CO.OFFER_ID = O.ID AND O.PRICE > 3000 AND C.PLAN_ID = P.ID;

QUERY 2
SELECT E.FIRST_NAME, E.LAST_NAME
FROM employee AS E, customer AS C, complaints AS CO, customer_service AS CS, service AS S
WHERE CO.EMPLOYEE_ID = E.SSN AND CO.DATE > '2019-01-01' AND CO.CUSTOMER_ID = C.ID AND CS.CUSTOMER_ID = C.ID AND CS.SERVICE_ID = S.SERVICE_ID AND S.COST > 150;

QUERY 3
SELECT  B.LOCATION, D.MGR_SSN
FROM branch AS B, department AS D, employee AS E, faq AS F
WHERE F.IS_ANSWERED = 1 AND F.SSN = E.SSN AND B.BNUM = E.BRANCH AND E.DEPT_NUM = D.DNUM;

QUERY 4
SELECT D.DNAME, C.FIRST_NAME, C.LAST_NAME, E.FIRST_NAME, E.LAST_NAME
FROM department AS D, employee AS E, complaints AS CT, customer AS C, card AS CD
WHERE D.DNUM = E.DEPT_NUM AND E.SSN = CT.EMPLOYEE_ID AND C.ID = CT.CUSTOMER_ID AND CD.CUSTOMER_ID = C.ID AND CD.VALUE > 5000;