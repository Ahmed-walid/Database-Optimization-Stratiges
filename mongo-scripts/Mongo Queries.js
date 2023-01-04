
// SELECT C.FIRST_NAME, C.LAST_NAME, P.COST
// FROM customer AS C, customer_offer AS CO, complaints AS CT, offer AS O, plan as P
// WHERE CT.DATE > '2015-01-01' AND CT.CUSTOMER_ID = C.ID AND C.ID = CO.CUSTOMER_ID AND CO.OFFER_ID = O.ID AND O.PRICE > 3000 AND C.PLAN_ID = P.ID ;


query = db.customer.aggregate([
    {
        $lookup: {
            from: "customer_offer",
            localField: "ID",
            foreignField: "CUSTOMER_ID",
            as: "customer_offer"
        }
    },
    {
        $unwind: "$customer_offer"
    },
    {
        $lookup: {
            from: "complaints",
            localField: "ID",
            foreignField: "CUSTOMER_ID",
            as: "complaints"
        }
    },
    {
        $unwind: "$complaints"
    },
    {
        $lookup: {
            from: "offer",
            localField: "customer_offer.OFFER_ID",
            foreignField: "ID",
            as: "offer"
        }
    },
    {
        $unwind: "$offer"
    },
    {
        $lookup: {
            from: "plan",
            localField: "PLAN_ID",
            foreignField: "ID",
            as: "plan"
        }
    },
    {
        $unwind: "$plan"
    },
    {
        $match: {
            "complaints.DATE": {
                $gt: "2015-01-01"
            },
            "offer.PRICE": {
                $gt: 3000
            }
        }
    },
    {
        $project: {
            "FIRST_NAME": 1,
            "LAST_NAME": 1,
            "COST": "$plan.COST"
        }
    }
])

// convert sql query to mongo query to be run from javascript
// SELECT CO.EMPLOYEE_FIRST_NAME , CO.EMPLOYEE_LAST_NAME 
// FROM customer AS C, complaints AS CO, customer_service AS CS, service AS S
// WHERE CO.DATE > '2019-01-01' AND CO.CUSTOMER_ID = C.ID AND CS.CUSTOMER_ID = C.ID AND CS.SERVICE_ID = S.SERVICE_ID AND S.COST > 150;

query = db.customer.aggregate([
    {
        $lookup: {
            from: "complaints",
            localField: "ID",
            foreignField: "CUSTOMER_ID",
            as: "complaints"
        }
    },
    {
        $unwind: "$complaints"
    },
    {
        $lookup: {
            from: "customer_service",
            localField: "ID",
            foreignField: "CUSTOMER_ID",
            as: "customer_service"
        }
    },
    {
        $unwind: "$customer_service"
    },
    {
        $lookup: {
            from: "service",
            localField: "customer_service.SERVICE_ID",
            foreignField: "SERVICE_ID",
            as: "service"
        }
    },
    {
        $unwind: "$service"
    },
    {
        $match: {
            "complaints.DATE": {
                $gt: "2019-01-01"
            },
            "service.COST": {
                $gt: 150
            }
        }
    },
    {
        $project: {
            "EMPLOYEE_FIRST_NAME": "$complaints.EMPLOYEE_FIRST_NAME",
            "EMPLOYEE_LAST_NAME": "$complaints.EMPLOYEE_LAST_NAME"
        }
    }
])

// -----------------
// SELECT  B.LOCATION, E.MGR_SSN
// FROM branch AS B, employee AS E, faq AS F
// WHERE F.IS_ANSWERED = 1 AND F.SSN = E.SSN AND B.BNUM = E.BRANCH;

query = db.branch.aggregate([
    {
        $lookup: {
            from: "employee",
            localField: "BNUM",
            foreignField: "BRANCH",
            as: "employee"
        }
    },
    {
        $unwind: "$employee"
    },
    {
        $lookup: {
            from: "faq",
            localField: "employee.SSN",
            foreignField: "SSN",
            as: "faq"
        }
    },
    {
        $unwind: "$faq"
    },
    {
        $match: {
            "faq.IS_ANSWERED": 1
        }
    },
    {
        $project: {
            "LOCATION": 1,
            "MGR_SSN": "$employee.MGR_SSN"
        }
    }
])


// -----------------
// SELECT D.DNAME, C.FIRST_NAME, C.LAST_NAME, E.FIRST_NAME, E.LAST_NAME
// FROM department AS D, employee AS E, complaints AS CT, customer AS C, card AS CD
// WHERE D.DNUM = E.DEPT_NUM AND E.SSN = CT.EMPLOYEE_ID AND C.ID = CT.CUSTOMER_ID AND CD.CUSTOMER_ID = C.ID AND CD.VALUE > 5000;

query = db.department.aggregate([
    {
        $lookup: {
            from: "employee",
            localField: "DNUM",
            foreignField: "DEPT_NUM",
            as: "employee"
        }
    },
    {
        $unwind: "$employee"
    },
    {
        $lookup: {
            from: "complaints",
            localField: "employee.SSN",
            foreignField: "EMPLOYEE_ID",
            as: "complaints"
        }
    },
    {
        $unwind: "$complaints"
    },
    {
        $lookup: {
            from: "customer",
            localField: "complaints.CUSTOMER_ID",
            foreignField: "ID",
            as: "customer"
        }
    },
    {
        $unwind: "$customer"
    },
    {
        $lookup: {
            from: "card",
            localField: "customer.ID",
            foreignField: "CUSTOMER_ID",
            as: "card"
        }
    },
    {
        $unwind: "$card"
    },
    {
        $match: {
            "card.VALUE": {
                $gt: 5000
            }
        }
    },
    {
        $project: {
            "DNAME": 1,
            "CUSTOMER_FIRST_NAME": "$customer.FIRST_NAME",
            "CUSTOMER_LAST_NAME": "$customer.LAST_NAME",
            "EMPLOYEE_FIRST_NAME": "$employee.FIRST_NAME",
            "EMPLOYEE_LAST_NAME": "$employee.LAST_NAME"
        }
    }
])

